import math 

def huffman(output):
    # output: dictionary of output symbols and their probabilities
    # return: dictionary of output symbols and their huffman codes

    # sort output symbols by probability
    output = sorted(output.items(), key=lambda x: x[1], reverse=True)
    output = dict(output)
    # create a list of nodes
    nodes = []
    for key in output:
        nodes.append([key, output[key]])
    # create a list of codes
    codes = {}
    for key in output:
        codes[key] = ""
    # create a huffman tree
    
    while len(nodes) > 1:
        # sort nodes by probability
        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)
        # combine two nodes with the smallest probabilities
        node1 = nodes.pop()
        node2 = nodes.pop()
        combined_node = [node1[0], node2[0]]
        nodes.append([combined_node, node1[1] + node2[1]])
        print(nodes)
        # update codes
        for symbol in node1[0]:
            codes[symbol] = "0" + codes[symbol]
        for symbol in node2[0]:
            codes[symbol] = "1" + codes[symbol]

    return codes

def print_I_info(output):
    result = "| I | Log |\n"
    for key,value in output.items():
        # do -log2(value )
        result += f"| I<sub>{key}</sub> | {-1*math.log2(value)} |\n"
        
    return result


def print_codes(codes):
    result = "| Symbol | Code |\n"
    for key,value in codes.items():
        result += f"| {key} | {value} |\n"
    return result


def change_keys(dictionary):
    result = {}
    for i,value in enumerate(dictionary.values()):
        result[f"a{i+1}"] = value
    return result


def print_more_info(output):
    val = 0 
    H = "H(x) = "
    for key in output.keys():
        H+=f"I<sub>{key}</sub> * P<sub>{key}</sub> + "
    H = H[:-1]
    H+= " = "
    # round to 3 decimal places
    for key,value in output.items():
        
        I = round(-1 *math.log2(value),3)
        val += (I)*value
        H+=f"{I} * {value}+"

        # H+=f"{(-1*math.log2(value))}*{value}+"
        # val += (-1*math.log2(value))*value
    
    H = H[:-1]
    # round to 3 decimal places
    val = round(val,3)
    H+= f" = {val}"
    return H


def main():
    output = {"a": 0.53, "b": 0.37, "c": 0.10}
    codes = huffman(output)

    output = change_keys(output)
    codes = change_keys(codes)

    print()
    print(print_codes(codes))
    print()
    print(print_I_info(output))
    print()
    print(print_more_info(output))


if __name__ == "__main__":
    main()
