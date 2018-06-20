# 회귀분석
import csv
import matplotlib.pyplot as plt
import numpy as np

# 파일 불러오기
f = open('출생아수와 사망자수.csv')
data = csv.reader(f)

year = []
icm = []
plt.grid(True)

for row in data:
    year.append(int(row[0]))
    icm.append(int(row[1]) - int(row[2]))

# 회귀분석
# x, y의 평균값
mx = np.mean(year)
my = np.mean(icm)

# 기울기 공식의 분모
# x편차 총합
divisor = sum([(mx - i) ** 2 for i in year])


# 기울기 공식의 분자
def top(year, mx, icm, my):
    d = 0
    for i in range(len(year)):
        d += (year[i] - mx) * (icm[i] - my)
    return d


dividend = top(year, mx, icm, my)

# 기울기와 y절편 구하기
a = dividend / divisor
b = my - (mx * a)

x = [c for c in range(1970, 2018)]
y = [a * d + b for d in range(1970, 2018)]
plt.plot(x, y)

xx = [c for c in range(2018, 2030)]
yy = [a * d + b for d in range(2018, 2030)]
plt.plot(xx, yy, 'r--')

zerospot = -(b/a)

plt.plot(year, icm)
plt.show()
print(zerospot)
