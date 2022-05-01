hexagons = set()

for i in range(1, 10**6):
    hexagons.add(i * (2*i-1))

pentagons = set()
for i in range(1, 10**6 * 3//4):
    p = i * (3*i-1)//2
    if p in hexagons:
        pentagons.add(p)

for i in range(1, 10**6 // 4):
    t = i * (i+1)//2
    if t in pentagons:
        print(f"T_{i} = {t}")