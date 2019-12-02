import sys


def run(program): 
    ip = 0
    while True: 
        opcode = program[ip]

        if opcode == 99: 
            return program[0] 
        elif opcode == 1:
            t1pos, t2pos, outpos = program[ip+1:ip+4]
            program[outpos] = program[t1pos] + program[t2pos]
            ip += 4
        elif opcode == 2:
            t1pos, t2pos, outpos = program[ip+1:ip+4]
            program[outpos] = program[t1pos] * program[t2pos]
            ip += 4
        else: 
            raise Exception("Error at ip", ip)


orig_program = list(map(int, sys.stdin.read().strip().split(',')))

for noun in range(0,100):
    for verb in range(0, 100): 
        program = orig_program[:]
        program[1] = noun
        program[2] = verb
        result = run(program)
        if result == 19690720:
            print("noun", noun)
            print("verb", verb)
            sys.exit()
# noun: 25
# verb: 05
