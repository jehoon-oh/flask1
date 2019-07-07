import tensorflow as tf
import numpy as np

class CabbageController:
    def __init__(self, avg_temp, min_temp, max_temp, rain_fall):
        self._avg_temp = avg_temp
        self._min_temp = min_temp
        self._max_temp = max_temp
        self._rain_fall = rain_fall

    def service(self):
        avg_temp = self._avg_temp
        min_temp = self._min_temp
        max_temp = self._max_temp
        rain_fall = self._rain_fall

        # 플레이스홀더 설정
        X = tf.placeholder(tf.float32, shape=[None, 4])
        W = tf.Variable(tf.random_normal([4, 1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        saver = tf.train.Saver()

        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            save_path = 'cabbage/data/saved.ckpt'
            saver.restore(sess, save_path)

            data = [[avg_temp, min_temp, max_temp, rain_fall]]
            arr = np.array(data, dtype=np.float32)
            predict = sess.run(tf.matmul(X, W) + b, {X : arr[0:4]})
            print(predict[0])
        return int(predict[0])