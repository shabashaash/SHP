from crypto import *
from os import system as execute
from platform import system as os_name

def clear():
    if os_name == "Windows": execute("cls")
    else: execute("clear")

clear()

print("This is the Ultimate Decryptor v1.2.")
thing = []
choice = 0
c = 0
thing.append(input("Input THE THING you wish to decrypt.\nIf it's an integer/binary/string or else just paste it.\nCross you fingers for it not to have any '\\n'.\nTHE THING: "))
clear()

options = '''
    dn) Dec2Nth
    nd) Nth2Dec
    bd) Bin2Dec
    db) Dec2Bin
    dr) Dec2Rus
    rd) Rus2Dec
     c) Chunk by N
     d) Drop element number N
     E) Decode Elias2Dec
     M) Morse decode (00001 -> 1)
     H) Decode Hemming 15/11 to bin
     R) RLE only on array
    oe) Transfer even/odd to 0/1
    sb) Str2bin
     s) Split by "smth"
@@@@@S) Sibirsky Decode (UL triangle) <-- NOT WORKING
   rev) Reverse ( 123 -> 321 )
     j) Join arr elements in str
     b) Revert previous operation
     q) Quit
     p) Print THE THING
    FW) Write THE THING to the file'''

while True:
    clear()

    ####################
    ####### DEBUG ######
    ####################
    
    #print(thing)

    ####################
    ####################

    print("@>>> Oll Korrect.")
    print("@>>> Iteration Num:", c)
    print("@>>> This is your thing:\n\n", thing[c],"\n")
    print("@>>> It's type is", type(thing[c]))
    print("@>>> Length of the thing: ", len(thing[c]) if type(thing[c]) is str else len(thing[c]), len(thing[c][0]))
    print("@>>> What would you like to do?")
    print(options)
    choice = input("@>> Your choice: ")
    if choice == "q":
        clear()
        exit()
    elif choice == "p":
        clear()
        print('START THE THING\n\n')
        print(*thing[c], sep='')
        print('\n\nEND THE THING')
        input("Press Enter")
    elif choice == "b":
        if c:
            c -= 1
            thing.pop()
        else:
            print("No operation to revert!")
            input("Press Enter")
    elif choice == "s":
        by = input("Split by: ")
        thing.append(thing[c].split(by))
        c += 1
    
    elif type(thing[c]) == list:
        new_thing = []
        for i in thing[c]:
            if i != '':
                new_thing.append(i)
        thing[c] = new_thing
        #Remove all ''

        res = []
        if choice == "dn":
            n = input("Nth base: ")
            for z in thing[c]:
                res.append(dec2nth(z, n))
        elif choice == "nd":
            n = input("Nth base: ")
            for z in thing[c]:
                res.append(nth2dec(z, n))
        elif choice == "bd":
            for z in thing[c]:
                res.append(bin2dec(z))
        elif choice == "db":
            for z in thing[c]:
                res.append(dec2bin(z))
        elif choice == "dr":
            for z in thing[c]:
                res.append(dec2rus(z))
        elif choice == "R":
            n = int(input("Start with 0/1: "))
            res = RLE(thing[c], n)
        elif choice == "M":
            for z in thing[c]:
                res.append(binMorse2dec(z))
        elif choice == "rd":
            for z in thing[c]:
                res.append(rus2dec(z))
        elif choice == "oe":
            for z in thing[c]:
                res.append(binMorse2dec(z))
        elif choice == "d":
            n = int(input("Drop N, starting from 1: "))
            res.append(dropEl(thing[c], n + 1))
        elif choice == "c":
            pass
        elif choice == "E":
            for z in thing[c]:
                res.append(elias2dec(z))
        elif choice == "H":
            for z in thing[c]:
                res.append(Hemming15_112bin(z))
        elif choice == "9":
            a = input("1 for: ")
            b = input("and 0 for: LOL don't care")
            for z in thing[c]:
                res.append(str2bin(z, a))
        elif choice == "rev":
            res.append(reverseArray(thing[c]))
        elif choice == "s":
            pass
        elif choice == "j":
            res = "".join(thing[c])
        else:
            print("FATAL ERROR")
            exit()
        c += 1
        thing.append(res)

    elif type(thing[c]) == str:
        if choice == "dn":
            n = input("Nth base: ")
            res = dec2nth(thing[c], n)
        elif choice == "nd":
            n = input("Nth base: ")
            res = nth2dec(thing[c], n)
        elif choice == "bd":
            res = bin2dec(thing[c])
        elif choice == "db":
            res = dec2bin(thing[c])
        elif choice == "dr":
            res = dec2rus(thing[c])
        elif choice == "R":
            res = thing[c]
        elif choice == "S":
            res = sibisky_UL2UR2any(thing[c])
        elif choice == "M":
            res = binMorse2dec(thing[c])
        elif choice == "oe":
            res = OddEven2bin(thing[c])
        elif choice == "rd":
            res = rus2dec(thing[c])
        if choice == "d":
            n = int(input("Drop N, starting from 0: "))
            res = dropEl(thing[c], n)
        elif choice == "c":
            n = input("Num of chunks: ")
            res = list(chunk(thing[c], n))
        elif choice == "E":
            res = elias2dec(thing[c])
        elif choice == "H":
            res = Hemming15_112bin(thing[c])            ###############################
        elif choice == "sb":
            a = input("1 for: ")
            b = input("and 0 for: LOL don't care")
            res = str2bin(thing[c], a)
        elif choice == "split":
            smthn = input("Smnth: ")
            res = choice[c].split(smthn)
        elif choice == "rev":
            res = reverseArray(thing[c])
        elif choice == "j":
            res = "".join(thing[c])
        thing.append(res)
        c += 1












