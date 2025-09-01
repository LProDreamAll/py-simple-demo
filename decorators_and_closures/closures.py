import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT): # clock是参数化装饰器的工厂函数
    def decorate(func):     # 真正的装饰器 
        def clocked(*_args):  # 包装被装饰的函数 
            t0 = time.perf_counter()
            print(type(_args))
            _result = func(*_args)  # 调用被装饰的函数
            elapsed = time.perf_counter() - t0
            name = func.__name__
            args = ', '.join(repr(arg) for arg in _args) 
            result = repr(_result)  
            print(fmt.format(**locals()))
            return _result

        return clocked 

    return decorate
@clock('{name}({args}) dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    return 1 if n < 2 else n*factorial(n-1)    
# 一个计算累计平均值的高阶函数，所有值存储在历史数列series中
def make_averager():
    series = []    
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    
    return averager

if __name__ == '__main__':
    # avg = make_averager()
    # print(avg(10))
    # print(avg(11))
    # print(avg(12))
    for i in range(3):
        snooze(.123)


