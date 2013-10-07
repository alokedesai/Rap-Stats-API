
from flask import (
    Flask
)
import requests
import json

app = Flask(__name__)
#base url for queries
baseUrl = "http://rapstats.herokuapp.com/articles/ngram_calculator?utf8=%E2%9C%93&q="
headers = {"X-Requested-With":"XMLHttpRequest"}


#basic return statement for homepage now--this needs to be fixed in the future
@app.route("/")
def index():
	return "Please query through the url"

#rounting for any questy
@app.route("/<query>")
def searchData(query):
	newQuery = query.split("-")

	url = baseUrl

	#add items to url
	for items in newQuery:
		url = url + items + "%2C+"

	#convert to json
	data =  json.loads(requests.get(url,headers=headers).text)

	year = []
	info = []

	#clean the data up and put it into a more friendly dictionary
	for years in data["years"]:
		year.append(years)
	newData = {}
	for key in data["terms"].keys():
		theDataList = data["terms"][key]
		newData[key] = []
		for i in theDataList:
			newData[key].append({"year" : year[theDataList.index(i)], "value" : i*100})

	

	#convert back to json
	return json.dumps(newData)
	









if __name__ == '__main__':
    app.run(debug=True)