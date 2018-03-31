## Technologies used
```
Web Framework: Flask
Programming Language: Python 2.7.14
Database: SQLite3
Object Relational Mapper (ORM): SQLAlchemy
Cloud Platform: Heroku
```
## URL where application can be accessed
```
https://ancient-mountain-18284.herokuapp.com/api/summary
```
## Dependencies needed to be installed for running the application locally
```
All the dependencies are in requirements.txt and can be installed using "pip install -r requirements.txt"
```

## Description

```
- Checkr_Project : Main project directory. Consists of all the files needed.
- In app.py file, write code for class Summary which has all the columns in it.
- Summary(): Class to display data from the database.
- Script read_data_from_csv.py: the script reads each row of data and adds the data to the database.
- Script read_data_from_server.py: reads data from the server using the endpoint "/api/summary"and performs filtering 	 by disaster number across all the states for all time periods.
```
## Steps for Heroku
```
$ heroku login
$ git init
$ git add .
$ git commit -m 'first'
$ heroku create
$ git push heroku master
```

## To view application

<b>Output: Visualization on the map</b> (based on number of disasters for every state. Darker the shade, higher the number of disaster in that state)
```
https://ancient-mountain-18284.herokuapp.com/api/map
```
<b>Output with filter: </b><br />
Output for filtering of data by types of disaster.
```
Disaster type = DR:
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"disaster_type", "op":"eq","val":"DR"}]}

Disaster type = EM.
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"disaster_type", "op":"eq","val":"EM"}]}
```
Output: Filtering out by date<br />
<b>Incident begin date = 1953-05-02T00:00:00.000Z.</b>
```
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"incident_begin_date", "op":"eq","val":"1953-05-02T00:00:00.000Z"}]}
```

-The value for 'name' can be changed to <b>Delcaration date</b>, <b>Incident end date</b> or <b>Disaster close out  date</b>, based on the requirement and they should be given their respective 'val' values.  <br />
-Similarly, the value of 'op' can be changed to 'lt' and 'gt' and between two dates based on the requirement.

Filtering of date by <b>Incident begin date greater than 1953-05-02T00:00:00.000Z.</b> 
```
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"incident_begin_date", "op":"gt","val":"1953-05-02T00:00:00.000Z"}]}
```

Filtering of date by <b>Incident begin date lesser than 1953-05-02T00:00:00.000Z.</b>
```
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"incident_begin_date","op":"lt","val":"1954-10-07T00:00:00.000Z"}]}
```

Filtering of date by <b>Incident begin date between 1953-05-02T00:00:00.000Z and 1954-10-07T00:00:00.000Z.</b>
```
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"incident_begin_date", "op":"gt","val":"1953-05-02T00:00:00.000Z"},{"name":"incident_begin_date", "op":"lt","val":"1954-10-07T00:00:00.000Z"}]} 
```

### Build filtering by Date and type of disaster

For filtering of data by types of disaster.
Sample output for filtering by Disaster type = DR.
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"disaster_type", "op":"eq","val":"DR"}]}

```
{
  "num_results": 12115, 
  "objects": [
    {
      "declaration_date": "1974-08-29T00:00:00", 
      "declared_country_area": null, 
      "disaster_close_out_date": "1976-12-01T00:00:00", 
      "disaster_number": "3002", 
      "disaster_type": "EM", 
      "fy_declared": "1974-03-29 00:00:00", 
      "hash_": "b147b14e1cdef44a8366a8bf00842c8c", 
      "hm_program_declared": 0, 
      "ia_program_declared": 0, 
      "id": 30322, 
      "ih_program_declared": "0", 
      "incident_begin_date": "1974-08-29T00:00:00", 
      "incident_end_date": "1974-08-29T00:00:00", 
      "incident_type": "Drought", 
      "last_refresh": "2018-02-09T14:39:45.377Z", 
      "pa_program_declared": 1, 
      "place_code": "99031", 
      "states": "PR", 
      "title": "IMPACT OF DROUGHT"
    }, 
    {
      "declaration_date": "1975-01-18T00:00:00", 
      "declared_country_area": null, 
      "disaster_close_out_date": "1975-03-14T00:00:00", 
      "disaster_number": "3007", 
      "disaster_type": "EM", 
      "fy_declared": "1975-03-29 00:00:00", 
      "hash_": "14133eefa013f8882268704795359bae", 
      "hm_program_declared": 0, 
      "ia_program_declared": 1, 
      "id": 30324, 
      "ih_program_declared": "0", 
      "incident_begin_date": "1975-01-18T00:00:00", 
      "incident_end_date": "1975-01-18T00:00:00", 
      "incident_type": "Tornado", 
      "last_refresh": "2018-02-09T14:39:45.553Z", 
      "pa_program_declared": 1, 
      "place_code": "99081", 
      "states": "AL", 
      "title": "TORNADOES"
    }, 
	
```

Sample output for filtering by Disaster type = EM.
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"disaster_type", "op":"eq","val":"EM"}]}

```
{
  "num_results": 12115, 
  "objects": [
    {
      "declaration_date": "1974-08-29T00:00:00", 
      "declared_country_area": null, 
      "disaster_close_out_date": "1976-12-01T00:00:00", 
      "disaster_number": "3002", 
      "disaster_type": "EM", 
      "fy_declared": "1974-03-29 00:00:00", 
      "hash_": "b147b14e1cdef44a8366a8bf00842c8c", 
      "hm_program_declared": 0, 
      "ia_program_declared": 0, 
      "id": 30322, 
      "ih_program_declared": "0", 
      "incident_begin_date": "1974-08-29T00:00:00", 
      "incident_end_date": "1974-08-29T00:00:00", 
      "incident_type": "Drought", 
      "last_refresh": "2018-02-09T14:39:45.377Z", 
      "pa_program_declared": 1, 
      "place_code": "99031", 
      "states": "PR", 
      "title": "IMPACT OF DROUGHT"
    }, 
    {
      "declaration_date": "1975-01-18T00:00:00", 
      "declared_country_area": null, 
      "disaster_close_out_date": "1975-03-14T00:00:00", 
      "disaster_number": "3007", 
      "disaster_type": "EM", 
      "fy_declared": "1975-03-29 00:00:00", 
      "hash_": "14133eefa013f8882268704795359bae", 
      "hm_program_declared": 0, 
      "ia_program_declared": 1, 
      "id": 30324, 
      "ih_program_declared": "0", 
      "incident_begin_date": "1975-01-18T00:00:00", 
      "incident_end_date": "1975-01-18T00:00:00", 
      "incident_type": "Tornado", 
      "last_refresh": "2018-02-09T14:39:45.553Z", 
      "pa_program_declared": 1, 
      "place_code": "99081", 
      "states": "AL", 
      "title": "TORNADOES"
    }, 

```
For filtering of data by date.
Sample output for the filtering of date by Incident begin date = 953-05-02T00:00:00.000Z.
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"incident_begin_date", "op":"eq","val":"1953-05-02T00:00:00.000Z"}]}

```
{
  "num_results": 1, 
  "objects": [
    {
      "declaration_date": "1953-05-02T00:00:00", 
      "declared_country_area": null, 
      "disaster_close_out_date": "1954-06-01T00:00:00", 
      "disaster_number": "1", 
      "disaster_type": "DR", 
      "fy_declared": "1953-03-29 00:00:00", 
      "hash_": "e6f77c3a97c63d478bf14c9a58f60a0d", 
      "hm_program_declared": 1, 
      "ia_program_declared": 1, 
      "id": 1, 
      "ih_program_declared": "0", 
      "incident_begin_date": "1953-05-02T00:00:00", 
      "incident_end_date": "1953-05-02T00:00:00", 
      "incident_type": "Tornado", 
      "last_refresh": "2018-02-09T14:38:26.149Z", 
      "pa_program_declared": 1, 
      "place_code": null, 
      "states": "GA", 
      "title": "TORNADO"
    }
  ], 
  "page": 1, 
  "total_pages": 1
}

```

Sample output for the filtering of date by Incident begin date greater than 953-05-02T00:00:00.000Z. 
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"incident_begin_date", "op":"gt","val":"1953-05-02T00:00:00.000Z"}]}

```
{
  "num_results": 48063, 
  "objects": [
    {
      "declaration_date": "1954-06-23T00:00:00", 
      "declared_country_area": null, 
      "disaster_close_out_date": "1956-02-01T00:00:00", 
      "disaster_number": "17", 
      "disaster_type": "DR", 
      "fy_declared": "1954-03-29 00:00:00", 
      "hash_": "b0afe5b02eccaa5c8eed1d3f354b0f2b", 
      "hm_program_declared": 1, 
      "ia_program_declared": 1, 
      "id": 2, 
      "ih_program_declared": "0", 
      "incident_begin_date": "1954-06-23T00:00:00", 
      "incident_end_date": "1954-06-23T00:00:00", 
      "incident_type": "Flood", 
      "last_refresh": "2018-02-09T14:38:26.191Z", 
      "pa_program_declared": 1, 
      "place_code": null, 
      "states": "IA", 
      "title": "FLOOD"
    }, 
    {
      "declaration_date": "1953-05-29T00:00:00", 
      "declared_country_area": null, 
      "disaster_close_out_date": "1960-02-01T00:00:00", 
      "disaster_number": "3", 
      "disaster_type": "DR", 
      "fy_declared": "1953-03-29 00:00:00", 
      "hash_": "a6dd526e79d7292ae21a7f9430422931", 
      "hm_program_declared": 1, 
      "ia_program_declared": 1, 
      "id": 3, 
      "ih_program_declared": "0", 
      "incident_begin_date": "1953-05-29T00:00:00", 
      "incident_end_date": "1953-05-29T00:00:00", 
      "incident_type": "Flood", 
      "last_refresh": "2018-02-09T14:38:26.144Z", 
      "pa_program_declared": 1, 
      "place_code": null, 
      "states": "LA", 
      "title": "FLOOD"
    }, 
```

Sample output for the filtering of date by Incident begin date lesser than 953-05-02T00:00:00.000Z.
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"incident_begin_date","op":"lt","val":"1954-10-07T00:00:00.000Z"}]}

```
{
  "num_results": 24, 
  "objects": [
    {
      "declaration_date": "1953-05-02T00:00:00", 
      "declared_country_area": null, 
      "disaster_close_out_date": "1954-06-01T00:00:00", 
      "disaster_number": "1", 
      "disaster_type": "DR", 
      "fy_declared": "1953-03-29 00:00:00", 
      "hash_": "e6f77c3a97c63d478bf14c9a58f60a0d", 
      "hm_program_declared": 1, 
      "ia_program_declared": 1, 
      "id": 1, 
      "ih_program_declared": "0", 
      "incident_begin_date": "1953-05-02T00:00:00", 
      "incident_end_date": "1953-05-02T00:00:00", 
      "incident_type": "Tornado", 
      "last_refresh": "2018-02-09T14:38:26.149Z", 
      "pa_program_declared": 1, 
      "place_code": null, 
      "states": "GA", 
      "title": "TORNADO"
    }, 
    {
      "declaration_date": "1954-06-23T00:00:00", 
      "declared_country_area": null, 
      "disaster_close_out_date": "1956-02-01T00:00:00", 
      "disaster_number": "17", 
      "disaster_type": "DR", 
      "fy_declared": "1954-03-29 00:00:00", 
      "hash_": "b0afe5b02eccaa5c8eed1d3f354b0f2b", 
      "hm_program_declared": 1, 
      "ia_program_declared": 1, 
      "id": 2, 
      "ih_program_declared": "0", 
      "incident_begin_date": "1954-06-23T00:00:00", 
      "incident_end_date": "1954-06-23T00:00:00", 
      "incident_type": "Flood", 
      "last_refresh": "2018-02-09T14:38:26.191Z", 
      "pa_program_declared": 1, 
      "place_code": null, 
      "states": "IA", 
      "title": "FLOOD"
    }, 

```
Sample output for the filtering of date by Incident begin date between 1953-05-02T00:00:00.000Z and 1954-10-07T00:00:00.000Z.
https://ancient-mountain-18284.herokuapp.com/api/summary?q={"filters":[{"name":"incident_begin_date", "op":"gt","val":"1953-05-02T00:00:00.000Z"},{"name":"incident_begin_date", "op":"lt","val":"1954-10-07T00:00:00.000Z"}]} 


```
{
  "num_results": 23, 
  "objects": [
    {
      "declaration_date": "1954-06-23T00:00:00", 
      "declared_country_area": null, 
      "disaster_close_out_date": "1956-02-01T00:00:00", 
      "disaster_number": "17", 
      "disaster_type": "DR", 
      "fy_declared": "1954-03-29 00:00:00", 
      "hash_": "b0afe5b02eccaa5c8eed1d3f354b0f2b", 
      "hm_program_declared": 1, 
      "ia_program_declared": 1, 
      "id": 2, 
      "ih_program_declared": "0", 
      "incident_begin_date": "1954-06-23T00:00:00", 
      "incident_end_date": "1954-06-23T00:00:00", 
      "incident_type": "Flood", 
      "last_refresh": "2018-02-09T14:38:26.191Z", 
      "pa_program_declared": 1, 
      "place_code": null, 
      "states": "IA", 
      "title": "FLOOD"
    }, 
    {
      "declaration_date": "1953-05-29T00:00:00", 
      "declared_country_area": null, 
      "disaster_close_out_date": "1960-02-01T00:00:00", 
      "disaster_number": "3", 
      "disaster_type": "DR", 
      "fy_declared": "1953-03-29 00:00:00", 
      "hash_": "a6dd526e79d7292ae21a7f9430422931", 
      "hm_program_declared": 1, 
      "ia_program_declared": 1, 
      "id": 3, 
      "ih_program_declared": "0", 
      "incident_begin_date": "1953-05-29T00:00:00", 
      "incident_end_date": "1953-05-29T00:00:00", 
      "incident_type": "Flood", 
      "last_refresh": "2018-02-09T14:38:26.144Z", 
      "pa_program_declared": 1, 
      "place_code": null, 
      "states": "LA", 
      "title": "FLOOD"
    }, 

```

### Output of read_data_from_server.py
~/DDSProject/CheckrProject$ ipython read_data_from_server.py
Returning the number of disasters for each state.
```
{'AL': 1323}
{'AK': 158}
{'AZ': 220}
{'AR': 1314}
{'CA': 1187}
{'CO': 491}
{'CT': 193}
{'DC': 20}
{'DE': 44}
{'FL': 1658}
{'GA': 1730}
{'HI': 64}
{'ID': 249}
{'IL': 1036}
{'IN': 1235}
{'IA': 1480}
{'KS': 1324}
{'KY': 2031}
{'LA': 1444}
{'ME': 384}
{'MD': 393}
{'MA': 347}
{'MI': 593}
{'MN': 1190}
{'MS': 1298}
{'MO': 2318}
{'MT': 412}
{'NE': 1085}
{'NV': 161}
{'NH': 259}
{'NJ': 517}
{'NM': 342}
{'NY': 1259}
{'NC': 1316}
{'ND': 1123}
{'OH': 1050}
{'OK': 1938}
{'OR': 386}
{'PA': 1081}
{'RI': 89}
{'SC': 615}
{'SD': 963}
{'TN': 1228}
{'TX': 3897}
{'UT': 156}
{'VT': 267}
{'VA': 1982}
{'WA': 718}
{'WV': 1075}
{'WI': 681}
{'WY': 75}
```








