from itertools import product


class HuffmanNode:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ""


def build_huffman_tree(node, tree=None, val=""):
    if tree is None:
        tree = []
    new_val = val + str(node.code)

    if node.left:
        tree = build_huffman_tree(node.left, tree, new_val)
    if node.right:
        tree = build_huffman_tree(node.right, tree, new_val)

    if not node.left and not node.right:
        tree.append((node.symbol, new_val))

    return tree


def create_final_tree(nodes):
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: (-x.freq, x.symbol), reverse=True)
        left = nodes[0]
        right = nodes[1]

        left.code = 0
        right.code = 1

        new_node = HuffmanNode(
            left.freq + right.freq, left.symbol + right.symbol, left, right
        )

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    final_tree = build_huffman_tree(nodes[0])
    return final_tree


def main():
    nodes = []

    symbols_probabilities = {"a1": 0.53, "a2": 0.37, "a3": 0.10}
    new_symbols_probabilities = {}
    number_of_symbols = int(input("Number of encoding symbols J: "))
    print()

    for combination in product(symbols_probabilities, repeat=number_of_symbols):
        chance = 1
        for symbol in combination:
            chance *= symbols_probabilities[symbol]
        symbol_name = "".join(combination)

        new_symbols_probabilities[symbol_name] = chance
        nodes.append(HuffmanNode(chance, symbol_name))

    print()

    final_tree = create_final_tree(nodes)

    print("SYMBOLS  PROBABILITY  CODE")
    final_tree = sorted(final_tree, key=lambda x: x[0])
    average_code_length = 0

    for item in final_tree:
        print(f"{item[0]}   |{new_symbols_probabilities[item[0]]:.4f}  |{item[1]}")
        average_code_length += new_symbols_probabilities[item[0]] * len(item[1])
    
    print(f"\n Average Code Length R = {average_code_length:.3f}")
    nodes = []


if __name__ == "__main__":
    main()
