from Compiler import db

class Generator(db.Model):
	P_ID = db.Column(db.Integer, primary_key=True)
	P_Name = db.Column(db.String(100), nullable=False)
	C_Name = db.Column(db.String(100))
	Lv = db.Column(db.Integer(), default=1)
	Align = db.Column(db.String(50))
	Gender = db.Column(db.String(50))
	Race = db.Column(db.String(50))
	Class = db.Column(db.String(50))
	STR = db.Column(db.Integer())
	DEX = db.Column(db.Integer())
	CON = db.Column(db.Integer())
	INT = db.Column(db.Integer())
	WIS = db.Column(db.Integer())
	CHA = db.Column(db.Integer())
