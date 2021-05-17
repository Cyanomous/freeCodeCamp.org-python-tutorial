import timeit
x=1
xyz=1


start_time = timeit.default_timer()
for i in range(1,1000000):
    if x==1:
        print("message")
elapsed = timeit.default_timer() - start_time


start_time2 = timeit.default_timer()
for i in range(1,1000000):
    if xyz==1:
        print("message")

elapsed2 = timeit.default_timer() - start_time2

print("small variable printing = ",str(elapsed),"big variable printing = "+str(elapsed2))