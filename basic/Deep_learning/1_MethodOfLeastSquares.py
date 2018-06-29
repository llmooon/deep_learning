#최소 제곱법
import numpy as np

x=[2,4,6,8]
y=[81,93,91,97]

#numpy를 이용하여 평균을 구한다.
mx=np.mean(x)
my=np.mean(y)

#divisor 인자에 최소 제곱근 공식 중 분모의 값을 저장한다.
divisor = sum([(mx-i)**2 for i in x]) # **2 => 제곱을 의미한다.
# print(divisor)
def top(x,mx,y,my):
    d=0
    for i in range(len(x)):
        d+=(x[i]-mx)*(y[i]-my)
    return d
dividend = top(x,mx,y,my)

#기울기
a=dividend/divisor
#y절편
b=my-(mx*a)
print("기울기 : "+str(a) + " y절편 : "+str(b))
