from data_visualiser import DataVisualiser
from database_manager import DatabaseManager
from data_source import DataSource

from chat_app import run


if __name__ == "__main__":
    # data_visualiser = DataVisualiser()
    # data_visualiser.load_data_source("data/bd-natural-increase-2010-2014.csv")


    # data_visualiser.load_data("data/bd-natural-increase-2010-2014.csv")
    # data_visualiser.append_data("data/bd-natural-increase-2015-2019.csv")
    # data_visualiser.append_data("data/bd-natural-increase-2020-2022.csv")

    # data_visualiser.data_source.save()

    # dbm = DatabaseManager.getInstance()
    # print(dbm)
    # dbm2 = DatabaseManager.getInstance()
    # print(dbm2)

    # print(dbm.get_collection())
    # doc = {'Name': "User"}
    # print(dbm.insert_one(doc))

    # id = "6a9f85e1837d523fed4b9d13"
    # print(dbm.find_one_by_id(id))
    # print(data_visualiser.data)
    # data = DataSource("bd-natural-increase", data_visualiser.data)
    # data.save()

    # data_visualiser.plot_line_chart(
    #     "Period", "Count", "Population Natural Increase", "Births_Deaths_or_Natural_Increase")
    
    run()
