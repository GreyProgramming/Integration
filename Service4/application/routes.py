from flask import render_template

from application import app
from application.models import 5eGenerator
from application.forms import 5eGeneratorForm

from Service2/namegen import app
from Service3/statsgen import app

# 5e chargen stuff


# how is this receiving? -> Pushed from routes in S1
# What is it called? -> NameSeed
# Function: Pull back info from Service2 - Character name generator + input to SQL table
# Function: Pull back info from service3 - Character stats + input to SQL table

#Future Service 4 Functionality: ORD the nameSeed and Char name, (nameseed/len(nameseed))+(Charname/len(charname))=X. While X>100, sum digits.
#use final X to generate race/class
#Pass final number to service 2 and pull back that dictionary item




@app.route('/dndchargen/1', methods=['GET', 'POST'])
def generate():
	char=5eGenerator(
		Character_Name = response[random_name()]
	)
	charname=requests.post(
