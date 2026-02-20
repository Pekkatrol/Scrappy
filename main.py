from scraper.scraper import get_page
from scraper.parser import parse_product
from scraper.exporter import export_to_csv
from scraper.helper import print_help
from sys import argv

def main():
    if (len(argv) == 2 and argv[1] == "-h"):
        print_help()
        quit(0)
    if (len(argv) != 3):
        print_help()
        quit(84)
    URL = argv[1]
    OUTPUT_NAME = argv[2]


if __name__ == "__main__":
    main()