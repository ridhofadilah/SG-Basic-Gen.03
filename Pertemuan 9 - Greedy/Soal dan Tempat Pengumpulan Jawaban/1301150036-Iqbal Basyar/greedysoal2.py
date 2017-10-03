# tempat mengerjakan coin change dengan greedy
himpunan_kandidat = [5, 4, 3, 1];



myCoin = 7
solution = [];

himpunan_kandidat.sort() #mastiin aja si

while (myCoin is not 0):
    next = himpunan_kandidat
    while(next):
        tukar = max(next)
        if (myCoin - tukar >= 0):
            myCoin -= tukar;
            solution.append(tukar)
            break
        else:
            next.pop()

print(solution)
