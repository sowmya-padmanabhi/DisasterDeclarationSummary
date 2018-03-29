import requests
import simplejson as json 

url = 'http://127.0.0.1:5000/api/summary'

states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA","HI", "ID", "IL", "IN", "IA", 
	  "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
      "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

for st in states:
	result = requests.get(url + '?q={"filters":[{"name":"states","op":"eq","val":"' + st + '"}]}')
	result.content
	obj = json.loads(result.content)
	res = obj['num_results']
	print ({st 	: res})
