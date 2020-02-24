import sys

PRINT_BEEJ = 1
HALT = 2


memory = [
    PRINT_BEEJ,
    PRINT_BEEJ,
    PRINT_BEEJ,
    PRINT_BEEJ,
    HALT
]


pc = 0

while True:
    command = memory[pc]

    if command == PRINT_BEEJ:
        print("BEEJ!")
        pc += 1
    elif command == HALT:
        sys.exit(1)
    else:
        print("I did not understand that command.")