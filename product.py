# 二維記帳小程式
items = []
while True:
	name = input('Please enter the name of the item: ')
	if name == 'q':
		break
	price = input('Please enter the cost of the item: ')
	items.append([name, price])
print(items)
print(items[0][0])

for item in items:
	print(item)
	print(item[0], 'price is', item[1])