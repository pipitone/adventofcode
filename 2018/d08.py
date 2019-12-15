import sys
license = list(map(int, sys.stdin.read().strip().split(" ")))

metadata_total = 0

def parse_node(license):
    global metadata_total 

    num_children = license.pop(0)
    num_meta = license.pop(0)
    children = []
    metadata = []
    value = 0
    for i in range(num_children):
        children.append(parse_node(license))
    for i in range(num_meta): 
        metadata.append(license.pop(0))
    
    metadata_total += sum(metadata)

    if not children: 
        value = sum(metadata)
    else: 
        for i in metadata: 
            if i > 0 and i <= num_children:
                value += children[i-1][2] # 3rd = value
    return (children, metadata, value)

root = parse_node(license)

# part 1
print(metadata_total)
# 46578

# part 2
print(root[2])
# 31251
