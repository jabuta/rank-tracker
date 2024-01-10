from search_engines import search_engines
import csv
import requests
from key import key

parameters = {"cx": search_engines["es"]["col"]}

keywords = {}

with open("workspace/github.com/jabuta/rank-tracker/files/keywords.csv",) as csvkeywords:
    kwdsdata = list(csv.reader(csvkeywords))
    for kwd in kwdsdata:
        keywords[kwd[0]] = kwd[1:]
print(keywords)



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
    print(get_google_results("Obras por impuestos",parameters))

# main()