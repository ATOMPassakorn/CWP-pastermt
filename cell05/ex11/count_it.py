import sys

parameter = len(sys.argv)-1
count = 0
if parameter >= 1:
    print(f"parameters: {parameter}")
    for i in sys.argv[1::]:
        for j in i:
            count+=1
        print(f"{i}: {count}")
        count=0
else:
    print("none")