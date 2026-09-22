import sys

parameter = len(sys.argv)-1
list = []
if parameter == 2:
    for i in range(int(sys.argv[1]),int(sys.argv[2])+1) :
        list.append(i)
    print(list)
else:
    print("none")