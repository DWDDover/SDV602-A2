from pathlib import Path

from data_explorer.controller.local_controller import LocalController
from data_explorer.controller.remote_controller import RemoteController
from data_explorer.controller.login_controller import LoginController
from data_explorer.controller.data_visualiser import DataVisualiser
from data_explorer.data.message_repository import MessageRepository
from data_explorer.data.session_repository import SessionRepository
from data_explorer.data.data_source_repository import DataSourceRepository
from data_explorer.data.file_manager import FileManager
from data_explorer.testing.test_views import TestLocalView

def testing_run():
    ##Local mode testing
    test_local_mode()
    
def test_local_mode():
    file_manager = FileManager()
    test_local_view = TestLocalView()
    lc = LocalController(file_manager, test_local_view)
    
    ##file path relative for testing on other machines.
    test_file = Path(__file__).resolve().parents[1] / "test_data" / "bd-natural-increase-2010-2014.csv"
    
    ##file selection of valid file
    lc.file_chosen(str(test_file))
    assert test_local_view.dropdown_values == ["Period", "Births_Deaths_or_Natural_Increase", "Count"]

    ##valid chart generation with a series key
    chart_data = lc.generate_des(
        "Births and deaths",
        "Period",
        "Count",
        "Births_Deaths_or_Natural_Increase",
    )
    assert chart_data is not None
    assert chart_data.title == "Births and deaths"
    assert chart_data.x_key == "Period"
    assert chart_data.y_key == "Count"
    assert set(chart_data.series) == {"Births", "Deaths", "Natural_Increase"}
    assert chart_data.series["Births"] == (
        ["2010", "2011", "2012", "2013", "2014"],
        [63897.0, 61404.0, 61179.0, 58719.0, 57243.0],
    )

    ##valid chart generation without a series key
    chart_data = lc.generate_des("All data", "Period", "Count", "Select a series key")
    assert chart_data is not None
    assert list(chart_data.series) == [None]
    assert len(chart_data.series[None][0]) == 15

    ##missing axis keys
    chart_data = lc.generate_des("Missing x-axis", "", "Count", "Select a series key")
    assert chart_data is None
    assert test_local_view.error_message == "Please select x-axis and y-axis."

    ##invalid series key
    chart_data = lc.generate_des("Invalid series", "Period", "Count", "Invalid")
    assert chart_data is None
    assert test_local_view.error_message == "Series key 'Invalid' not found in data source."

    ##trying chart generation before selecting a file
    empty_controller = LocalController(FileManager(), TestLocalView())
    chart_data = empty_controller.generate_des(
        "No data", "Period", "Count", "Select a series key"
    )
    assert chart_data is None
    assert empty_controller.local_view.error_message == "Please select a CSV file first."
