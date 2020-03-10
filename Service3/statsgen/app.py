from flask import Flask, jsonify
import random

app = Flask(__name__)


def stat_gen():
	i=0
	stats=[]
	while i<6:
		stat=random.randint(3,18)
		stats.append(stat)
		i+=1

	return stats

@app.route('/')
def rand_stats():
	sA,sB,sC,sD,sE,sF=stat_gen()
	return jsonify(STR = sA,
		DEX = sB,
		CON = sC,
		INT = sD,
		WIS = sE,
		CHA = sF)


if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')



