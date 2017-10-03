# Inisialisasi Masalah TSP

# baris menyatakan titik asal
# kolom menyatakan titik tujuan
# isi dari index(baris, kolom) adalah jarak dari asal ke tujuan 
himpunan_kandidat = [[999, 6, 5, 9, 5], # list jarak dari titik A
                     [6, 999, 7, 7, 3], # list jarak dari titik B               
                     [5, 7, 999, 4, 4], # list jarak dari titik C               
                     [9, 7, 4, 999, 8], # list jarak dari titik D
                     [5, 3, 4, 8, 999]] # list jarak dari titik E

perjalanan = "E->" # mulainya dari titik E

# selanjutnya kalian yang isi
###################################################################
titik = []
proses = [4, 0]
i = proses[0]
j = proses[1]
sampai = 4
while sampai not in titik:
	while j < len(himpunan_kandidat[i]):
		if(himpunan_kandidat[i][j] < himpunan_kandidat[proses[0]][proses[1]]):
			proses = [i, j]
			#print(proses, " : ", himpunan_kandidat[proses[0]][proses[1]])
			for q in range(len(himpunan_kandidat)):
				himpunan_kandidat[proses[0]][proses[1]] = 999
			j = 0
			if(proses[1] == 0): i = 0
			elif(proses[1] == 1): i = 1
			elif(proses[1] == 2): i = 2	
			elif(proses[1] == 3): i = 3
			elif(proses[1] == 4): i = 4
			
			if i not in titik:
				titik.append(i)
				if(i == sampai): perjalanan += "E"
				elif(i == 0): perjalanan += "A->"
				elif(i == 1): perjalanan += "B->"
				elif(i == 2): perjalanan += "C->"
				elif(i == 3): perjalanan += "D->"
				elif(i == 4): perjalanan += "E->"
			
		else: j+=1
		
###################################################################

# print hasil akhir
print(perjalanan) # hasil akhir harus E->B->A->C->D->E

# jawaban optimal tanpa menggunakan greedy akan terlihat seperti berikut E->B->D->C->A->E
