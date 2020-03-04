from random import random

def StatGen()
	i=0
	stats{}

	While i<6:
	#Roll 4 D6
		rolls=[]
		for _ in range(4):
			roll=random.randint(1,6),
			rolls.append(roll)

	#remove lowest, sum others, store in list
		rolls.remove(min(rolls))
		stats.append(sum(rolls))

		i+=1

	return stats
