# map(function, iterable)
# 定义处理函数：求平方
from functools import reduce

def square(x):
    return x **2


def map_demo() -> None:
    """Demonstrate map()"""
    numbers = [1, 2, 3, 4, 5]
    result_map = map(square, numbers)
    print(result_map)
    print(list(result_map))
    
def map_demo_lambda() -> None:
    """Demonstrate map()"""
    numbers = [1, 2, 3, 4, 5]
    result_map = map(lambda x: x **2, numbers)
    print(result_map)
    print(list(result_map))
    
    
def map_demo1() -> None:
   words = ["apple", "banana", "cherry"]
   result = map(lambda s: s.upper(), words)
   print(list(result))
def add(x, y):
    return x + y
# reduce(function, iterable[, initial])
def reduce_demo() -> None:
    """Demonstrate reduce()"""
    numbers = [1, 2, 3, 4, 5]
    # 1. 计算列表中所有元素的和
    result_sum = reduce(add, numbers)
    print(result_sum)
    result_reduce = reduce(lambda x, y: x + y, numbers)
    print(result_reduce)
    

    
if __name__ == '__main__':
    # map_demo()
    # map_demo_lambda()
    reduce_demo()