Rap-Stats-API
=============

Rap Stats API allows you to make simply queries to [Rap Stats](http://www.rapgenius.com/rapstats).  

Python Example
--------------

1. Import a libarry which will get the data for you.
    `import urllib2`
2. Grab the data and store it in a variable.
	`request = urllib2.urlopen('http://course-api.herokuapp.com/lit')`
3.	The request is stored in JSON, but Python can convert it into a normal dictionary
	```python
	import json
    data = json.load(request) 
	for terms in data:
		print terms["value"] + ":" + terms["year"]
	```
