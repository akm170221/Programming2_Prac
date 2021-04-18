for i in range( 0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()
stars = int(input("Number of stars: "))
symbol = "*"
for i in range(stars):
    print(symbol, end=' ')

stars = int(input("Number of stars: "))
for i in range(0, stars):
    for j in range(0, i + 1):
        print("*", end=' ')

    print("\r")
