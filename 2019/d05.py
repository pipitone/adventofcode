import sys
import itertools
DEBUG = False

def debug(*args): 
    if DEBUG: 
        print(*args)

def get_args(program, args, modes):
    mode_args = list(itertools.zip_longest(reversed(modes), args, fillvalue="0"))
    debug("mode,args", mode_args)
    new_args = [int(program[int(arg)]) if mode == "0" else int(arg) for mode, arg in mode_args]
    debug("resolved args", new_args)
    return new_args

def run(program): 
    ip = 0
    while True: 
        program = list(map(str, program)) # a hack unworthy of a true computer scientist
        modes, opcode = program[ip][:-2], int(program[ip][-2:])
        debug("opcode", opcode, "modes", modes)

        if opcode == 99: 
            return program
        elif opcode == 1: # add
            # op arg arg store
            args = get_args(program, program[ip+1:ip+3], modes)
            program[int(program[ip+3])] = sum(args)
            ip += 4
        elif opcode == 2: # multiply
            # op arg arg store
            args = get_args(program, program[ip+1:ip+3], modes)
            program[int(program[ip+3])] = args[0] * args[1]
            ip += 4
        elif opcode == 3: # input
            # op store
            print("Input > ", end="")
            sys.stdout.flush()
            value = int(sys.stdin.readline().strip())
            inpos = int(program[ip+1])
            program[inpos] = value
            ip += 2
        elif opcode == 4: # output
            # op output
            args = get_args(program, [program[ip+1]], modes)
            print("Output >", args[0])
            ip += 2
        elif opcode == 5: # jump-if-true
            # op arg jump
            args = get_args(program, program[ip+1:ip+3], modes)
            if args[0] != 0:
                ip = args[1]
            else: 
                ip += 3
        elif opcode == 6: # jump-if-false
            # op arg jump
            args = get_args(program, program[ip+1:ip+3], modes)
            if args[0] == 0:
                ip = args[1]
            else: 
                ip += 3
        elif opcode == 7:  # less-than
            # op arg1 arg2 store
            args = get_args(program, program[ip+1:ip+3], modes)
            program[int(program[ip+3])] = int(args[0] < args[1])
            ip += 4
        elif opcode == 8:  # equals
            # op arg1 arg2 store
            args = get_args(program, program[ip+1:ip+3], modes)
            program[int(program[ip+3])] = int(args[0] == args[1])
            ip += 4
        else: 
            raise Exception("Error at ip", ip)

for line in open(sys.argv[1]): 
    if line.strip().startswith("#"):
        print(line)
    elif line.strip() == '':
        continue
    else: 
        program = line.strip().split(',')
        debug(program)
        program = run(program)
        debug(program)
