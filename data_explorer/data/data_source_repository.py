from data_explorer.data.database_manager import DatabaseManager
from data_explorer.model.data_source import DataSource

class DataSourceRepository:
    def __init__(self):
        self.db_manager = DatabaseManager.getInstance()

    def create_data_source(self, name, data, user_id):
        data_source_id = self.db_manager.insert_one("data_sources", {
                    "name": name,
                    "user_id": user_id,
                    "data": data,
                })
        ## returns the id in order to link the data source to a session
        return str(data_source_id)

    def get_data_source_by_id(self, datasource_id ):
        data_source = self.db_manager.find_one_by_id("data_sources", datasource_id)
        if data_source:
            return DataSource(data=data_source["data"], name=data_source["name"], data_source_id=str(data_source["_id"]))
        return None
    
    def get_sources_by_user_id(self, user_id):
        data_sources = self.db_manager.get_collection("data_sources").find({"user_id": user_id})
        sources = []
        for source in data_sources:
            ## the sources in the list do not hold the data, they are just for the controlelr to retrieve the selected ID.
            sources.append(DataSource(name=source["name"], data_source_id=str(source["_id"])))
        return sources