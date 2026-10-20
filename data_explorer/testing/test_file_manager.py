import unittest
from data_explorer.data.file_manager import FileManager
from data_explorer.exceptions import EmptyFileError, InvalidFilePathError

class TestFileManager(unittest.TestCase):
    fm = FileManager()
    
    def test_read_csv_with_valid_file(self):
        data = self.fm.read_csv('data_explorer/test_data/valid_data.csv')
        print(len(data))
        self.assertEqual(len(data), 3)
        self.assertEqual(data[0]['Name'], 'Declan')
        self.assertEqual(data[1]['Name'], 'Jane')
        self.assertEqual(data[2]['Name'], 'John')
        
        
    def test_read_csv_with_duplicate_headers(self):
        data = self.fm.read_csv('data_explorer/test_data/duplicate_headers.csv')
        ## first header has john at 40, second age header has 35. last header should be used so 35 expected
        self.assertEqual(data[2]['Age'], '35')
        
    def test_read_csv_with_empty_file(self):
        with self.assertRaises(EmptyFileError):
            data = self.fm.read_csv('data_explorer/test_data/empty_file.csv')
        
    def test_read_csv_with_missing_values(self):
        data = self.fm.read_csv('data_explorer/test_data/missing_values.csv')
        self.assertEqual(data[0]['Age'], '')
        
    def test_read_csv_with_headers_only(self):
        data = self.fm.read_csv('data_explorer/test_data/headers_only.csv')
        self.assertEqual(data, [])
        
    def test_read_csv_with_extra_values(self):
        data = self.fm.read_csv('data_explorer/test_data/extra_values.csv')
        self.assertEqual(data[0]['Name'], 'Declan')
        self.assertEqual(data[0]['Age'], '30')
        self.assertEqual(data[0]['Occupation'], 'Student')
        ##the extra value is stored with a None key in the dictionary
        self.assertEqual(data[0][None], ['value'])
        
    def test_read_csv_with_invalid_path(self):
        with self.assertRaises(InvalidFilePathError):
            data = self.fm.read_csv('data_explorer/test_data/ghdgfgdf.csv')


if __name__ == '__main__':
    unittest.main()