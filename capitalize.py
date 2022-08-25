def capitalize_list_items(default_list = []): #Define function
    presidente = []                             #Create empty list
    presidente.append(default_list)             #Add parameters to a empty list
    nombre_presidente = " ".join(presidente)    #Turn list into a string
    name_capitalize = nombre_presidente.capitalize() #Capitalize string
    new_list = name_capitalize.split()          #Turn string into a list
    return new_list
print(capitalize_list_items("i am learning python"))
