# Little machine emulator
Very simple interpreter for a made up assembly language

It uses an instruction set inspired by (but not too similar to) the game "TIS-100".
The starting point for this interpreter is meant to be as simple as possible while not making it too hard to make a program do something interesting.

### Instruction set

Key: `D` is the destination variable, `S1` and `S2` are source variable, `I1` and `I2` are immediate (integer) values. `S1`/`I1` means a variable or an immediate value can be used in this place.

#### Input/Output
Syntax              | Description
---                 | ---
`INP D`             | input integer as text from terminal
`OUT S`             | output integer as text to terminal

#### Arithmetic
Syntax              | Description | Equivalent code
--------------------|--------|---------
`MOV D S/I`         | Copy source value to D                                                                   | `D` = `S1`/`I1`
`ADD D S1/I1 S2/I2` | Add source values together, put the result in the desitantion                            | `D` = `S1`/`I1` +  `S2`/`I2`        
`SUB D S1/I1 S2/I2` | Subtract source 2 from source 1, put the result in the desitantion                       | `D` = `S1`/`I1` -  `S2`/`I2`        
`MUL D S1/I1 S2/I2` | Multiply source values together, put the result in the desitantion                       | `D` = `S1`/`I1` *  `S2`/`I2`        
`DIV D S1/I1 S2/I2` | Divide source 1 by source 2, round down to an integer, put the result in the desitantion | `D` = `S1`/`I1` // `S2`/`I2`       
`MOD D S1/I1 S2/I2` | Modulo division of source 1 by source 2, put the result in the desitantion               | `D` = `S1`/`I1` %  `S2`/`I2`        

Example: `SUB B A 10` is B = A - 10 and `SUB B 10 A` is B = 10 - A

#### Flow Control
Syntax              | Description                             | Equivalent code
---                 | ---                                     | ---
`label:`            | define a label at the begging of a line |
`JMP label`         | Jump to label                           | goto label           
`JEZ S label`       | Jump to label if S is equal to zero     | if S == 0 goto label                                 
`JNZ S label`       | Jump to label if S is not equal to zero | if S != 0 goto label                                     
`JGZ S label`       | Jump to label if S is greater than zero | if S > 0 goto label                                     
`JLZ S label`       | Jump to label if S is less than zero    | if S < 0 goto label                                  

#### Comments
`#comment` at the end of a line

### Example program - Print 10 Fibbonacci numbers

Python:
```py
a=1
b=1
for i in range(0, 10, 2):
    print(a)
    a+=b
    print(b)
    b+=a
```


Equivalent assembly code:
```
MOV A 1 #set initial values
MOV B 1

MOV i 10 #set counter
loop:
    OUT A
    ADD A A B
    OUT B
    ADD B B A

    SUB i i 2 #decrement counter
    JGZ i loop
```

### Notes:

 - The only data type is integer
 - You have unlimited named variables (making it not quite an assembly language that can be directly mapped to a real machine with a finite register file)
 - Variables for each instructions are written destination first, followed by the source variable(s), (like in "Intel assembly syntax").
 - A variable is defined when it appears as the destination of instructions (in the case it hasn't been defined before)

No syntax or other error messages implemented for now, like when a variable is used before being defined/set to a value. Python just gives an exception instead.

### Output
Output of the 3 included example programs
```
running file sourceFibbonacci.txt
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 
Program END
running file sourceCollatz.txt
19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1, 
Program END
running file sourcePrimes.txt
1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
Program END
```