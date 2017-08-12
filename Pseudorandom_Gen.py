import matplotlib.pyplot as plt

#XOR function
def XOR(a, b):
    if (a + b == 1):
        return 1
    else:
        return 0

#OR function
def OR(a, b):
    if (a + b == 0):
        return 0
    else:
        return 1

#NOT function
def NOT(a):
    if a == 0:
        p = 1
    if a == 1:
        p = 0
    return p

#Shift Right function
def ShiftR(a):
    i = len(a) - 1
    while ( i > 0):
        a[i] = a[i - 1]
        i -= 1
    a[0] = 0
    return a

#Bin To Dec Function
def BinToDec(bin_list):
    dec = 0
    p = 0
    i = len(bin_list) - 1
    while (i >= 0):
        dec += bin_list[i] * pow(2, p)
        p += 1
        i -= 1
    return dec

i = 0
x = []
while (i < 16):
    x.append(0)
    i += 1
x[0] = 1

randlist = []
stop_val = 50
i = 0
while (i < stop_val):
    #randlist.append(BinToDec(x))
    print(x, BinToDec(x))
    x = ShiftR(x)
    x[0] = NOT ( XOR( x[len(x) - 1], x[len(x) - 2] ) )
    i += 1

#plt.hist(randlist, bins = 10, normed = True)