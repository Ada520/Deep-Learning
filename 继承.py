# -*- encoding:utf-8 -*-

'''
在OOP程序设计中，当我们定义一个class的时候，
可以从某个现有的class继承，新的class称为子类Subclass），
而被继承的class称为基类、父类或超类（Base class、Super class）。
比如，我们已经编写了一个名为Animal的class，
有一个run()方法可以直接打印：
'''
class Animal(object):
    def run(self):
        print 'Animal is running'
'''
#当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：

class Dog(Animal):
    pass
class Cat(Animal):
    pass
#对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
#继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，
# 什么事也没干，就自动拥有了run()方法：
dog=Dog()
dog.run()
cat=Cat()
cat.run()
'''

'''
#当然也可以对子类增加一些方法，比如Dog类：
class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat...'

'''

'''
#继承的第二个好处是只需要我们对代码做一点改进即可。
# 你看到了，无论是Dog还是Cat，它们run()的时候，
# 显示的都是Animal is running...，符合逻辑的做法是
# 分别显示Dog is running...和Cat is running...，因此，对Dog和Cat类改进如下：
class Dog(Animal):
    def run(self):
        print 'Dog is running...'

class Cat(Animal):
    def run(self):
        print 'Cat is running...'

dog=Dog()
dog.run()
cat=Cat()
cat.run()

'''

#当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。




















