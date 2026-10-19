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
        
    def test_is_empty_with_data(self):
        data = [
            {"name": "Declan", "age": 30},
            {"name": "Joe", "age": 25}
        ]
        ds = DataSource(name="Test Data", data=data)
        self.assertFalse(ds.is_empty())
        
    def test_is_empty_with_empty_data(self):
        ds = DataSource(name="Empty Data", data=[])
        self.assertTrue(ds.is_empty())
        
    def test_is_compatible_with_compatible_columns(self):
        data1 = [
            {"name": "Declan", "age": 30},
            {"name": "Joe", "age": 25}
        ]
        data2 = [
            {"name": "name1", "age": 28},
            {"name": "name2", "age": 32}
        ]
        ds1 = DataSource(name="Data Source 1", data=data1)
        ds2 = DataSource(name="Data Source 2", data=data2)
        self.assertTrue(ds1.is_compatible(ds2))
        
    def test_is_compatible_with_wrong_columns(self):
        data1 = [
            {"name": "Declan", "age": 30},
            {"name": "Joe", "age": 25}
        ]
        data2 = [
            {"name": "name1", "height": 170},
            {"name": "name2", "height": 180}
        ]
        ds1 = DataSource(name="Data Source 1", data=data1)
        ds2 = DataSource(name="Data Source 2", data=data2)
        self.assertFalse(ds1.is_compatible(ds2))
        
    def test_is_compatible_with_empty_datasource(self):
        data1 = [
            {"name": "Declan", "age": 30},
            {"name": "Joe", "age": 25}
        ]
        ds1 = DataSource(name="Data Source 1", data=data1)
        ds2 = DataSource(name="Empty Data Source", data=[])
        self.assertTrue(ds1.is_compatible(ds2))
        
    def test_append_data_with_compatible_data(self):
        data1 = [
            {"name": "Declan", "age": 30},
            {"name": "Joe", "age": 25}
        ]
        data2 = [
            {"name": "name1", "age": 28},
            {"name": "name2", "age": 32}
        ]
        ds1 = DataSource(name="Data Source 1", data=data1)
        ds1.append_data(data2)
        self.assertEqual(len(ds1.data), 4)
        
    def test_append_data_with_incompatible_data(self):
        data1 = [
            {"name": "Declan", "age": 30},
            {"name": "Joe", "age": 25}
        ]
        data2 = [
            {"name": "name1", "height": 170},
            {"name": "name2", "height": 180}
        ]
        ds1 = DataSource(name="Data Source 1", data=data1)
        with self.assertRaises(ValueError):
            ds1.append_data(data2)
            
    def test_append_data_with_empty_datasource(self):
        data1 = [
            {"name": "Declan", "age": 30},
            {"name": "Joe", "age": 25}
        ]
        ds1 = DataSource(name="Empty Data Source", data=[])
        ds1.append_data(data1)
        self.assertEqual(len(ds1.data), 2)

if __name__ == '__main__':
    unittest.main()