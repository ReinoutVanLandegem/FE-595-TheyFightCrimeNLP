from collections import Counter

alldisc = []

for line in open('allheros.txt'):
    if line != '\n':
        line = line.replace('\n', '')
        desc = ' '.join(line.split(' ')[1:])

        alldisc.append(desc)

count = dict(Counter(alldisc))
mostcomon = []
for key, value in sorted(count.items(), key=lambda item: item[1]):
    mostcomon.append(key)

mostcomon = mostcomon[-10:]
print(mostcomon)