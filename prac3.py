# 리스트 데이터 타입
students = ["kiji", "sori", "maru"]
grades = [2,1,4]
print(students[1])
print(len(students))
print(min(grades))
print(max(grades))
print(sum(grades))

import statistics
print(statistics.mean(grades)) # 평균 구하기

import random
print(random.choice(students)) # 리스트 중 랜덤으로 원소 하나 뽑기