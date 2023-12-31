import requests
from key import key



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