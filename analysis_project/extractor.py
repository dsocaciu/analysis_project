import requests
import paramiko

class Extractor:
    def __init__(self, source_url, type, username=None, password=None):
        self.source_url = source_url
        self.type = type
        self.username = username
        self.password = password

    def extract_data(self):
        raise NotImplementedError("Subclasses must implement the extract_data method")

class SFTPDataExtractor(Extractor):
    def __init__(self, source_url, username, password, remote_path):
        super().__init__(source_url, username, password, type="SFTP")
        self.remote_path = remote_path

    def extract_data(self):
        # Implement SFTP data extraction logic
        with paramiko.Transport((self.source_url, 22)) as transport:
            transport.connect(username=self.username, password=self.password)
            sftp = paramiko.SFTPClient.from_transport(transport)
            with sftp.file(self.remote_path) as file:
                data = file.read()
        return data

class HTTPDataExtractor(Extractor):
    def __init__(self,source_url):
        super().__init__(source_url,type="HTTP")

    def extract_data(self):
        # Implement HTTP data extraction logic
        response = requests.get(self.source_url)
        data = response.text
        return data

