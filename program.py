def add_random_list (list=[]):
    import random
    for i in range (0, random.randrange(0,20,2)):
        list.append(random.randint(0,100))
    print("Ваш список:", list, sep="\n")
    print("\n")
    return list

add_random_list()
