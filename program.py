def add_random_list (list=[]):
    import random
    for i in range (0, random.randrange(2,20,2)):
        list.append(random.randint(0,100))
    print("Ваш список:", list, sep="\n")
    print("\n")
    return list

def razdel (list, list_=[]):
    for i in range (len(list)//2):
        list_.append(list.pop(0))
    print(list_, list, sep="\n")
    return list_ , list

list=add_random_list()
razdel(list)
