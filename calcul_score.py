# -*- coding: utf-8 -*-

def calcul_score(lst1, lst2):
	score0 = 0 #common tags
	score1 = 0 #only in 1
	score2 = 0 #only in 2

	tags1 = lst1[2::]
	tags2 = lst2[2::]

	for tag in tags1:
		if tag in tags2:
			score0 += 1

	score1 = max(len(tags1)-score0, 0)
	score2 = max(len(tags2)-score0, 0)

	score_final = min(score0, score1, score2)
	
	print(score_final)

	return score_final


calcul_score(['H', 4, 'test', 'test1', 'test2', 'test3'], ['H',4, 'test2', 'test3', 'test4', 'test5'])
