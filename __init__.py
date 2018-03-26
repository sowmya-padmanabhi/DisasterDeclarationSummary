from flask import Flask, jsonify
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from CheckrProject import model
from CheckrProject.model import DDSummary
from flask import jsonify

@app.route('/summary', methods=['GET'])
def get_summary():
	incidents = DDSummary.query.all()
	result = []
	for incident in incidents:
		tmp_res = {}
		tmp_res['id'] = incident.id
		tmp_res['disaster_number'] = incident.disaster_number
		tmp_res['ih_program_declared'] = incident.ih_program_declared
		tmp_res['ia_program_declared'] = incident.ia_program_declared
		tmp_res['pa_program_declared'] = incident.pa_program_declared
		tmp_res['hm_program_declared'] = incident.hm_program_declared
		tmp_res['states'] = incident.states
		tmp_res['declaration_date'] = incident.declaration_date
		tmp_res['fy_declared'] = incident.fy_declared
		tmp_res['disaster_type'] = incident.disaster_type
		tmp_res['incident_type'] = incident.incident_type
		tmp_res['incident_begin_date'] = incident.incident_begin_date
		tmp_res['incident_end_date'] = incident.incident_end_date
		tmp_res['incident_begin_date'] = incident.incident_begin_date
		tmp_res['disaster_close_out_date'] = incident.disaster_close_out_date
		tmp_res['declared_country_area'] = incident.declared_country_area
		tmp_res['disaster_close_out_date'] = incident.disaster_close_out_date
		tmp_res['place_code'] = incident.place_code
		tmp_res['hash_'] = incident.hash_
		tmp_res['last_refresh'] = incident.last_refresh	
		#result.append({'states':incident.states})
		#result.append({'disaster_number':incident.disaster_number,'ih_program_declared':incident.ih_program_declared,'ia_program_declared':incident.ia_program_declared,'pa_program_declared':incident.pa_program_declared,'hm_program_declared':incident.hm_program_declared,'states':incident.states,'declaration_date':incident.declaration_date,'fy_declared':incident.fy_declared,'disaster_type':incident.disaster_type,'incident_type':incident.incident_type,'incident_begin_date':incident.incident_begin_date,'incident_end_date':incident.incident_end_date,'disaster_close_out_date':incident.disaster_close_out_date,'declared_country_area':incident.declared_country_area,'place_code':incident.place_code,'hash_':incident.hash_,'last_refresh':incident.last_refresh})
	 
	return jsonify({ 'summary': tmp_res })

