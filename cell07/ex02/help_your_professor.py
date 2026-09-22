def average(persons):
    sum=0
    person=0
    for name, score in persons.items():
        sum+=int(score)
        person+=1
    ans=sum/person
    return ans

class_3B = {
"marine": 18,
"jean": 15,
"coline": 8,
"luc": 9
}
class_3C = {
"quentin": 17,
"julie": 15,
"marc": 8,
"stephanie": 13
}
print(f"Average for class 3B: {average(class_3B)}.")
print(f"Average for class 3C: {average(class_3C)}.")