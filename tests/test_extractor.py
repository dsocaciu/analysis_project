import unittest
from unittest.mock import patch
from analysis_project.extractor import SFTPDataExtractor, HTTPDataExtractor  

class TestDataExtractors(unittest.TestCase):
    # def test_sftp_data_extraction(self):
    #     sftp_extractor = SFTPDataExtractor("sftp.example.com", "your_username", "your_password", "/path/to/file.txt")
        
    #     with patch('paramiko.Transport') as mock_transport:
    #         mock_file = mock_transport.return_value.__enter__.return_value.file.return_value
    #         mock_file.read.return_value = b"Mock SFTP Data"
    #         sftp_data = sftp_extractor.extract_data()

    #     self.assertEqual(sftp_data, b"Mock SFTP Data")

    def test_http_data_extraction(self):
        http_extractor = HTTPDataExtractor("http://www.example.com")

        with patch('requests.get') as mock_get:
            mock_get.return_value.text = "Mock HTTP Data"
            http_data = http_extractor.extract_data()

        self.assertEqual(http_data, "Mock HTTP Data")


if __name__ == '__main__':
    unittest.main()
