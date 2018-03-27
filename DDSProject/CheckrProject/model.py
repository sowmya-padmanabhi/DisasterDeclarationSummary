from CheckrProject import db
from datetime import datetime

class DDSummary(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	disaster_number = db.Column(db.String(10))
	ih_program_declared = db.Column(db.String(10))
	ia_program_declared = db.Column(db.Integer)
	pa_program_declared = db.Column(db.Integer, index=True)
	hm_program_declared = db.Column(db.Integer, index=True)
	states = db.Column(db.String(10), index=True)
	declaration_date = db.Column(db.DateTime, index=True)
	fy_declared = db.Column(db.Integer, index=True)
	disaster_type = db.Column(db.String(10), index=True)
	incident_type = db.Column(db.String(10), index=True)
	title = db.Column(db.String(10), index=True)
	incident_begin_date = db.Column(db.DateTime, index=True)
	incident_end_date = db.Column(db.DateTime, index=True)
	disaster_close_out_date = db.Column(db.DateTime, index=True)
	declared_country_area = db.Column(db.String(10), index=True)
	place_code = db.Column(db.String(10), index=True)
	hash_ = db.Column(db.Integer, index=True)
	last_refresh = db.Column(db.String(20), index=True)
		

	def __repr__(self):
		return '<DDSummary {}>'.format(disasterNumber)
