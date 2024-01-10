from get_google_results import get_google_results
from search_engines import search_engines
import csv

parameters = {"cx": search_engines["es"]["col"]}

keywords = {}

with open("workspace/github.com/jabuta/rank-tracker/files/keywords.csv",) as csvkeywords:
    kwdsdata = list(csv.reader(csvkeywords))
    for kwd in kwdsdata:
        keywords[kwd[0]] = kwd[1:]
print(keywords)



def main():
    print(get_google_results("Obras por impuestos",parameters))

# main()