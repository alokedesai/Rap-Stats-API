Rap-Stats-API
=============

Rap Stats API allows you to make simply queries to [Rap Stats](http://www.rapgenius.com/rapstats) through a simple flask web [application](http://rap-stats-api.herokuapp.com/).  

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
	    	print term
	    	for values in data[terms]:
		    	print str(values["year"]) + ":" + str(values["terms"])

#### Ouput
The output is in JSON format, with each term being an array of a certain "year", "value" pair. **Note the value is in percentage format.
** Here's an example, with the query being east coast, west coast: ['http://rap-stats-api.herokuapp.com/east+coast-west+coast']('http://rap-stats-api.herokuapp.com/east+coast-west+coast')
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
