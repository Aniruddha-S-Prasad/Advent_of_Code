import numpy as np

def main():
	guide = np.genfromtxt('input.txt', delimiter=' ', dtype='U75')

	my_play = np.zeros(guide.shape[0], dtype='int')
	my_play[guide[:, 1] == 'X'] += 1
	my_play[guide[:, 1] == 'Y'] += 2
	my_play[guide[:, 1] == 'Z'] += 3

	opp_play = np.zeros(guide.shape[0], dtype='int')
	opp_play[guide[:, 0] == 'A'] += 1
	opp_play[guide[:, 0] == 'B'] += 2
	opp_play[guide[:, 0] == 'C'] += 3

	win = [2, 3, 1]
	win_play = [win[x - 1] for x in opp_play]
	lose = [3, 1, 2]
	lose_play = [lose[x - 1] for x in opp_play]

	score = np.zeros(guide.shape[0])

	# Rock	Paper	Scissors
	# A		B		C
	# 1		2		3
	# Draws with
	# 1		2		3
	# Wins against
	# 3		1		2
	# Loses against
	# 2		3		1
	score += my_play
	score[my_play == opp_play] += 3
	score[my_play == win_play] += 6
	score[my_play == lose_play] += 0
	print(score.sum())

	return

if __name__=='__main__':
	main()