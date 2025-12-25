FindP = False
power = 1
pFinded = False
n = int(input("Enter a number for find factors (N) (***N < 100***): "))
LTN = int(input("Enter random number Less than N : ")) #LTN, L = Less, T = than, N = N 
if LTN > n:
    print(":( Sorry! Your random number is greater than n.")
else:
    print("Finding p...")
    while FindP==False:
            pPower = LTN**power
            print("Testing ", LTN,"^",power,"%",n)
            pAnswer = pPower%n
            if pAnswer == 1:
                FindP = True
            else:
                power = power+1
    print(power)
    power = power/2
    gAO = (LTN**power)+1
    output = gAO%n
    gAOdivi = n
    while pFinded == False:
        output = gAO%gAOdivi
        gAO = gAOdivi
        if output ==0:
            pFinded = True
        else:
            gAOdivi = output
    q = n/gAOdivi
    print("p is ",gAOdivi," and q is ",q)