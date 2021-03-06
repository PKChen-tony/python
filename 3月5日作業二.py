import random
first = int (random.randint(1,49) )     #第一個號碼不會重覆
biglottery=[]
biglottery.append(first)                #直接放入

while (len(biglottery)<7):              #少於7顆球再重抽
    for check in biglottery:
        r = int (random.randint(1,49) )
        if check == r:                  #重號
            pass
        else:   
            biglottery.append(r)        #不重號加入  
print("****程式執行結果****")
print("大樂透號:")
print(biglottery[0:6])
print("特別號:")
print(biglottery[6])     
"""
****程式執行結果****
大樂透號:
[49, 27, 12, 16, 23, 9]
特別號:
36
"""