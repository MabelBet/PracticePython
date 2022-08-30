#Asabeneh_30_Days_Of_Python
#Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():    
    import random
    list = []
    for i in range(0,255):
        list.append(i)

    random_id = random.choices(list, k=3)
    return(random_id)
print(rgb_color_gen())