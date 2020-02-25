import sys

PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3
SAVE = 4 #saves value to a register
PRINT_REGISTER = 5 # prints register
ADD = 6 #adds two registers, stores result in first


memory = [
    PRINT_BEEJ,
    SAVE,
    65,
    2,
    SAVE,
    20,
    3,
    ADD,
    2,
    3,
    PRINT_REGISTER,
    2,
    HALT
]

#gives you an array of 8 zeroes
register = [0] * 8
# 8 is standard

# a register is like memory, only super-fast
pc = 0

while True:
    command = memory[pc]

    if command == PRINT_BEEJ:
        print("BEEJ!")
        pc += 1
    elif command == PRINT_NUM:
        num = memory[pc + 1]
        print(num)
        pc += 1
    elif command == HALT:
        sys.exit(0)
    elif command == SAVE:
        num = memory[pc + 1]
        reg = memory[pc + 2]
        register[reg] = num
        pc += 3
        #what does that ^ register[reg] actually refer to???
    elif command == ADD:
        reg_a = memory[pc + 1]
        reg_b = memory[pc + 2]
        register[reg_a] += register[reg_b]
        pc += 3
    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(register[reg])
        pc += 2
    else:
        print("I did not understand that command.")
        sys.exit(1)

#what do compilers have to do with anything?