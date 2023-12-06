from extractor import HTTPDataExtractor

def main():

    linkedin  = HTTPDataExtractor(source_url="https://www.linkedin.com/jobs/search/?f_C=1441%2C17876832%2C791962%2C2374003%2C18950635%2C16140%2C10440912&geoId=92000000")

    print(linkedin.extract_data())

if __name__ == '__main__':
    main()