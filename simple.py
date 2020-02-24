import sys

PRINT_BEEJ = 1
HALT = 2
PRINT_NUM = 3


memory = [
    PRINT_BEEJ,
    PRINT_NUM,
    1,
    PRINT_NUM,
    12,
    PRINT_BEEJ,
    PRINT_NUM,
    37,
    HALT
]


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
    else:
        print("I did not understand that command.")
        sys.exit(1)