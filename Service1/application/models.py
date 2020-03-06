from application import db, login_manager
from flask_login import UserMixin
from datetime import datetime
from enum import Enum

# Enums for 5e stuff

#class size(Enum):
#	"Small" = 1
#	"Medium" = 2
#
#class speed(Enum):
#	"25 ft" = 1
#	"25/50 ft" = 2
#	"30 ft" = 3
#	"30/20C" = 4
#	"30/30S" = 5
#	"35 ft" = 6
#	"40 ft" = 7
#
#class source(Enum):
#	"PlayersHandbook" = 1
#	"DungeonMasterGuide" = 2
#	"GuildmasterRavinica" = 3
#	"ElementalEvil" = 4
#	"Mordenkainens" = 5
#	"SwordCoast" = 6
#	"VolosGuide" = 7
#	"Kaldesh" = 8		#https://media.wizards.com/2017/downloads/magic/Plane-Shift_Kaladesh.pdf
#	"Zendikar" = 9		#https://media.wizards.com/2016/downloads/magic/Plane%20Shift%20Zendikar.pdf
#	"Eberron" = 10		#https://media.wizards.com/2015/downloads/dnd/UA_Eberron_v1.pdf
#	"EladrinGith" = 11	#https://media.wizards.com/2017/dnd/downloads/UA-Eladrin-Gith.pdf
#	"Waterborne" = 12		#https://media.wizards.com/2015/downloads/dnd/UA_Waterborne_v3.pdf
#
#class school(Enum):
#	"Divination" = 1
#	"Abjuration" =2
#	"Enchantment" = 3
#	"Necromancy" = 4
#	"Illusion" = 5
#	"Conjuraction" = 6
#	"Evocation" = 7
#	"Transmutation" = 8
#
#class range(Enum):
#	"n/a" = 1
#	"Self" = 2
#	"Self +10 ft radius" = 3
#	"Self +10 ft radius hemisphere" = 4
#	"Self +10 ft radius sphere" = 5
#	"Self +100 ft line" = 6
#	"Self +15 ft cone" = 7
#	"Self +30 ft cone" = 8
#	"Self +30 ft range" = 9
#	"Self +30 ft radius" = 10
#	"Self +5 ft radius" = 11
#	"Self +5 mile radius" = 12
#	"Self +60 ft cone" = 13
#	"Self +60 ft line" = 14
#	"Sight" = 15
#	"Touch" = 16
#	"Touch with reach" = 17
#	"Special" = 18
#	"Unlimited" = 19
#	"Entire Plane" = 20
#	"5 foot" = 21
#	"10 foot" = 22
#	"15 foot" = 23
#	"30 foot" = 24
#	"30 ft line" = 25
#	"50 foot" = 26
#	"60 foot" = 27
#	"90 foot" = 28
#	"100 foot" = 29
#	"120 foot" = 30
#	"150 foot" = 31
#	"120 foot" = 32
#	"300 foot" = 33
#	"500 foot" = 34
#	"600 foot" = 35
#	"1 mile" = 36
#	"500 mile" = 37
#
#class Stats(Enum):
#	"STR" = 1
#	"DEX" = 2
#	"CON" = 3
#	"INT" = 4
#	"WIS" = 5
#	"CHA" = 6
#
# Tables for the 5e stuff
#
#class classes(db.Model)
#	CL_ID = db.Column(sb.Integer(1), primary_key=True)
#	Name =  db.Column(db.String(50), nullable=False, unique=True)
#	Primary = db.Column(sb.String(5), Nullable = False, Enum(stats))
#	Secondary = db.Column(sb.String(5), Nullable = False, Enum(stats))
#	Dump = db.Column(sb.String(5), Nullable = False, Enum(stats))
#
#class Language(db.Model):
#	L_ID = db.Column(db.Integer, primary_key=True)
#	Language = db.Column(db.String(15), nullable=False)
#	Script = db.Column(db.String(15), nullable=False)
#
#class Race(db.Model):
#	R_ID = db.Column(db.Integer, primary_key=True)
#	Fullname = db.Column(db.String(50), nullable=False)
#	size = db.Column(db.String(10), nullable=False, Enum(size))
#	speed = db.Column(db.string(10), nullable=False, Enum(speed))
#	Language1 = db.Column(db.Integer, db.ForeignKey('language.l_id'), nullable=False)
#	Language2 = db.Column(db.Integer, db.ForeignKey('language.l_id'), nullable=True)
#	STRmod = db.Column(db.Integer(2), default=0)
#	DEXmod = db.Column(db.Integer(2), default=0)
#	CONmod = db.Column(db.Integer(2), default=0)
#	INTmod = db.Column(db.Integer(2), default=0)
#	WISmod = db.Column(db.Integer(2), default=0)
#	CHAmod = db.Column(db.Integer(2), default=0)
#	FREEmod = db.Column(db.Integer(2), default=0)
#	Notes = db.Column(db.String(1000))
#	Source = db.Column(sb.String(5), Nullable = False, Enum(source))
#
#class Spells(db.Model):
#	S_ID = db.Column(db.Integer, primary_key=True)
#	Fullname = db.Column(db.String(50), nullable=False)
#	Level = db.Column(db.Integer(2), nullable=False)
#	School = db.Column(db.String(50), nullable=False, Enum(school))
#	Casting_Time = db.Column(db.String(50), nullable=False)
#	Ritual = db.Column(db.Boolean)
#	Concentration = db.Column(db.Boolean)
###	Classes = db.Column(db.String(50), nullable=False)	# need to pull back more than one - created new table, will need to figure this out
#	Range = db.Column(db.String(50), nullable=False, Enum(range))
#	Components = db.Column(db.String(50), nullable=False)
#	Description = db.Column(db.String(500), nullable=False)
#	Source = db.Column(sb.String(5), Nullable = False, Enum(source))
#
#class Feats(db.Model):
#	F_ID = db.Column(db.Integer, primary_key=True)
#	Name = db.Column(db.String(50), nullable=False)
#	Description = db.Column(db.String(500), nullable=False)
#	Note1 = db.Column(db.String(100))
#	Note2 = db.Column(db.String(100))
#	Note3 = db.Column(db.String(100))
#	Note4 = db.Column(db.String(100))
#	Note5 = db.Column(db.String(100))
#	Prerequisites = db.Column(db.String(50), nullable=False)
#	Source = db.Column(sb.String(5), Nullable = False, Enum(source))
#
#class Gear(db.Model):
#	G_ID = db.Column(db.Integer, primary_key=True)
#	Name = db.Column(db.String(50), nullable=False)
#	Description = db.Column(db.String(500), nullable=False)
#	Cost = db.Column(db.Float(15), nullable=False)
#	Weight db.Column(db.Float(10))
#
#class Weapons(db.Model):
#	W_ID = db.Column(db.Integer, primary_key=True)
#	Name = db.Column(db.String(50), nullable=False)
#	Cost = db.Column(db.Float(15), nullable=False)
#	Damage = db.Column(db.String(50), nullable=False)
#	Weight db.Column(db.Float(10))
#	Properties = db.Column(db.String(500), nullable=False)
#
#class Armour(db.Model):
#	A_ID = db.Column(db.Integer, primary_key=True)
#	Name = db.Column(db.String(50), nullable=False)
#	ACBoost = db.Column(db.String(50), nullable=False)
#	Cost = db.Column(db.Float(15), nullable=False)
#	Prerequisites = db.Column(db.String(50), nullable=False)
#	StealthDisadvantage = db.Column(db.Boolean)
#	Weight db.Column(db.Float(10))
#
#class MountVehicle(db.Model):
#	M_ID = db.Column(db.Integer, primary_key=True)
#	Name = db.Column(db.String(50), nullable=False)
#	Cost = db.Column(db.Float(15), nullable=False)
#	Speed = db.Column(db.String(25), nullable=False)
#	CarryWeight = db.Column(db.Integer(3), nullable=False)
#
#class TradeGoods(db.Model):
#	T_ID = db.Column(db.Integer, primary_key=True)
#	Cost = db.Column(db.Float(15), nullable=False)
#	Description = db.Column(db.String(500), nullable=False)
#
#class Consumables(db.Model):
#	C_ID = db.Column(db.Integer, primary_key=True)
#	Name = db.Column(db.String(50), nullable=False)
#	Health = db.Column(db.String(50), nullable=False)
#	Cost = db.Column(db.Float(15), nullable=False)
#	Weight db.Column(db.Float(10))

class Generator(db.Model):
	P_ID = db.Column(db.Integer, primary_key=True)
	P_Name = db.Column(db.String(100))
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

#UserFunctionality

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False, unique=True)
	content = db.Column(db.String(1000), nullable=False, unique=True)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	def __repr__(self):
		return ''.join([
			'User ID: ', str(self.user_id), '\r\n',
			'Title: ', self.title, '\r\n', self.content
		])

@login_manager.user_loader
def load_user(id):
	return Users.query.get(int(id))

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(30), nullable=False)
	last_name = db.Column(db.String(30), nullable=False)
	email = db.Column(db.String(150), nullable=False, unique=True)
	password = db.Column(db.String(200), nullable=False)
	posts = db.relationship('Posts', backref='author', lazy=True)

	def __repr__(self):
		return ''.join([
			'UserID: ', str(self.id), '\r\n',
			'Email: ', self.email, '\r\n',
			'Name: ', self.first_name, ' ', self.last_name
		])

class Content(db.Model):
	c_id = db.Column(db.Integer, primary_key=True)
	rolemodel = db.Column(db.String(50), nullable=False)
	history = db.Column(db.VARCHAR(10000), nullable = False)
	resources = db.Column(db.VARCHAR(5000))
	pictures = db.Column(db.VARCHAR(5000))
