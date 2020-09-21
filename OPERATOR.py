#self-dev operators finder Algorithm
#this program will ask you for the total number of the numbers you will enter later
#then it'll ask you for the result that equations using these numbers are able to give using all sets possible of operators in these equations
#you can choose whether the repeat a used a number in an equation or not to
#e.g: you enter 5,2,3,3 and the result = 27
#one of the generated equations would be 5*2*3-3 which equals 27
#but it'll generate all of the equations possible as well
#this program allows to solve more than a single riddle then to find the common solutions among all of the entered solutions

import random,math,copy

def main():
    print("OPERATOR STARTED.")
    full = []
    noNumbersIn = []
    finale = []
    print("do you want the solutions of only one riddle or to find the similar solutions for multiple riddles?")
    print("(O)nly one or (M)ultiple?")
    res = input(">> ")
    while res.lower() != "o" and res.lower() != "m":
        print("re-enter please.")
        res = input(">> ")
    if res == "o":
        operator()
    else:
        print("enter how many riddles do you want to solve?")
        numb = int(input(">> "))
        for i in range(numb):
            o = operator()
            full.append(o)
        print("do you want find common solutions?")
        print("(Y)es or (N)o ?")
        ress = input(">> ")
        while ress.lower() != 'y' and ress.lower() != 'n':
            print("re-enter please")
            print(">> ")
        if ress.lower() == 'n':
            print( ":3")
        else:
            noNumbersIn = OPOPDeleter(full)
            finale = commonWealthButNotTheRussianOne(noNumbersIn)
    print(noNumbersIn)
    print(finale)
    #print("%s common solutions found"%len(finale))
    #for i in range(len(finale)):
    #   print("common solution %s : %s" %(i+1,finale[i]))
        
def operator():
    numbOfNumbs = int(input("enter the number of the numbers used in the riddle : "))
    List = fillTheList(numbOfNumbs)
    result = int(input("enter the result : "))
    print("do you want to you generate equations with repeating numbers or using the number only once in the equation?")
    print("(R)epeated or (N)o :3 ?")
    ress = input(">> ")
    while ress.lower() != "r" and ress.lower() != "n":
        print("re-enter please")
        ress = input(">> ")
    if ress == "r":        
        print("number of equations possible : %s"%totalNumbOfEquationswithRep(List))
        print("List : %s"%List)
        equation = equationsRep(List)
        solution = solutions(equation,result)
        print("%s solutions found"%len(solution))
        print("enter (A) to show all of the equations and (S) to show solutions and (N)one to show nothing")
        response = input(">> ")
        while response.lower() != 'a' and response.lower() != 's' and response.lower() != 'n':
            print("re-enter your response please")
            response = input(">> ")
        if response.lower() == 'a':
            for k,v in equation.items():
                print("equation : %s , result = %s"%(k,v))
        elif response.lower() == 's':
            for k in solution:
                print("equation : %s"%k)
        else:
            print(';')
        
        print("             *******************************               ")
    else:
        print("number of equations possible : %s"%totalNumbOfEquationswithoutRep(List))
        print("List : %s"%List)
        equation = equationswithoutRep(List)
        solution = solutions(equation,result)
        print("%s solutions found"%len(solution))
        print("enter (A) to show all of the equations and (S) to show solutions and (N)one to show nothing")
        response = input(">> ")
        while response.lower() != 'a' and response.lower() != 's' and response.lower() != 'n':
            print("re-enter your response please")
            response = input(">> ")
        if response.lower() == 'a':
            for k,v in equation.items():
                print("equation : %s , result = %s"%(k,v))
        elif response.lower() == 's':
            for k in solution:
                print("equation : %s"%k)
        else:
            print(';')
        
        print("             *******************************               ")
    return solution
def fillTheList(Numbs):
    listOfNumbs = []
    for i in range(Numbs):
        n = input("enter the number(%s) : "%(i+1))
        listOfNumbs.append(n)
    return listOfNumbs
    
def totalNumbOfEquationswithRep(List):
    return (math.pow(len(List),len(List)) * math.pow(4,len(List)-1))
def totalNumbOfEquationswithoutRep(List):
    return math.factorial(len(List )) * math.pow(4,len(List)-1)

def equationsRep(List):
    d = {}
    totalnumbOfcalcs = totalNumbOfEquationswithRep(List)
    ll = len(List)
    operations = ['+','-','*','/']
    print("generating equations...")
    while len(d) != totalnumbOfcalcs:
        operation = random.choice(List)
        for i in range(ll-1):
            operation += random.choice(operations) + random.choice(List)
        if operation not in d:
            if "/0" in operation:
                d[operation] = "impossible"    
            else:
                d[operation] = eval(operation)
    return d
def equationswithoutRep(List):
    d = {}
    totalnumbOfcalcs = totalNumbOfEquationswithoutRep(List)
    ll = len(List)
    operations = ['+','-','*','/']
    print("generating equations...")
    while len(d) != totalnumbOfcalcs:
        List0 = copy.deepcopy(List)
        ll0 = len(List0)
        operation = random.choice(List0)
        List0.remove(operation)
        while List0 != []:
            randomChoice = random.choice(List0)
            operation += random.choice(operations) + randomChoice
            List0.remove(randomChoice)
        if operation not in d:
            if "/0" in operation:
                d[operation] = "impossible"    
            else:
                d[operation] = eval(operation)
    return d

    
def solutions(d,result):
    finalList = []
    for k,v in d.items():
        if v == result:
            finalList.append(k)
    return finalList

def OPOPDeleter(L0):
    operators = ['+','-','*','/']
    for item in L0:
        for equation in item:
            equation = list(equation)
            while ('0' in equation) or ('1' in equation) or ('2' in equation) or ('3' in equation) or ('4' in equation) or ('5' in equation) or ('6' in equation) or ('7' in equation) or ('8' in equation) or ('9' in equation):
                for charr in equation:
                    if charr not in operators:
                        equation. remove(charr)
            equation = ''.join(equation)
            print(equation)
    print(L0)
    return L0

def commonWealthButNotTheRussianOne(L0):
    common = []
    hey = 5
    short = shortestLenList(L0)
    for item in L0[short]:
        b = True
        for indx in range(len(L0)):
            if indx == short:
                hey = 0
            else:
                if item not in L0[indx]:
                    b = False
        if b == True:
            common.append(item)
    return common


def shortestLenList(L0):
    short = 0
    shortest = len(L0[0])
    for item in range(1,len(L0)):
        if len(L0[item]) > shortest:
            short = item
    return short


if __name__ == '__main__':
    main()











            
