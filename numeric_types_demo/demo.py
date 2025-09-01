"""
str 类型
"""


def main() -> None:
    print("gg" in "eggs")


def lists_demo():
    lists = [[]] * 3 # 所有三个元素都是对这个单个空列表的引用。修改列表的任何元素都会修改此单个列表
    print(lists)
    lists[0].append(1)
    print(lists)
    lists = [[] for i in range(3)] # 每个元素都是一个独立的空列表
    print(lists)
    lists[0].append(0)
    print(lists)
    lists[1].append(1)
    print(lists)


if __name__ == "__main__":
    # lists_demo()
    import sys
    print(sys.getfilesystemencoding() )
    import threading.local as local
    mydata = local()
