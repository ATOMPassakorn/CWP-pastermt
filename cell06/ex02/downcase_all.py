import sys

def downcase_it(txt):
    return(txt.lower())

parameter = len(sys.argv)-1
if parameter >= 1:
    for i in sys.argv[1::]:
        print(downcase_it(i))
else:
    print("none")