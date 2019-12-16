class Computer(object):
    def __init__(self, tape):
        self.sp = 0
        self.tape = tape
        self.tapeBackup = tape
        for x in range(len(self.tape)):
            self.tape[x] = int(self.tape[x])

    def print(self):
        print(self.tape)

    def len(self):
        return len(self.tape)

    def reset(self):
        self.tape = self.tapeBackup
        self.sp = 0

    def read(self, index):
        return self.tape[index]

    def write(self, index, val):
        self.tape[index] = val

    def execute(self):
        opcode = self.read(self.sp)
        if opcode == 1:
            self.add()
        elif opcode == 2:
            self.mult()
        elif opcode == 99:
            print("Halt!")

    def add(self):
        arg1 = self.read(self.sp + 1)
        arg2 = self.read(self.sp + 2)
        arg3 = self.read(self.sp + 3)
        self.tape[arg3] = self.tape[arg1] + self.tape[arg2]
        self.sp += 4

    def mult(self):
        arg1 = self.read(self.sp + 1)
        arg2 = self.read(self.sp + 2)
        arg3 = self.read(self.sp + 3)
        self.tape[arg3] = self.tape[arg1] * self.tape[arg2]
        self.sp += 4

    def input():
        arg1 = self.read(self.sp + 1)
        arg2 = int(input('> '))
        self.tape[arg1] = arg2

    def output():
        arg1 = self.read(self.sp + 1)
        print(self.tape[arg1])

    def run(self):
        while True:
            opcode = self.read(self.sp)
            if opcode == 1:
                self.add()
            elif opcode == 2:
                self.mult()
            elif opcode == 99:
                break
