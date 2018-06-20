# 비경제활동인구수/경제활동가능인구수 그래프 완성본
import csv
import matplotlib.pyplot as plt
import matplotlib as mpb

f = open('연령계층별_인구구성비_경제활동가능인구1.csv')
plt.figure(figsize=(4, 2), dpi=300) # 그래프 크기 및 해상도 조절
mpb.rcParams.update({'font.size': 4})
data = csv.reader(f)
next(data)

evp = []

for row in data:
    evp.append(int(row[2]))

f1 = open('성_활동상태별_비경제활동인구_년1.csv')
data1 = csv.reader(f1)
next(data1)
next(data1)

nevp = []

for row in data1:
    nevp.append(int(row[1])*1000)

percentage = []

for i in range(0, 18):
    percentage.append(nevp[i]/evp[i]*100)

year = []
for i in range(2000, 2018):
    year.append(i)

plt.axis([2000, 2017, 41, 44])
plt.plot(year, percentage)
plt.show()
