from get_google_results import get_google_results
from search_engines import search_engines


parameters = {"cx": search_engines["es"]["col"]}


def main():
    print(get_google_results("Obras por impuestos",parameters))

main()