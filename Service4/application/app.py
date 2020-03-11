from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# 5e chargen stuff

#use final X to generate race/class
#Pass final number to service 2 and pull back that dictionary item

@app.route('/', methods=['GET', 'POST'])
def generate():
		#Service 4 receives player name from Service 1
	app.logger.info(request.data.decode("utf-8"))
	Player=request.data.decode("utf-8")
		#Pings service 2 to receive randomised character name
	Char_Name=requests.get("http://flask-app_Service2_1:5000/").text
		#Pings service 3 to get randomised character stats
	Stats=requests.get("http://flask-app_Service3_1:5000/").json()

	return jsonify(name = Char_Name,
		stats = Stats)

		#Inputs these items into SQL table - P_ID should be auto-generated
	generated = Generator(
		P_Name = Player,
		C_Name = Char_Name,
		Lv = "1",				# Once MVP is attained
		Align = "Neutral",			# Come back and
		Gender = "Not Applicable",		# Create more generators
		Race = "Test",				# For all of these
		Class = "The Classiest",		# -MGrey
		STR = Stats.STR,
		DEX = Stats.DEX,
		CON = Stats.CON,
		INT = Stats.INT,
		WIS = Stats.WIS,
		CHA = Stats.CHA
	)

	db.session.add(generated)
	db.session.commit()

		#returns primary key for that field to service 1

	return str(Generator.P_ID)


if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0')


