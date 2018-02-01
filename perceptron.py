# -*- encoding=utf-8 -*-
class Perceptron(object):
    def __init__(self,input_num,activator):
        '''
        初始化感知器，设置输出参数的个数，以及激活函数，
        激活函数的类型为double->double
        '''
        self.activator=activator
        #权重向量初始化为0
        self.weights=[0.0 for x in range(input_num)]
        #偏置初始化为0.0
        self.bias=0.0

    def __str__(self):
        return 'weights\t: %s\nbias\t:%f\n'%(self.weights,self.bias)

    def predict(self,input_vec):
        '''
        输入向量，输出感知器的计算结果
        '''
        # 把input_vec[x1,x2,x3...]和weights[w1,w2,w3,...]打包在一起
        # 变成[(x1,w1),(x2,w2),(x3,w3),...]
        # 然后利用map函数计算[x1*w1, x2*w2, x3*w3]
        # 最后利用reduce求和
        return self.activator(
            reduce(lambda a,b:a+b,
                   map(lambda (x,w):x*w,
                       zip(input_vec,self.weights)),0.0)+self.bias
        )

    def train(self,input_vecs,labels,iteration,rate):
        '''
        :param input_vecs:输入向量
        :param labels:与每一输入向量对应的label
        :param iteration:训练轮数
        :param rate:学习率
        :return:
        '''
        for i in range(iteration):
            self._one_iteration(input_vecs,labels,rate)

    def _one_iteration(self,input_vecs,labels,rate):
        '''
        一次迭代，把所有的训练数据过一遍
        '''
        # 把输入和输出打包在一起，成为样本的列表[(input_vec, label), ...]
        # 而每个训练样本是(input_vec, label)
        samples=zip(input_vecs,labels)
        #对每个样本，按照感知器规则进行更新权重
        for (input_vec,label) in samples:
            #计算感知器在当前权重下的输出
            output=self.predict(input_vec)
            #更新权重
            self._upgrate_weights(input_vec,output,label,rate)

    def _upgrate_weights(self,input_vec,output,label,rate):
        '''
        更新权重
        :param input_vec:
        :param output:
        :param label:
        :param rate:
        :return:
        '''
        delta=label-output
        self.weights=map(
            lambda (x,w): w+rate*delta*x,zip(input_vec,self.weights)
        )
        self.bias+=rate*delta

def f(x):
    '''
    定义激活函数
    :param x:
    :return:
    '''
    return 1 if x>0 else 0

def get_training_dataset():
    '''
    基于and真实表构建训练数据
    :return:
    '''
    input_vects=[[1,1],[0,0],[1,0],[0,1]]
    labels=[1,0,0,0]
    return input_vects,labels

def train_and_perceptron():
    '''
    使用and真值表训练感知器
    :return:
    '''
    p=Perceptron(2,f)
    input_vects,labels=get_training_dataset()
    p.train(input_vects,labels,10,0.1)
    return p

if __name__ == '__main__':
    and_perception=train_and_perceptron()
    print and_perception

    #测试

    print '1 and 1 = %d' % and_perception.predict([1, 1])
    print '0 and 0 = %d' % and_perception.predict([0, 0])
    print '1 and 0 = %d' % and_perception.predict([1, 0])
    print '0 and 1 = %d' % and_perception.predict([0, 1])


















































