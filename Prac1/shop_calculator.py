items = int(input("Number of items: "))
while items < 0:
    items = int(input("Number of items: "))
total = 0
for i in range(items):
    price = float(input("Price of item: "))
    total = total + price
if total > 100:
    Total = total * ((100-10)/100)
print("Total price for", items, 'items is $', Total)