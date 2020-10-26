def read_file(filename):#fun1
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:#有可能在第一行會顯示\ufeff 可寫為uft-8-sig
		for line in f :
			lines.append(line.strip())#strip可以把\n去除
	return lines

def convert(lines): #格式轉換 #for loop就是把清單中一個一個叫出來 這邊的話就是把lines裡面的內容較囉
	new = []
	person = None #預設值先設為無 
	#person = '123'   #先把person宣告出來
	for line in lines:
		if line == 'Allen':
			 person = 'Allen'
			 continue #會直接跳到下一個迴圈 
		elif line == 'Tom':
			 person = 'Tom'
			 continue
		if person: #如果person有值才繼續執行
		#if person !='123' #如果person不是預設值的話才執行下面
			new.append(person + ': ' + line) 
		#+為字串合併 #
	return new
	#print(new)  
	#但如果第一行不為人名會error
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n') #真正寫入檔案的部分

def main():#fun2
	lines = read_file('input.txt') #把檔名變參數
	lines = convert(lines) #覆蓋的感覺
	write_file('output.txt', lines)
main() #程式的進入點
