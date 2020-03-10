from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# 5e chargen stuff

# how is this receiving? -> Pushed from routes in S1
# What is it called? -> NameSeed
# Function: Pull back info from Service2 - Character name generator + input to SQL table
# Function: Pull back info from service3 - Character stats + input to SQL table

#Future Functionality: ORD the nameSeed and Char name, (nameseed/len(nameseed))+(Charname/len(charname))=X. While X>100, sum digits.
#use final X to generate race/class
#Pass final number to service 2 and pull back that dictionary item

@app.route('/', methods=['GET', 'POST'])
def generate():
		#Service 4 receives player name from Service 1
	app.logger.info(request.data.decode("utf-8"))
		#Pings service 2 to receive randomised character name
	NameRand=requests.get("http://flask-app_Service2_1:5000/").text
		#Pings service 3 to get randomised character stats
	Stats=requests.get("http://flask-app_Service3_1:5000/").json()

		#Inputs these items into SQL table

		#returns primary key for that field to service 1

	return jsonify(name = NameRand,
		stats = Stats)


if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')


