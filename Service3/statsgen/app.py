from random import random

def stat_gen()
	i=0
	stats=[]
	While i<6
		stat=random.randint(3,18)
		stats.append(stat)
		i+=1

	return stats

@app.route('/stats')
	def rand_stats()
		username=request.data.decode('UTC-8')
		list=stats(username)
		return(list)

