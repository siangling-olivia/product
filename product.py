# 二維記帳小程式

# 讀取csv檔案+Split
items = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for item in f:
		if 'Item, Cost' in item:
			continue
		name, price = item.strip().split(',')
		items.append([name, price])
while True:
	name = input('Please enter the name of the item: ')
	if name == 'q':
		break
	price = input('Please enter the cost of the item: ')
	items.append([name, price])
print(items) 

# 把所有購買紀錄印出來
for item in items:
	print(item)
	print(item[0], 'price is', item[1])

#寫入檔案到csv
with open('products.csv', 'w', encoding='utf-8') as f: # 為了避免有中文的亂碼
	f.write('Item, Cost\n')
	for item in items:
		f.write(item[0] + ',' + item[1] + '\n' )