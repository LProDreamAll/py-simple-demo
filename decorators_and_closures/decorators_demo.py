
def deco(func):
    def inner():
        func()
        print('running inner')
    return inner

@deco
def target():
    print('running target()')
    
    
if __name__ == '__main__':
    target()
