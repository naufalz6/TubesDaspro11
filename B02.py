import F01

def upgrade_gold(username):
	user = F01.pilihan("user.csv")
	premium = F01.pilihan("premium.csv")
	check = False
	while not(check) :
		for i in range(11):
			if (user[i][3] == username):
				check = True
				indexuser = i
				break
	for j in range(11):
		if premium[j][0] == '':
			p = j
			break
	premium[p][0] = user[indexuser][0]
	premium[p][1] = user[indexuser][1]
	premiumu[p][2] = user[indexuser][2]
	premium[p][3] = user[indexuser][3]
	premium[p][4] = user[indexuser][4]
	premium[p][5] = user[indexuser][5]
	premium[p][6] = user[indexuser][6]
	return premium