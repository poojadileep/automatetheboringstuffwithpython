import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
 ht = []
 flip = random.randint(0,1)
 ht.append(flip)

for i in range(len(ht)-6) :
  if ht[i] == ht[i+1] ==  ht[i+2] == ht[i+3] == ht[i+4] == ht[i+5] :
    numberOfStreaks += 1
print(numberOfStreaks)


    # Code that checks if there is a streak of 6 heads or tails in a row.
print('Chance of streak: %s%%' % (numberOfStreaks / 100))
