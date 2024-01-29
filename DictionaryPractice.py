temps = [27,31,23,34,37,38,29,30,35,30]
sum = 0
days = 7

for i in range(days):
    sum += temps[i]

print(sum/days)

print(max(temps))

daytemps = {
    "Jan 1" : 27,
    "Jan 2" : 31,
    "Jan 3" : 23,
    "Jan 4" : 34,
    "Jan 5" : 37,
    "Jan 6" : 38,
    "Jan 7" : 29,
    "Jan 8" : 30,
    "Jan 9" : 35,
    "Jan 10" : 30
}

print(daytemps["Jan 9"])
print(daytemps["Jan 4"])


fhand = open("poem.txt")

poemwrds = dict()
for line in fhand:
    words = line.split()
    for word in words:
        poemwrds[word] = poemwrds.get(word,0) + 1

print(poemwrds)