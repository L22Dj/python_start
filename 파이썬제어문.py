# -*- coding: utf-8 -*-
"""파이썬제어문.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AXe6n54NHKMZ6VF2CkTlryKCurqIUs19
"""

# 2
food = input('먹고 싶은 음식은 : ')
print('당신이 입력한 먹고 싶은 음식은' + food + ' 입니다.')
print('오늘 비가 오네요 우산을 들고가세요!')
if food == '자장면':
    print('중국집으로 가요.')
elif food == '회':
    print('일식집으로 가요.')
elif food == '떡볶이':
    print('분식집으로 가요.')
elif food == '우동':
    print('우동집으로 가요.')
else:
    print('자장면, 회, 떡볶이, 우동이 아니면 그냥 집에서 먹어요.')

start = 1 #시작값
while start <= 10: #조건식
    print(start, ' -> 내가 반복')
    start += 1 # start = start + 1, 증감식

start = 0
while start < 10:
    print(start, ' -> 내가 반복')
    start += 1 # start = start + 1

start = 0
while start < 10:
    start += 1 # start = start + 1
    print(start, ' -> 내가 반복')

for _ in range(0,10): #변수 설정을 하지 않을 경우 _ 로 채워 넣어준다.
    print('나도 반복')

for i in range(0,10): # 0~9, default : 1씩 증가
    print(i)

for i in range(11):
    print(i)

for i in range(0,10,2): # 0~9, default : 1씩 증가
    print(i)

sum = 0
for i in range(0,10):
    sum += i
    print(sum)

#1
time = int(input('현재 시간을 입력하세요 : '))
if time <= 11:
    print('굿 모닝')
elif 11 < time <= 15:
    print('굿 애프터눈')
elif 15 < time <= 20:
    print('굿 이브닝')
else:
    print('굿 나잇')

month = int(input('이번달은 몇 월인가요? '))
if 3 <= month < 6:
    print(month,'월은 봄입니다.')
elif 6 <= month < 9:
    print(month,'월은 여름입니다.')
elif 9 <= month < 12:
    print(month,'월은 가을입니다.')
else:
    print(month,'월은 겨울입니다.')

food = list(input('음식을 입력하세요'))