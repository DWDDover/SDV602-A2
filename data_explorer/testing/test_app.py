# from local_controller import LocalController
# from remote_controller import RemoteController
from data_explorer.testing.test_data_source import TestDataSource
from data_explorer.testing.test_file_manager import TestFileManager
from data_explorer.data.message_repository import MessageRepository

def testing_run():
    mr = MessageRepository()
    mr.create_message("user1", "123", "Hello, this is a new test message.")
    messages = mr.get_messages_by_session("123")
    for message in messages:
        print(message)
