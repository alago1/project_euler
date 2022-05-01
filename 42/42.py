triangles = {1}
s = 1
t = 2
while s < 420:
    s += t
    t += 1
    triangles.add(s)

with open('words.txt') as file:
    words = file.read().split(",")
    
vals = {k:v for v, k in enumerate("\"ABCDEFGHIJKLMNOPQRSTUVWXYZ")}
n_tria = 0
for word in words:
    s = 0
    for letter in word:
        s += vals[letter]
    
    if s in triangles:
        n_tria += 1

print(n_tria)