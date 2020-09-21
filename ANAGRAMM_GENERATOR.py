#SIMPLE ANNAGRAMS GENERATOR

import random ,math


def Annagrammer(text): #calculate annagrams...
    conv = list(text)
    co = []
    total_anns = math.factorial(len(conv))
    repeat = divide_on(conv)
    sett = total_anns // repeat
    print("Anagramms to generate : %s" %(sett) )
    print("generating right now...\n")
    while len(co) != sett:
        random.shuffle(conv)
        back = ''.join(conv)
        if back not in co:
            co.append(back)
    for a in co:
        print(a)

def divide_on(list):
    numb = 1
    deja = []
    for item in list:
        if list.count(item) > 1 and item not in deja:
            numb *= list.count(item)
            deja.append(item)
    return numb

def main():
    init = input("enter text : ")
    Annagrammer(init)


    
if __name__ == '__main__':
    main()



