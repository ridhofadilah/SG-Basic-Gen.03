# tempat mengerjakan coin change dengan greedy
himpunan_kandidat = [5,4,3,1];
Coin = 7
solusi = [];



while(Coin is not 0):
    while(himpunan_kandidat):
        tukar = max(himpunan_kandidat)
        if(Coin - tukar >= 0):
            Coin -= tukar;
            solusi.append(tukar)
            break
        else:
            himpunan_kandidat.pop()
print(solusi)