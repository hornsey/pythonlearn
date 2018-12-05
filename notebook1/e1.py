#coding:utf-8
import time
import random

goal = random.randint(1,10)
count = 0
while count < 5:
    temp = input("猜猜我现在想的数字是多少？")
    guess = int(temp)
    if guess == goal:
        print("真聪明！猜中啦！")
        break
    elif guess > goal:
        print("笨蛋！猜大啦!")
    else:
        print("笨蛋！猜小啦!")
    count+=1; 

print("Game Over")
