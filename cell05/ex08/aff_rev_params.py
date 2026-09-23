import sys

parameter = len(sys.argv)-1
if parameter >= 1:
    for i in sys.argv[:0:-1]:
        print(i)
else:
    print("none")