def isInt(s: str) -> bool:
    try: 
        int(s)
    except ValueError:
        return False
    else:
        return True

def runFile(fileName, printNewline = False):
    var = {} #dictionary of variable name/value pairs

    def getValue(s: str) -> int:
        if isInt(s):
            return int(s)
        else:
            return var[s]

    with open(fileName, 'r') as file:
        lines = file.readlines()
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
            if printNewline:
                print(Sval)
            else:
                print(Sval, end=", ", flush=True)
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

    print()
    print("Program END")


if __name__ == '__main__':
    files = [
        "sourceFibbonacci.txt",
        "sourceCollatz.txt",
        "sourcePrimes.txt"
    ]

    for file in files:
        print(f"running file {file}")
        runFile(file)