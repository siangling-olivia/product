# 二維記帳小程式


import os # operating systems

# 讀取csv檔案+Split
def readfile(filename):
	items = []
	with open(filename, 'r', encoding='utf-8') as f:
		for item in f:
			if 'Item, Cost' in item:
				continue
			name, price = item.strip().split(',')
			items.append([name, price])
	return items


#讓使用者輸入
def userinput(items):
	while True:
		name = input('Please enter the name of the item: ')
		if name == 'q':
			break
		price = input('Please enter the cost of the item: ')
		items.append([name, price])
	print(items) 
	return items

# 把所有購買紀錄印出來
def printitems(items):
	for item in items:
		print(item)
		print(item[0], 'price is', item[1])

#寫入檔案到csv
def writefile(filename, items):
	with open(filename, 'w', encoding='utf-8') as f: # 為了避免有中文的亂碼
		f.write('Item, Cost\n')
		for item in items:
			f.write(item[0] + ',' + item[1] + '\n' )


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): # 先檢查檔案是否存在
		print('Find the file.')
		items = readfile(filename)
	else:
		print('Could not find the file.')

	items = userinput(items)
	printitems(items)
	writefile('products.csv', items)


main()