from search_engines import search_engines
import csv
import requests
from key import key
from simple_term_menu import TerminalMenu

parameters = {"cx": search_engines["es"]["col"]}

keywords = {}

with open("workspace/github.com/jabuta/rank-tracker/files/keywords.csv",) as csvkeywords:
    kwdsdata = list(csv.reader(csvkeywords))[1:]
    for kwd in kwdsdata:
        keywords[kwd[0]] = {'locale': kwd[1]}
print(*keywords.keys(), sep="\n")


def add_keywords():
    print("Input the Keywords you want to track, press enter to enter a new keyword, press enter on empty to finish")
    while True:
        new_keyword = input()
        if new_keyword == "":
            break
        options = ["es-co", "en-us"]
        terminal_menu = TerminalMenu(options)
        locale = terminal_menu.show()
        keywords[new_keyword] = {'locale': locale}



def get_google_results(query,parameters):
    parameters["key"] = key
    parameters["q"] = query
    
    api_url = "https://www.googleapis.com/customsearch/v1?"

    try:
        x = requests.get(api_url,parameters)

        x = x.json()

        resultlist = []
        for item in x["items"]:
            resultlist.append(item["link"])

        return resultlist
    except Exception as err:
        print(err)
        raise



def main():
    options = ["add keywords", "entry 2", "entry 3"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    print(f"You have selected {options[menu_entry_index]}!")

    if options[menu_entry_index] == "add keywords":
        add_keywords()

if __name__ == "__main__":
    main()
    