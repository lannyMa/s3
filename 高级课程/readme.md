# 介绍:
当下主流的编程方法有三种：函数式，面向过程，面向对象，三者相当于编程界的三个门派，每个门派有自己的独门秘籍，都是用来解决问题的。三种流派都是一种编程的方法论，只不过是各自的风格不同，在不同的应用场景下也各有优劣。



# 一：函数式编程：函数式=编程语言定义的函数+数学意义的函数

通俗来讲，函数式就是用编程语言去实现数学函数。这种函数内对象是永恒不变的，要么参数是函数，要么返回值是函数，没有for和while循环，所有的循环都由递归去实现，无变量的赋值（即不用变量去保存状态），无赋值即不改变。



## PART1 特征：

1.不可变数据
2.第一类对象
3.尾调用优化（尾递归）



#### 例一：不可变：不用变量保存状态，不修改变量
```
#非函数式
a=1
def incr_test1():
    global a
    a+=1
    return a

incr_test1()
print a

#函数式
n=1
def incr_test2(n):
    return n+1

print incr_test2(2)
print n
```

#### 例二：第一类对象：函数即“变量”

函数名可以当做参数传递
返回值可以是函数名


#### 例三：尾调用：在函数的最后一步调用另外一个函数
(最后一步不一定是函数的最后一行)

```
# 函数bar在foo内为尾调用
def bar(n):
    return n
def foo(x):
    return bar(x)

```

```
# 函数bar1和bar2在foo内均为尾调用，二者在if判断条件不同的情况下都有可能作为函数的最后一步

def bar1(n):
    return n

def bar2(n):
    return n+1

def foo(x):
    if type(x) is str:
        return bar1(x)
    elif type(x) is int:
        return bar2(x)
```

```
# 函数bar在foo内为非尾调用
def bar(n):
    return n
def foo(x):
    y=bar(x)
    return y


# 函数bar在foo内为非尾调用
def bar(n):
    return n
def foo(x):
    return bar(x)+1
```

#### 尾调用优化:
尾调用的关键就在于是在函数的最后一步去调用别的函数，那么最后一步调用，有何好处
根据函数即“变量”的定义，定义a函数，a内调用函数b，b内调用函数c，在内存中会形成
一个调用记录，又称调用帧（call frame），用于保存调用位置和内部变量等信息，即a->b->c
直到c返回结果给b，c的调用记录才会消失，b返回给a，b的调用记录消失，a返回结果,a的调用
记录消失，所有的调用记录，都是先进后出，形成了一个“调用栈”（call stack）

![](https://images2018.cnblogs.com/blog/1312420/201804/1312420-20180406161816106-152764639.png)


尾调用由于是函数的最后一步操作，所以不需要保留外层函数的调用记录，因为调用位置、
内部变量等信息都不会再用到了，只要直接用内层函数的调用记录，取代外层函数的调用记录就可以了。

```
def bar(n):
    return n

def foo(x):
    return bar(x)

print foo(3) #foo(3)就等于bar(3),也就是说，foo在最后一步调用了bar，然后foo的调用记录就
             #清除了，剩下的就是bar自己的事情了。所有内存里永远只保留一个调用记录
bar(3)
```
这就叫做"尾调用优化"（Tail call optimization），
即只保留内层函数的调用记录。如果所有函数都是尾调用，那么完全可以做到每次执行时，
调用记录只有一项，这将大大节省内存。这就是"尾调用优化"的意义。


#### 尾递归：

定义：函数调用自身，称为递归。如果尾调用自身，就称为尾递归。
递归特点：重复相同的事情，每次重复会使问题规模减少

#### 递归举例：
问题：人口普查，包括全国各地总人数，每个人所在的地域，家族成员
解决方法：
找来所有省长，让他们去统计各自省的人口情况
省长安排市长去统计
市长安排给县长。。。

![](https://images2018.cnblogs.com/blog/1312420/201804/1312420-20180406161904984-1753625696.png)


#### 尾递归举例：
问题：师傅，天安门怎么走？
解决方法：a问b，b不知道，b去问c，c去问d，最后由d得出结果，此过程可以发现，问题最后只需要d去解决就ok了，a,b,c都无需保存任何记录，不干事，因为他们啥都不知道。

#### 尾递归的优点：

递归非常耗费内存，因为需要同时保存成千上百个调用记录，很容易发生"栈溢出"错误（stack overflow）。但对于尾递归来说，由于只存在一个调用记录，所以永远不会发生"栈溢出"错误。



#### 由递归转成尾递归：

下面的代码是一个阶乘函数，计算n的阶乘，最多需要保存n个调用记录，复杂度为O(n)
```
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)


print factorial(5)
```

如果改成尾递归，只保留一个记录，复杂度为O(1)
```
def factorial(n,total):
    if n == 1:
        return total
    return factorial(n-1,n*total)


print factorial(5,1)
```

分析：

由上述示范可以看出，尾递归的实现，往往需要修改递归函数，确保最后一步调用自身。
要做到这一点，就是把函数的内部变量变成参数传递。如上例，但是带来一个问题是：改写后的函数需要新增一个形参total，这样你在做5的阶乘的时候，变成了factorial(5,1)这个1让人很费解


#### 解决方法一：定义默认参数
```
def factorial(n,total=1):
    if n == 1:
        return total
    return factorial(n-1,n*total)


print factorial(5)
```

#### 解决方法二：在尾递归外新增一个正常形式的函数
```
def tailfactorial(n,total):
    if n == 1:
        return total
    return tailfactorial(n-1,n*total)


def factorial(n):
    return tailfactorial(n,1)

print factorial(5)
```

#### 解决方法三：函数式编程友谊概念，叫做柯里化（currying）,意思是将多个参数转成单参数形式，这里可以用到柯里化（python中使用偏函数实现柯里化），与方法二类似
```
from functools import partial

def tailfactorial(n,total):
    if n == 1:
        return total
    return tailfactorial(n-1,n*total)



factorial=partial(tailfactorial,total=1)

print factorial(5)
```

偏函数简单示例
```
from operator import add,mul
from functools import partial

add1=partial(add,1)
mul10=partial(mul,10)

print add1(10)
print add1(11)

print mul10(1)
print mul10(2)
```

## PART2 相关编程技术
1.mapping(映射)
```
#统计名字长度
names=['alex','runtu','feng']

#for循环式解决，可读性差
names_length=[]
for i in names:
    names_length.append(len(i))
print names_length

#函数式解决，可读性好，透明度高
print map(len,names)
```

2.reducing（合并）
```
sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

sam_count = 0
for sentence in sentences:
    sam_count += sentence.count('Sam')

print sam_count
sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.',
             'Sam chortled.']

sam_count = reduce(lambda a, x: a + x.count('Sam'),
                   sentences,
                   0)
```

3.piplining（管道）

4.recursing（递归）

5.currying（柯里化）:
```
from operator import add,mul
from functools import partial

add1=partial(add,1)
mul10=partial(mul,10)

print add1(10)
print add1(11)

print mul10(1)
print mul10(2)
```

6.高阶函数

7.闭包

8.lambda

这里请参考我另一篇文章，函数与函数式编程

## PART3 函数式编程属性
1.并行
```
对于为什么要使用函数式编程，这有一个更好的论据?
    现代的应用程序都会牵涉到多核计算机上的并行运算功能，
    程序状态就成了一个问题。所有的命令式语言，包括面向对象语言，
    在涉及多线程时，都会遇到共享对象的状态修改问题。这就是死锁、堆栈跟踪、
    低级处理器缓存命中率低等问题的根源。
    如果对象没有状态，这些问题就不存在了。
```

2.惰性计算

a.列表解析与生成器

b.yield与协程(微线程,英文名Coroutine）
```
#列表解析
l=[i for i in range(10) if i%2 == 0]

#[0, 2, 4, 6, 8]
```

```
#生成器
l=(i for i in range(10) if i%2 == 0)

#<generator object <genexpr> at 0x028E1CD8>
```

```
#协程
'''
子程序，或者称为函数，在所有语言中都是层级调用，比如A调用B，B在执行过程中又调用了C，
C执行完毕返回，B执行完毕返回，最后是A执行完毕。
所以子程序调用是通过栈实现的，一个线程就是执行一个子程序。
协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，
在适当的时候再返回来接着执行。
但协程的特点在于是一个线程执行，那和多线程比，协程有何优势？
最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，
没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，
又充分发挥协程的高效率，可获得极高的性能。
Python对协程的支持还非常有限，用在generator中的yield可以一定程度上实现协程。虽然支持不完全，但已经可以发挥相当大的威力了
传统的生产者-消费者模型是一个线程写消息，一个线程取消息，通过锁机制控制队列和等待，
但一不小心就可能死锁。
如果改用协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后
切换回生产者继续生产，效率极高：

“子程序就是协程的一种特例。”

函数内使用yield变成生成器，func.next(),遇到yield就返回yield后面跟的值，
下次调用直接从yield的位置开始
如果c=func(),c.send(i)，那么yield的位置会获取i这个值，生成器函数不会返回，会继续运行yield下面的操作
'''
def consumer():
    r=''
    while True:
        n=yield r
        print('吃货:包子[%s]来了，吃包子' %n)
        time.sleep(1)
        r='200 ok'

def producer(c):
    c.next()
    for i in range(5):
        print('厨师:包子[%s]做好了' %i)
        r=c.send(i)
        print('厨师:包子被取走了，状态码为%s' %r)
    c.close()
producer(consumer())



#运行结果
厨师:包子[0]做好了
吃货:包子[0]来了，吃包子
厨师:包子被取走了，状态码为200 ok
厨师:包子[1]做好了
吃货:包子[1]来了，吃包子
厨师:包子被取走了，状态码为200 ok
厨师:包子[2]做好了
吃货:包子[2]来了，吃包子
厨师:包子被取走了，状态码为200 ok
厨师:包子[3]做好了
吃货:包子[3]来了，吃包子
厨师:包子被取走了，状态码为200 ok
厨师:包子[4]做好了
吃货:包子[4]来了，吃包子
厨师:包子被取走了，状态码为200 ok

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，
而非线程的抢占式多任务。
```

3.确定性

函数式指数学意义的函数，数学意义的函数，参数传入一定，则结果永远一定
如函数：
```
y=3*x
x=3时，y永远等于9
```

下面的程序演示三辆车比赛。每次移动时间，每辆车可能移动或者不动。每次移动时间程序会打印到目前为止所有车的路径。五次后，比赛结束。
```
from random import random
time=5
car_positions=[1,1,1]

while time:
    #decrease time
    time-=1
    print('')
    for i in range(len(car_positions)):
        #move car
        if random() > 0.3:
            car_positions[i]+=1
        #draw car
        print('-'*car_positions[i])

#代码是命令式的。一个函数式的版本应该是声明式的。应该描述要做什么，而不是怎么做。
from random import random
time=5
car_positions=[1,1,1]
def move_cars():
    for i in range(len(car_positions)):
        if random() > 0.3:
            car_positions[i]+=1

def draw_car(car_position):
    print('-'*car_position)

def draw():
    print('')
    for i in car_positions:
        draw_car(i)

def run_step_of_race():
    global time
    time-=1
    move_cars()

while time:
    run_step_of_race()
    draw()
```

```
#移除状态，转化成函数式

from random import random

def move_cars(car_positions):
    return map(lambda x: x + 1 if random() > 0.3 else x,
               car_positions)

def output_car(car_position):
    return '-' * car_position

def run_step_of_race(state):
    return {'time': state['time'] - 1,
            'car_positions': move_cars(state['car_positions'])}

def draw(state):
    print ''
    print 'n'.join(map(output_car, state['car_positions']))

def race(state):
    draw(state)
    if state['time']:
        race(run_step_of_race(state))

race({'time': 5,
      'car_positions': [1, 1, 1]})
```

# 二：面向过程

找到解决问题的入口，按照一个固定的流程去模拟解决问题的流程

1.搜索目标，用户输入（配偶要求），按找要求到数据结构（字典）内检索合适的人物
2.表白，表白成功进入3，否则进入2
3.恋爱，恋爱成功进入4，否则返回1
4.见家长，家长同意进入5，家长说她是你失散多年的妹妹，返回1
5.结婚


违反开放封闭（OCP)原则，如果有一天需要加入一种Monthly类型，无疑需要修改这个方法；
这样的代码风格会让接下来的开发者不假思索的进行延续，比方说需要根据不同的活动类型延期活动；
这样的代格违反了DRY原则，相同的代码框架却无法重用。

# 三：面向对象：
人:
属性：身高，体重，颜值，财富，学历，性取向

方法：
吃饭，说话，睡觉，表白，结婚

恋爱系统：
属性：