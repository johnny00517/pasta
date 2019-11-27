food = []

while True:
	name = input('商品名稱: ')
	if name == 'q':
		break

	price = input('商品價格: ')
	
	food.append([name,price])

print(food)

for f in food:
	print('商品:', f[0], '為', f[1], '元')