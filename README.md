## Technologies used

Flask, Python, SQLAlchemy

## Description

```
- DDSProject: Main project directory. Consists of CheckrProject directory, read_data_from_csv.py' and 'DisasterDeclarationsSummary.csv' files.
- CheckrProject: Sub directory
- Add all the needed files to the main project directory and sub directory.
- In model.py file, write code for class Summary which has all the columns in it.
- Summary(): Function to dispplay data from the database.
- Google how to read CSV using a python script
- Script read_data_from_csv.py: the server reads each row of data and adds the data to the database.
- Script read_data_from_server.py: reads data from the server and performs filtering by disaster number across all the states for all time periods.

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

### Build filtering by Date and type of disaster

For filtering of data by types of disaster.
Sample output for filtering by DisasterType DR.
http://127.0.0.1:5000/api/summary?q={"filters":[{"name":"disaster_type", "op":"eq","val":"DR"}]}

```
num_results	34618
objects	
0:	
	declaration_date	"1953-05-02T00:00:00"
	declared_country_area	null
	disaster_close_out_date	"1954-06-01T00:00:00"
	disaster_number	"1"
	disaster_type	"DR"
	fy_declared	"1953-03-26 00:00:00"
	hash_	"e6f77c3a97c63d478bf14c9a58f60a0d"
	hm_program_declared	1
	ia_program_declared	1
	id	1
	ih_program_declared	"0"
	incident_begin_date	"1953-05-02T00:00:00"
	incident_end_date	"1953-05-02T00:00:00"
	incident_type	"Tornado"
	last_refresh	"2018-02-09T14:38:26.149Z"
	pa_program_declared	1
	place_code	null
	states	"GA"
	title	"TORNADO"
1:	
	declaration_date	"1954-06-23T00:00:00"
	declared_country_area	null
	disaster_close_out_date	"1956-02-01T00:00:00"
	disaster_number	"17"
	disaster_type	"DR"
	fy_declared	"1954-03-26 00:00:00"
	hash_	"b0afe5b02eccaa5c8eed1d3f354b0f2b"
	hm_program_declared	1
	ia_program_declared	1
	id	2
	ih_program_declared	"0"
	incident_begin_date	"1954-06-23T00:00:00"
	incident_end_date	"1954-06-23T00:00:00"
	incident_type	"Flood"
	last_refresh	"2018-02-09T14:38:26.191Z"
	pa_program_declared	1
	place_code	null
	states	"IA"
	title	"FLOOD"
	
```
The val can take different values depending on what type of disaster we want to filter out.
Sample output for filtering by DisasterType = EM.
http://127.0.0.1:5000/api/summary?q={"filters":[{"name":"disaster_type", "op":"eq","val":"EM"}]}

```
num_results	12115
objects	
0:
	declaration_date	"1974-08-29T00:00:00"
	declared_country_area	null
	disaster_close_out_date	"1976-12-01T00:00:00"
	disaster_number	"3002"
	disaster_type	"EM"
	fy_declared	"1974-03-26 00:00:00"
	hash_	"b147b14e1cdef44a8366a8bf00842c8c"
	hm_program_declared	0
	ia_program_declared	0
	id	30322
	ih_program_declared	"0"
	incident_begin_date	"1974-08-29T00:00:00"
	incident_end_date	"1974-08-29T00:00:00"
	incident_type	"Drought"
	last_refresh	"2018-02-09T14:39:45.377Z"
	pa_program_declared	1
	place_code	"99031"
	states	"PR"
	title	"IMPACT OF DROUGHT"
1:	
	declaration_date	"1975-01-18T00:00:00"
	declared_country_area	null
	disaster_close_out_date	"1975-03-14T00:00:00"
	disaster_number	"3007"
	disaster_type	"EM"
	fy_declared	"1975-03-26 00:00:00"
	hash_	"14133eefa013f8882268704795359bae"
	hm_program_declared	0
	ia_program_declared	1
	id	30324
	ih_program_declared	"0"
	incident_begin_date	"1975-01-18T00:00:00"
	incident_end_date	"1975-01-18T00:00:00"
	incident_type	"Tornado"
	last_refresh	"2018-02-09T14:39:45.553Z"
	pa_program_declared	1
	place_code	"99081"
	states	"AL"
	title	"TORNADOES"

```
For filtering of data by date.
Sample output for the filtering of date by Incident begin date=953-05-02T00:00:00.000Z.
127.0.0.1:5000/api/summary?q={"filters":[{"name":"incidentBeginDate", "op":"eq","val":"1953-05-02T00:00:00.000Z"}]}

```
num_results:	1
objects:
0:
	declaration_date	"1953-05-02T00:00:00"
	declared_country_area	null
	disaster_close_out_date	"1954-06-01T00:00:00"
	disaster_number	"1"
	disaster_type	"DR"
	fy_declared	"1953-03-26 00:00:00"
	hash_	"e6f77c3a97c63d478bf14c9a58f60a0d"
	hm_program_declared	1
	ia_program_declared	1
	id	1
	ih_program_declared	"0"
	incident_begin_date	"1953-05-02T00:00:00"
	incident_end_date	"1953-05-02T00:00:00"
	incident_type	"Tornado"
	last_refresh	"2018-02-09T14:38:26.149Z"
	pa_program_declared	1
	place_code	null
	states	"GA"
	title	"TORNADO"
	page	1
	total_pages	1

```

However, the values for name, op, val can change to other specific filtering requirement, ex disasterCloseOutDate, LT or GT and 1954-06-01T00:00:00.000Z respectively.
Sample output for the filtering of date by Incident begin date greater than 953-05-02T00:00:00.000Z. 
127.0.0.1:5000/api/summary?q={"filters":[{"name":"incidentBeginDate", "op":"gt","val":"1953-05-02T00:00:00.000Z"}]}

```
num_results:	48039
objects:
0:
	declaration_date	"1954-11-10T00:00:00"
	declared_country_area	null
	disaster_close_out_date	"1957-09-01T00:00:00"
	disaster_number	"31"
	disaster_type	"DR"
	fy_declared	"1955-03-26 00:00:00"
	hash_	"c0388e7b904ec46bec14718092965024"
	hm_program_declared	1
	ia_program_declared	1
	id	4
	ih_program_declared	"0"
	incident_begin_date	"1954-11-10T00:00:00"
	incident_end_date	"1954-11-10T00:00:00"
	incident_type	"Other"
	last_refresh	"2018-02-09T14:38:26.182Z"
	pa_program_declared	1
	place_code	null
	states	"AK"
	title	"SEVERE HARDSHIP"
1:	
	declaration_date	"1955-06-01T00:00:00"
	declared_country_area	null
	disaster_close_out_date	"1959-12-01T00:00:00"
	disaster_number	"35"
	disaster_type	"DR"
	fy_declared	"1955-03-26 00:00:00"
	hash_	"0ff7aff8743f693923b6cfd3bd7bd3f6"
	hm_program_declared	1
	ia_program_declared	1
	id	6
	ih_program_declared	"0"
	incident_begin_date	"1955-06-01T00:00:00"
	incident_end_date	"1955-06-01T00:00:00"
	incident_type	"Flood"
	last_refresh	"2018-02-09T14:38:26.292Z"
	pa_program_declared	1
	place_code	null
	states	"OK"
	title	"FLOOD & TORNADO"

```

Sample output for the filtering of date by Incident begin date lesser than 953-05-02T00:00:00.000Z.
127.0.0.1:5000/api/summary?q={"filters":[{"name":"incidentBeginDate","op":"lt","val":"1953-05-02T00:00:00.000Z"}]}

```
num_results:	24
objects:
0:
	declaration_date	"1953-05-02T00:00:00"
	declared_country_area	null
	disaster_close_out_date	"1954-06-01T00:00:00"
	disaster_number	"1"
	disaster_type	"DR"
	fy_declared	"1953-03-26 00:00:00"
	hash_	"e6f77c3a97c63d478bf14c9a58f60a0d"
	hm_program_declared	1
	ia_program_declared	1
	id	1
	ih_program_declared	"0"
	incident_begin_date	"1953-05-02T00:00:00"
	incident_end_date	"1953-05-02T00:00:00"
	incident_type	"Tornado"
	last_refresh	"2018-02-09T14:38:26.149Z"
	pa_program_declared	1
	place_code	null
	states	"GA"
	title	"TORNADO"
1:	
	declaration_date	"1954-06-23T00:00:00"
	declared_country_area	null
	disaster_close_out_date	"1956-02-01T00:00:00"
	disaster_number	"17"
	disaster_type	"DR"
	fy_declared	"1954-03-26 00:00:00"
	hash_	"b0afe5b02eccaa5c8eed1d3f354b0f2b"
	hm_program_declared	1
	ia_program_declared	1
	id	2
	ih_program_declared	"0"
	incident_begin_date	"1954-06-23T00:00:00"
	incident_end_date	"1954-06-23T00:00:00"
	incident_type	"Flood"
	last_refresh	"2018-02-09T14:38:26.191Z"
	pa_program_declared	1
	place_code	null
	states	"IA"
	title	"FLOOD"

```
Sample output for the filtering of date by Incident begin date between 1953-05-02T00:00:00.000Z and 1954-10-07T00:00:00.000Z.
"127.0.0.1:5000/api/summary?q={"filters":[{"name":"incidentBeginDate", "op":"gt","val":"1953-05-02T00:00:00.000Z"},{"name":"incidentBeginDate", "op":"lt","val":"1954-10-07T00:00:00.000Z"}]}" 

```
num_results:	23
objects:
0:
	declaration_date	"1954-06-23T00:00:00"
	declared_country_area	null
	disaster_close_out_date	"1956-02-01T00:00:00"
	disaster_number	"17"
	disaster_type	"DR"
	fy_declared	"1954-03-26 00:00:00"
	hash_	"b0afe5b02eccaa5c8eed1d3f354b0f2b"
	hm_program_declared	1
	ia_program_declared	1
	id	2
	ih_program_declared	"0"
	incident_begin_date	"1954-06-23T00:00:00"
	incident_end_date	"1954-06-23T00:00:00"
	incident_type	"Flood"
	last_refresh	"2018-02-09T14:38:26.191Z"
	pa_program_declared	1
	place_code	null
	states	"IA"
	title	"FLOOD"
1:	
	declaration_date	"1953-05-29T00:00:00"
	declared_country_area	null
	disaster_close_out_date	"1960-02-01T00:00:00"
	disaster_number	"3"
	disaster_type	"DR"
	fy_declared	"1953-03-26 00:00:00"
	hash_	"a6dd526e79d7292ae21a7f9430422931"
	hm_program_declared	1
	ia_program_declared	1
	id	3
	ih_program_declared	"0"
	incident_begin_date	"1953-05-29T00:00:00"
	incident_end_date	"1953-05-29T00:00:00"
	incident_type	"Flood"
	last_refresh	"2018-02-09T14:38:26.144Z"
	pa_program_declared	1
	place_code	null
	states	"LA"
	title	"FLOOD"

```
### Prerequisities

```
-List of packages that were needed for the project are given in the requirements.txt file.

```







