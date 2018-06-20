# 비경제활동인구수 별 활동 내역 남자 완성본
import csv
import matplotlib.pyplot as plt
import matplotlib as mpb

f = open('성_활동상태별_비경제활동인구_년1.csv')
plt.figure(figsize=(4, 2), dpi=300)  # 그래프 크기 및 해상도 조절
mpb.rcParams.update({'font.size': 4})
data = csv.reader(f)
next(data)
next(data)

year = []
취업준비 = []
전체 = []
육아 = []
가사 = []
통학 = []
연로 = []
심신장애 = []
그외 = []
list_of_list = [year, 전체, 육아, 가사, 통학, 연로, 심신장애, 그외, 취업준비]
year = [a for a in range(2000, 2018)]

for row in data:
    for num in range(0, 9):
        list_of_list[num].append(int(row[num+8]))

plt.xticks(year)
plt.plot(year, 가사, 'g', label='가사')
plt.plot(year, 육아, 'r', label='육아')
plt.plot(year, 통학, 'b', label='통학')
plt.plot(year, 연로, 'y', label='연로')
plt.plot(year, 심신장애, 'k', label='심신장애')
plt.plot(year, 그외, 'magenta', label='그외')
plt.plot(year, 취업준비, 'cyan', label='취업준비')

plt.legend()

plt.show()
