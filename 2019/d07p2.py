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

def run(program, inputs = [], ip = 0): 
    """ return (program, outputs, ip, hasHalted) """
    inputs = inputs[:]
    outputs = []
    while True: 
        program = list(map(str, program)) # a hack unworthy of a true computer scientist
        modes, opcode = program[ip][:-2], int(program[ip][-2:])
        debug("opcode", opcode, "modes", modes)

        if opcode == 99: 
            return (program, outputs, ip, True)
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
            if not inputs:
                return (program, [], ip, False)
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
            return (program, outputs, ip, False)
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

def amp(program, a, b, c, d, e):
    # init
    a_program, a_out, a_ip, a_halted = run(program[:], inputs=[a])
    b_program, b_out, b_ip, b_halted = run(program[:], inputs=[b])
    c_program, c_out, c_ip, c_halted = run(program[:], inputs=[c])
    d_program, d_out, d_ip, d_halted = run(program[:], inputs=[d])
    e_program, e_out, e_ip, e_halted = run(program[:], inputs=[e])

    # feedback loop
    e_out = [0]
    e_last = [0]
    while not e_halted:
        e_last = e_out
        a_program, a_out, a_ip, a_halted = run(a_program, inputs=e_out, ip=a_ip)
        b_program, b_out, b_ip, b_halted = run(b_program, inputs=a_out, ip=b_ip)
        c_program, c_out, c_ip, c_halted = run(c_program, inputs=b_out, ip=c_ip)
        d_program, d_out, d_ip, d_halted = run(d_program, inputs=c_out, ip=d_ip)
        e_program, e_out, e_ip, e_halted = run(e_program, inputs=d_out, ip=e_ip)
    return e_last

for line in open(sys.argv[1]): 
    if line.strip().startswith("#"):
        print(line)
    elif line.strip() == '':
        continue
    else: 
        program = line.strip().split(',')
        thrusts = {}
        for params in itertools.permutations(range(5,10)):
            output, = amp(program, *params)
            thrusts[output] = params

        max_thrusts = max(thrusts.keys())
        print(max_thrusts, thrusts[max_thrusts])
