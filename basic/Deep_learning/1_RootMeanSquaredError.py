#RMSE 평균 제곱 오차/ 평균 제곱근 오차
import numpy as np

#임의로 선분 생성. 기울기와 y 절편 생성
ab=[3,76]

data=[[2,81],[4,93],[6,91],[8,97]]
x=[i[0] for i in data]
y=[i[1] for i in data]

#임의로 생성한 선분의 값 리턴.
def predict(x):
    return ab[0]*x+ab[1]

#평균 제곱 오차 구하는 과정
def rmse(p,a):
    return np.sqrt(((p-a)**2).mean())

def rmse_val(predict_result,y):
    return rmse(np.array(predict_result),np.array(y))

#각각의 x 값에 따른 임의의 선분의 y 값 저장
predict_result=[]
for i in range(len(x)):
    predict_result.append(predict(x[i]))

#최종 RMSE
print(rmse_val(predict_result,y))
