import requests
from search_engines import search_engines
from key import key



q = "Que son las obras por impuestos colombia"
parameters = {"key": key, "cx": search_engines["es"]["col"],"q": q}



x = requests.get(api_url,parameters)

x = x.json()

resultlist = []
for item in x["items"]:
    resultlist.append(item["link"])

print(resultlist)


def get_results(q,search_engines):
    api_url = "https://www.googleapis.com/customsearch/v1?"