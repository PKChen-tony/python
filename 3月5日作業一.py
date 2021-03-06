data=list()
print("******程式執行結果******")
while len(data) <= 5:
    num = int(input("請輸入數字:"))
    data.append(num)
print("串列內容:",data)
print('氣泡排序法：原始資料為：')
for i in range(6):
    print('%3d' %data[i],end='')
print()

for i in range(5,-1,-1): #掃描次數
    for j in range(i):
        if data[j]>data[j+1]:#比較,交換的次數
            data[j],data[j+1]=data[j+1],data[j]#比較相鄰兩數,如果第一數較大則交換
    print('第 %d 次排序後的結果是：' %(6-i),end='') #把各次掃描後的結果印出
    for j in range(6):
        print('%3d' %data[j],end='')
    print()
	
print('排序後結果為：')
for j in range(6):
    print('%3d' %data[j],end='')
print()

"""
******程式執行結果******

請輸入數字:10

請輸入數字:80

請輸入數字:9

請輸入數字:6

請輸入數字:70

請輸入數字:80
串列內容: [10, 80, 9, 6, 70, 80]
氣泡排序法：原始資料為：
 10 80  9  6 70 80
第 1 次排序後的結果是： 10  9  6 70 80 80
第 2 次排序後的結果是：  9  6 10 70 80 80
第 3 次排序後的結果是：  6  9 10 70 80 80
第 4 次排序後的結果是：  6  9 10 70 80 80
第 5 次排序後的結果是：  6  9 10 70 80 80
第 6 次排序後的結果是：  6  9 10 70 80 80
排序後結果為：
  6  9 10 70 80 80
"""
