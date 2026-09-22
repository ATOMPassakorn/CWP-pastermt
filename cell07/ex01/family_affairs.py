def find_the_redheads(persons):
    family = []
    for name, color in persons.items():
        if color == "red":
            family.append(f"{name}")
    return family

dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))