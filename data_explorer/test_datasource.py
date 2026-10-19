import unittest
from data_source import DataSource

class TestDataSource(unittest.TestCase):
    def test_columns_with_data(self):
        data = [
            {"name": "Declan", "age": 30},
            {"name": "Joe", "age": 25}
        ]
        ds = DataSource(name="Test Data", data=data)
        self.assertEqual(ds.columns(), ["name", "age"])

    def test_columns_with_empty_data(self):
        ds = DataSource(name="Empty Data", data=[])
        self.assertEqual(ds.columns(), [])

    def test_columns_with_none_data(self):
        ds = DataSource(name="None Data", data=None)
        self.assertEqual(ds.columns(), [])
        
    def test_empty_datasource(self):
        ds = DataSource()
        self.assertEqual(ds.columns(), [])
        self.assertEqual(ds.name, "")
        
    def test_source_states(self):
        ds1 = DataSource()
        ds2 = DataSource()
        ds1.data.append({"name": "Declan", "age": 28})
        self.assertEqual(ds2.columns(), [])
        
if __name__ == '__main__':
    unittest.main()