import sys

program = list(map(int, sys.stdin.read().strip().split(',')))
ip = 0

if len(sys.argv) > 1 and sys.argv[1] == 'prod': 
    program[1] = 12
    program[2] = 2

while True: 
    opcode = program[ip]

    if opcode == 99: 
        print(program)
        sys.exit()
    elif opcode == 1:
        t1pos, t2pos, outpos = program[ip+1:ip+4]
        program[outpos] = program[t1pos] + program[t2pos]
        ip += 4
    elif opcode == 2:
        t1pos, t2pos, outpos = program[ip+1:ip+4]
        program[outpos] = program[t1pos] * program[t2pos]
        ip += 4
    else: 
        print("Error at ip", ip)
        sys.exit(1)

# 9581917
