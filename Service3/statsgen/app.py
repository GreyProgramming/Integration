from flask import Flask
from random import random

app = Flask(__name__)


def stat_gen():
	i=0
	stats=[]
	while i<6:
		stat=random.randint(3,18)
		stats.append(stat)
		i+=1

	return stats

@app.route('/stats')
def rand_stats():
	username=request.data.decode('UTC-8')
	list=stats(username)
	return(list)


if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0')



