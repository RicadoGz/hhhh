from greenlet import greenlet
def fun1():
    print("fuck")
    gr2.switch()
    print("and")
    gr2.switch()
def fun2():
    print("wjj")
    gr1.switch()
    print("tx")

gr1=greenlet(fun1)
gr2=greenlet(fun2)
gr1.switch()