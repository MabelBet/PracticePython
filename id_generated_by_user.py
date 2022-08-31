def id_generated_by_user():
    import random
    import string

    num_ids = int(input("Ingrese el número de códigos que se van a generar: "))
    length_ids = int(input("Ingrese la cantidad de caracteres que va a tener cada ID: "))
    count = 0

    while count < num_ids:
        random_id = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(length_ids)])
        count = count + 1
        print(random_id)
    return random_id
id_generated_by_user()