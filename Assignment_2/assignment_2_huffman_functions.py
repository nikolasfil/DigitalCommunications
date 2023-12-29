import heapq
from collections import defaultdict


class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(symbol_freq):
    heap = [HuffmanNode(symbol, freq) for symbol, freq in symbol_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged_node = HuffmanNode(
            f"{node1.symbol}{node2.symbol}", node1.freq + node2.freq
        )
        merged_node.left = node1
        merged_node.right = node2

        heapq.heappush(heap, merged_node)

        print_huffman_tree(merged_node, "")

    return heap[0]


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
        print(f"Node Tree: {len(nodes)} {nodes}")
        # update codes
        for symbol in node1[0]:
            codes[symbol] = "0" + codes[symbol]
        for symbol in node2[0]:
            codes[symbol] = "1" + codes[symbol]

    return codes


def huffman_encode_pairs(combinations_dict, pairs=2):
    """Returns the encoded huffman codes for the combinatios of x pairs"""
    result = ""
    huffman_encoded = huffman_encoding(combinations_dict)
    huffman_pairs_encoded = {
        key: value for key, value in huffman_encoded.items() if len(key) == 2 * pairs
    }
    result = f"\n\n| {'Combination':15} | {'Code':15} |\n| {'-':15} | {'-':15} |\n"
    for key in sorted(huffman_pairs_encoded.keys()):
        temp_result = f"| {key:15} | {huffman_pairs_encoded[key]:15} | "
        result += temp_result + "\n"

    return result, huffman_pairs_encoded


def huffman_encoding(symbol_prob):
    root = build_huffman_tree(symbol_prob)
    codes = build_huffman_codes(root)

    return codes


def build_huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}

    if node is not None:
        if node.symbol is not None:
            mapping[node.symbol] = code
        build_huffman_codes(node.left, code + "0", mapping)
        build_huffman_codes(node.right, code + "1", mapping)

    return mapping


def print_huffman_tree(node, branch):
    if node.symbol is not None:
        result = f"{node.symbol}:{node.freq},{branch}"
        with open("huffman_tree.txt", "a") as f:
            f.write(f"{result}\n")
        # print(result)
    if node.left is not None:
        print_huffman_tree(node.left, branch + "0")
    if node.right is not None:
        print_huffman_tree(node.right, branch + "1")
