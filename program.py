def add_random_list (list=[]):
    import random
    for i in range (0, random.randrange(4,20,2)):
        list.append(random.randint(0,100))
    print("Ваш список:", list, sep="\n")
    print("\n")
    return list

def razdel (list, list_=[]):
    for i in range (len(list)//2):
        list_.append(list.pop(0))
    return list_ , list

def reverse (list_, list):
    list.reverse()
    for i in range (0,len(list_)-1):
        list.insert(0, list_[i])
    return list


list=add_random_list()
x=razdel(list)
list_=x[0]
list=x[1]
list=reverse(list_, list)

print("Отсортированный список:",list, sep="\n")
