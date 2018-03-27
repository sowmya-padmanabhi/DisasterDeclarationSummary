import csv
from CheckrProject.model import DDSummary
from CheckrProject import db
import dateutil.parser

with open('DisasterDeclarationsSummaries.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)

	for row in csv_reader:
		d = DDSummary()
		d.disaster_number = row['disasterNumber']
		d.ih_program_declared = row['ihProgramDeclared']
		d.ia_program_declared = row['iaProgramDeclared']
		d.pa_program_declared = row['paProgramDeclared']
		d.hm_program_declared = row['hmProgramDeclared']
		d.states = row['state']
		if row['declarationDate']:
			d.declaration_date = dateutil.parser.parse(row['declarationDate'])
		d.fy_declared = dateutil.parser.parse(row['fyDeclared'])
		d.disaster_type = row['disasterType']
		d.incident_type = row['incidentType']
		d.title = row['title']
		if row['incidentBeginDate']:
			d.incident_begin_date = dateutil.parser.parse(row['incidentBeginDate'])
		if row['incidentEndDate']:		
			d.incident_end_date = dateutil.parser.parse(row['incidentEndDate'])
		if row['disasterCloseOutDate']:		
			d.disaster_close_out_date = dateutil.parser.parse(row['disasterCloseOutDate'])
		if row['declaredCountyArea']:
			d.declaredCountryArea = row['declaredCountyArea']
		if row['placeCode']:
			d.place_code = row['placeCode']
		d.hash_ = row['hash']
		d.last_refresh = row['lastRefresh']
		db.session.add(d)
	db.session.commit()		
