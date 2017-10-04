# tempat mengerjakan coin change dengan greedy
kandidat = [5,4,3,1];
my_coin = 12
solusi = [];
kandidat.sort()

while (my_coin is not 0):
	while (kandidat):
		temp = max(kandidat)
		if (my_coin-temp>=0):
			solusi.append(temp)
			my_coin -= temp;
			break
		else:
			kandidat.pop()

print(solusi)