Rap-Stats-API
=============

Rap Stats API allows you to make simply queries to [Rap Stats](http://www.rapgenius.com/rapstats).  

Python Example
--------------

1. Import a libarry which will get the data for you.
    `import urllib2`
2. Grab the data and store it in a variable.
	`request = urllib2.urlopen('http://rap-stats-api.herokuapp.com/east+coast-west+coast')`
3.	The request is stored in JSON, but Python can convert it into a normal dictionary

		
		import json
        data = json.load(request) 
	    for terms in data:
		    print terms["value"] + ":" + terms["year"]

#### Multiple Terms
To query for multiple terms, separate terms with a dash ("-") as in:

`request = urllib2.urlopen('http://rap-stats-api.herokuapp.com/rapgenius-google')`

#### Multiple Words
If a query has more than one word, separate each word with a plus ("+") as in:

`request = urllib2.urlopen('http://rap-stats-api.herokuapp.com/east+coast-west+coast')`

#### Combine Multiple Tags
If you want to combine multiple lyircs into one data point use the ampersand ("&"):

`request = urllib2.urlopen('http://rap-stats-api.herokuapp.com/rapgenius&rap+genius-worldstarhiphop&world+star+hiphop')`

Note requests cannot contain more than 3 words!
