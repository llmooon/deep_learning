import tensorflow as tf

data=[[2,81],[4,93],[6,91],[8,97]]
x_data = [x_row[0] for x_row in data]
y_data = [y_row[1] for y_row in data]

#기울기 a 와 y 절편 b의 값을 임의로 정한다.(a: 0~10 , b : 0~100)
a=tf.Variable(tf.random_uniform([1],0,10,dtype=tf.float64,seed=0))
b=tf.Variable(tf.random_uniform([1],0,100,dtype=tf.float64,seed=0))

#y에 대한 일차 방정식
y=a*x_data+b

#rmse
rmse=tf.sqrt(tf.reduce_mean(tf.square(y-y_data)))
#학습률
learningrate=0.001

#최소 점 찾기
gradient_decent = tf.train.GradientDescentOptimizer(learningrate).minimize(rmse);

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for step in range(2001):
        sess.run(gradient_decent)
        if step%100==0:
            print("Epoch =  %.f , rmse = %.04f , 기울기 = %.4f , y절편 = %.4f"%(step,sess.run(rmse),sess.run(a),sess.run(b)))