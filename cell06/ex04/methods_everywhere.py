import sys

def shrink(txt):
    return txt[0:8]

def enlarge(txt):
    while len(txt) < 8:
        txt+="Z"
    return txt

parameter = len(sys.argv)-1
if parameter >= 1:
    for i in sys.argv[1::]:
        if len(i) < 8:
            i = enlarge(i)
        else:
            i = shrink(i)
        print(i)
else:
    print("none")