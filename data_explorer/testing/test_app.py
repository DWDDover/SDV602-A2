from pathlib import Path

from data_explorer.controller.local_controller import LocalController
from data_explorer.controller.remote_controller import RemoteController
from data_explorer.controller.login_controller import LoginController
from data_explorer.controller.data_visualiser import DataVisualiser
from data_explorer.data.message_repository import MessageRepository
from data_explorer.data.session_repository import SessionRepository
from data_explorer.data.data_source_repository import DataSourceRepository
from data_explorer.data.user_repository import UserRepository
from data_explorer.data.file_manager import FileManager
from data_explorer.testing.test_views import TestLocalView

def testing_run():
    tests = [
        ("local mode", test_local_mode),
        ("login and registration", test_login_and_registration),
    ]
    failed_tests = 0

    for name, test in tests:
        try:
            test()
        except AssertionError as error:
            failed_tests += 1
            print(f"FAIL: {name}: {error}")
        except Exception as error:
            failed_tests += 1
            print(f"ERROR: {name}: {type(error).__name__}: {error}")
        else:
            print(f"PASS: {name}")

    if failed_tests:
        raise SystemExit(f"{failed_tests} test(s) failed")
    
def test_local_mode():
    ##Also tests file manager, data visualiser, and local controller
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
    
def test_login_and_registration():
    ##Also tests user repository and database manager
    ur = UserRepository()
    ur.delete_user("newuser")

    try:
        ##valid new user registration
        result = ur.register("newuser", "newpassword")
        assert result is not None
        assert result.username == "newuser"

        ##valid login
        result = ur.login("newuser", "newpassword")
        assert result is not None
        assert result.username == "newuser"

        ##invalid login
        result = ur.login("newuser", "wrongpassword")
        assert result is None
        
        ##invalid new user registration (username already exists)
        result = ur.register("newuser", "password1")
        assert result is None
    finally:
        ##Clean up the database even when an assertion fails
        ur.delete_user("newuser")
