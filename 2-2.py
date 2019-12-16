from sys import argv
import intCode
import sys

tape = []
out = []

if "-l" in argv:
    tape = []
    tape = open(argv[1]).read().strip().split(',') #opens the file, and formats it into a list

comp = intCode.Computer(tape)

for noun in range(0,99):
    for verb in range(0,99):
        comp.write(1, noun)
        comp.write(2, verb)
        comp.print()
        if comp.read(0) == 19690720:
            out.append(noun, ", ", verb)
            print("Match found!")
        else:
            print("Not a match")
        comp.reset()

print(out)
