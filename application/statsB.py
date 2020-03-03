from random import random

def stat_gen()
	i=0
	stats=[]
	While i<6
		stat=random.randint(3,18)
		stats.append(stat)
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
