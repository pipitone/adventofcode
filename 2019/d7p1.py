import sys
import itertools
import pprint
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

def run(program, inputs = []): 
    inputs = inputs[:]
    outputs = []
    ip = 0
    while True: 
        program = list(map(str, program)) # a hack unworthy of a true computer scientist
        modes, opcode = program[ip][:-2], int(program[ip][-2:])
        debug("opcode", opcode, "modes", modes)

        if opcode == 99: 
            return outputs
        elif opcode == 1: # add
            # op arg arg store
            args = get_args(program, program[ip+1:ip+3], modes)
            debug("add", args, "to", program[ip+3])
            program[int(program[ip+3])] = sum(args)
            ip += 4
        elif opcode == 2: # multiply
            # op arg arg store
            args = get_args(program, program[ip+1:ip+3], modes)
            debug("mult", args, "to", program[ip+3])
            program[int(program[ip+3])] = args[0] * args[1]
            ip += 4
        elif opcode == 3: # input
            # op store
            value = int(inputs.pop(0))
            debug("input", value)
            inpos = int(program[ip+1])
            debug("input", value, "to", inpos)
            program[inpos] = value
            ip += 2
        elif opcode == 4: # output
            # op output
            args = get_args(program, [program[ip+1]], modes)
            debug("output",args)
            outputs.append(args[0])
            ip += 2
        elif opcode == 5: # jump-if-true
            # op arg jump
            args = get_args(program, program[ip+1:ip+3], modes)
            debug("jump-if-true", args[0], "to", args[1])
            if args[0] != 0:
                ip = args[1]
            else: 
                ip += 3
        elif opcode == 6: # jump-if-false
            # op arg jump
            args = get_args(program, program[ip+1:ip+3], modes)
            debug("jump-if-false", args[0], "to", args[1])
            if args[0] == 0:
                ip = args[1]
            else: 
                ip += 3
        elif opcode == 7:  # less-than
            # op arg1 arg2 store
            args = get_args(program, program[ip+1:ip+3], modes)
            program[int(program[ip+3])] = int(args[0] < args[1])
            debug("less-than", args[0], "<", args[1], "to", program[ip+3])
            ip += 4
        elif opcode == 8:  # equals
            # op arg1 arg2 store
            args = get_args(program, program[ip+1:ip+3], modes)
            program[int(program[ip+3])] = int(args[0] == args[1])
            debug("equals", args[0], "==", args[1], "to", program[ip+3])
            ip += 4
        else: 
            raise Exception("Error at ip", ip)
        debug("ip", ip, program)

def amp(program, A, B, C, D, E):
    Aout = run(program[:], inputs=[A] + [0])
    Bout = run(program[:], inputs=[B] + Aout)
    Cout = run(program[:], inputs=[C] + Bout)
    Dout = run(program[:], inputs=[D] + Cout)
    Eout = run(program[:], inputs=[E] + Dout)
    return Eout

for line in open(sys.argv[1]): 
    if line.strip().startswith("#"):
        print(line)
    elif line.strip() == '':
        continue
    else: 
        program = line.strip().split(',')
        thrusts = {}
        for params in itertools.permutations(range(5)):
            output, = amp(program, *params)
            thrusts[output] = params

        max_thrusts = max(thrusts.keys())
        print(max_thrusts, thrusts[max_thrusts])
