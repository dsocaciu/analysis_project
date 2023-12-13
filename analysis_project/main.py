from extractor import HTTPDataExtractor

def main():

    linkedin  = HTTPDataExtractor(source_url="https://www.linkedin.com/jobs/search/?currentJobId=3747037030&geoId=102571732&keywords=Senior%20Data%20Engineer&location=New%20York%2C%20New%20York%2C%20United%20States&refresh=true")

    print(linkedin.extract_data())

if __name__ == '__main__':
    main()