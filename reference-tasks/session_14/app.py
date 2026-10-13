from data_visualiser import DataVisualiser
from database_manager import DatabaseManager
from data_source import DataSource

if __name__ == "__main__":
    dv = DataVisualiser()
    
    dv.load_data("bd-natural-increase-2010-2014.csv")
    # print(dv.data)
    dv.append_data("bd-natural-increase-2015-2019.csv")
    # print(dv.data)
    dv.append_data("bd-natural-increase-2020-2022.csv")
    
    dv.data_source.save()
    
    dv.load_data_source("bd-natural-increase-2010-2014.csv")

    dv.plot_line_chart("Period", "Count", "Population", "Births_Deaths_or_Natural_Increase")
    
    