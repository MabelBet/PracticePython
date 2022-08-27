def add_item(total_university, another_university):
    universities = []
    universities.append(total_university)
    universities.append(another_university)
    definetly_list = total_university + another_university
    print(definetly_list)
    return universities
print(add_item(["Externado", "Andes", "Rosario"], "Javeriana"))

#Its possible to get better and returns just one list