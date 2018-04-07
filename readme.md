作用域
    默认对不可变全局变量只读,对arr可变全局变量可变
    global实现对不可变全局变量
匿名函数
    1,单独使用要给取名
    2,处理逻辑简单的: 加减乘除/取余/arr的pop等

嵌套:

递归
    1,调用自己
    2,结束条件
    3,每次数据量减少: 减法 除法 arr的pop.

    尾调用
    尾递归(优化)

高阶函数:
    1,参数是函数
    2,返回值是函数
-


装饰器: 高阶函数+函数嵌套+闭包
    1,不改源码
    2,调用方式不变

序列: str tuple list


map
    一个序列每项+1   -->for
    10000个序列每项+1-->函数
    加减乘除/取余/arr的pop等, 功能写活,传方法+数据 --> map_test(func,arr)
        遍历arr,func作用于每项
        返回新序列,res
    lambda简化func
    map(func,arr)
        遍历arr,func作用于每项
        返回新序列,res
    用途: 对arr的每项操作: 加减乘除/取余/arr的pop,str的upper等
-
filter:
    过滤1个序列以mao开头的项    -->for
    过滤10000个序列以mao开头的项-->函数
    过滤以kk结尾的              -->filter_test(func,arr)
        1,遍历arr,func作用与每项
        2,返回新序列,res
    lambda简化func
    map(func,arr)
        1,遍历arr,func作用与每项
        2,返回新序列,res
    用途: 过滤序列中一些满足条件的项, 如以..开头,结尾,包含...关键字.
-
reduce:
    将1个序列每项求和    -->for
    将10000个序列每项求和-->函数
    将列表元素相乘       -->reduce_test(func,arr) http://www.cnblogs.com/iiiiiher/diary/2018/04/06/8729213.html
    lambda简化func
    map(func,arr,base)
    用途: 合并序列.



函数式编程(erlang): 编程函数+数学意义上的函数

无赋值,可读性差
无循环,所有循环依赖递归实现

y = 2*x+1
def add_2(x):
    return 2*x+1


对象:
    特征
    动作

类:
    