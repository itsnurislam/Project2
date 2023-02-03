year = int(input("Write the year: "))

def Calc(x):
    d = 0
    for i in range(x+1):
        if i<10:
            d = d + i
        else:
            hh = str(i)
            h = list(hh)
            d = d + int(h[0]) + int(h[1])
    return d

try:
    if(year%4==0):
        print("Leap year")
        b = Calc(31) * 7 + Calc(30) * 4 + Calc(29)
        print("Sum: ", b)
    else:
        print("Non-Leap year")
        b = Calc(31) * 7 + Calc(30) * 4  + Calc(28)
        print("Sum: ", b)
except:
    print("Write the correct data")


