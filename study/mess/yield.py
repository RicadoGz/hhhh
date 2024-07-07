def fun1():
    yield "fuck"
    yield from fun2()
    yield "wjj"
def fun2():
    yield "tx"
    yield "and"
f1=fun1()
for i in f1:
    print(i)