from data_visualiser import DataVisualiser

if __name__ == "__main__":
    dv = DataVisualiser()
    
    dv.load_data("data/bd-natural-increase-2010-2014.csv")
    # print(dv.data)
    dv.append_data("data/bd-natural-increase-2015-2019.csv")
    # print(dv.data)
    dv.append_data("data/bd-natural-increase-2020-2022.csv")
    dv.plot_line_chart("Period", "Count", "test", series_key="Births_Deaths_or_Natural_Increase")