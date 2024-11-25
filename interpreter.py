sourceFibbonacci = '''
MOV A 1
MOV B 1
MOV i 10 #print 10 Fibbonaci numbers
loop:
    OUT A
    ADD A A B
    OUT B
    ADD B B A

    SUB i i 2
    JGZ i loop
'''

#generate the Collatz sequence (also known as the 3n+1 sequence)
sourceCollatz = '''
MOV n 31 #initial value

loop:
    MOD t n 2 #t (temporary value) is 1 if n is odd, 0 if even
    JEZ t endif #if n is odd, n = 3n + 1
        MUL n n 3 
        ADD n n 1
        OUT n
    endif:

    #n is always divisible by 2 after an 3n+1 step, so divide it
    DIV n n 2
    OUT n

SUB t n 1 #if n > 1, repeat
JGZ t loop
'''

#Python version:
'''
for i in range(1, 100):
    prime = True
    for divisor in range(2, i):
        if i % divisor == 0:
            prime = False
    if prime:
        print(i)
'''

sourcePrimes = '''
MOV i 1
loopMain:
    MOV divisor 2
    loopDivisor:
        MOD t i divisor
        JEZ t notPrime

        ADD divisor divisor 1
    SUB t i divisor
    JGZ t loopDivisor
    OUT i #output number if no the divisor loop completed without finding a divisor

    notPrime:
    ADD i i 1
SUB t 100 i
JGZ t loopMain
'''

#source = sourceFibbonacci
#source = sourceCollatz
source = sourcePrimes

var = {} #variables

def isInt(s: str) -> bool:
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

def getValue(s: str) -> int:
    if isInt(s):
        return int(s)
    else:
        return var[s]

lines = source.split("\n")
lineN = 0

#remove comments
for lineN, line in enumerate(lines):
    lines[lineN] = line.split("#")[0]

#remove blank lines
lines = [line for line in lines if len(line.split()) > 0]

#get all labels
labels = {}
for lineN, line in enumerate(lines):
    tokens = line.split()
    #if there is a label on this line, note it down in the 'labels' loop up table
    #and strip it out from the code
    if len(tokens) > 0 and tokens[0][-1] == ":":
        labelName = tokens[0][:-1]
        labels[labelName] = lineN

        lines[lineN] = " ".join(tokens[1:]) #remove label from code



#run the program
lineN = 0
while lineN < len(lines):
    line = lines[lineN]
    tokens = line.split()
    if len(tokens) == 0:
        lineN += 1
        continue

    instr = tokens[0]
    args = tokens[1:]
    nextLineN = lineN + 1

    if instr == "INP":   # INP D - input from terminal
        D = args[0]
        var[D] = int(input(">"))
    elif instr == "OUT": # OUT S - output to terminal
        Sval = getValue(args[0])
        print(Sval)
    elif instr == "MOV": # MOV D S/I - D = S/I
        D = args[0]
        Sval = getValue(args[1])
        var[D] = Sval
    elif instr == "ADD": # ADD D S1/I1 S2/I2 - D = S1/I1 + S2/I2
        D = args[0]
        S1val = getValue(args[1])
        S2val = getValue(args[2])
        var[D] = S1val + S2val
    elif instr == "SUB": # SUB D S1/I1 S2/I2 - D = S1/I1 - S2/I2
        D = args[0]
        S1val = getValue(args[1])
        S2val = getValue(args[2])
        var[D] = S1val - S2val
    elif instr == "MUL": # MUL D S1/I1 S2/I2 - D = S1/I1 * S2/I2
        D = args[0]
        S1val = getValue(args[1])
        S2val = getValue(args[2])
        var[D] = S1val * S2val
    elif instr == "DIV": # DIV D S1/I1 S2/I2 - D = S1/I1 // S2/I2
        D = args[0]
        S1val = getValue(args[1])
        S2val = getValue(args[2])
        var[D] = S1val // S2val
    elif instr == "MOD": # MOD D S1/I1 S2/I2 - D = S1/I1 % S2/I2
        D = args[0]
        S1val = getValue(args[1])
        S2val = getValue(args[2])
        var[D] = S1val % S2val
    elif instr == "JMP": # JMP label - Jump to label
        nextLineN = labels[args[0]]
    elif instr == "JEZ": # JEZ S label - Jump to label if S is equal to zero
        Sval = getValue(args[0])
        if Sval == 0:
            nextLineN = labels[args[1]]
    elif instr == "JNZ": # JNZ S label - Jump to label if S is not equal to zero
        Sval = getValue(args[0])
        if Sval != 0:
            nextLineN = labels[args[1]]
    elif instr == "JGZ": # JGZ S label - Jump to label if S is greater than zero
        Sval = getValue(args[0])
        if Sval > 0:
            nextLineN = labels[args[1]]
    elif instr == "JLZ": # JLZ S label - Jump to label if S is less than zero
        Sval = getValue(args[0])
        if Sval < 0:
            nextLineN = labels[args[1]]

    lineN = nextLineN

print("Program END")
