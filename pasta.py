food = []

while True:
	name = input('商品名稱: ')
	if name == 'q':
		break

	price = input('商品價格: ')
	
	food.append([name,price])

print(food)

for foood in food:
	print('商品:', foood[0], '為', foood[1], '元')

with open('pasta.txt', 'w')as f:
	for foood in food:
		f.write(foood[0] + ',' + foood[1] + '\n')

with open('pasta.csv', 'w', encoding='utf-8')as f:        #.cvs可以用excel打開  #encoding='utf-8'  編碼
	f.write('商品,價格\n')
	for foood in food:
		f.write(foood[0] + ',' + foood[1] + '\n')