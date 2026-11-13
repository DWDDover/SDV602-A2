from data_explorer.controller.local_controller import LocalController
from data_explorer.controller.remote_controller import RemoteController
from data_explorer.controller.login_controller import LoginController
from data_explorer.controller.data_visualiser import DataVisualiser
from data_explorer.data.message_repository import MessageRepository
from data_explorer.data.session_repository import SessionRepository
from data_explorer.data.data_source_repository import DataSourceRepository
from data_explorer.data.file_manager import FileManager
from data_explorer.testing.test_views import TestLocalView

class Result:
    def __init__(self, success, message):
        self.success = success
        self.message = message

def testing_run():
    ##Local mode testing
    test_local_controller()
    
def test_local_controller():
    file_manager = FileManager()
    test_local_view = TestLocalView()
    lc = LocalController(file_manager, test_local_view)
    
    # Simulate file selection
    lc.file_chosen("./test_data/bd-natural-increase-2010-2014.csv")
    
    # Check if dropdowns are updated correctly
    assert test_local_view.dropdown_values == {'column1': [], 'column2': []}  # Replace with actual expected columns
    
    # Simulate generating DES with valid inputs
    chart_data = lc.generate_des("Test Chart", "column1", "column2", "Select a series key")
    assert chart_data is not None  # Check if chart data is generated successfully
    
    # Simulate generating DES with missing x_key
    chart_data = lc.generate_des("Test Chart", "", "column2", "Select a series key")
    assert chart_data is None  # Should return None due to missing x_key
    assert test_local_view.error_message == "Please select x-axis and y-axis."
    
    # Simulate generating DES with invalid series_key
    chart_data = lc.generate_des("Test Chart", "column1", "column2", "invalid_series_key")
    assert chart_data is None  # Should return None due to invalid series_key
    assert test_local_view.error_message == "Series key 'invalid_series_key' not found in data source."
    
