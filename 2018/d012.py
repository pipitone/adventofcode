import sys
state = ""
rules = set()
for line in sys.stdin.readlines(): 
    line = line.strip()
    if "=>" in line and line.endswith("#"):
        rules.add(line.split(" => ")[0])
    elif line.startswith("initial"):
        _, state = line.split(": ")

state = list(state)
print(0, ''.join(state))
for i in range(1, 21):
    # grow the state
    try: 
        state = ["."] * max(2-state.index("#"),0) + state
        state = state + ["."] * max(2-state[::-1].index("#"),0)
    except ValueError:
        pass
    print(i, ''.join(state))
    newstate = state[:]
    for j in range(2,len(state)-3):
        context = ''.join(state[j-2:j+3])
        if context in rules:
            print(context)
            newstate[j] = "#"
        else:
            newstate[j] = "."
    state = newstate
    print(i, ''.join(state))
