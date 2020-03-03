from random import random

def stat_gen()
	i=0
	stats[]

	While i<6:
	#Roll 4 D6
		rolls=[]
		for j in range(4):
			roll=random.randint(1,6),
			rolls.append(roll)

	#remove lowest, sum others, store in list
		rolls.remove(min(rolls))
		stats.append(sum(rolls))

		i+=1

	Primary=max(stats)
	stats.remove(max(stats))

	Secondary=max(stats)
	stats.remove(max(stats))

	StatA=max(stats)
	stats.remove(max(stats))

	StatB==max(stats)
	stats.remove(max(stats))

	StatC==max(stats)
	stats.remove(max(stats))

	Dumpstat=max(stats)
	stats.remove(max(stats))

	db.add(stats)
