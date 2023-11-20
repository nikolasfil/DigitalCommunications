



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

    with open("huffman_tree.txt", "w") as f:
        f.write("Huffman Tree:\n")

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged_node = HuffmanNode(f"{node1.symbol}{node2.symbol}", node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2

        heapq.heappush(heap, merged_node)
        print_huffman_tree(merged_node, "")

    return heap[0]

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
        result = f"{node.symbol} : {node.freq}, Branch: {branch}"
        with open("huffman_tree.txt", "a") as f:
            f.write(f"{result}\n")
        print(result)
    if node.left is not None:
        print_huffman_tree(node.left, branch + "0")
    if node.right is not None:
        print_huffman_tree(node.right, branch + "1")

def huffman_encoding(symbol_prob):
    root = build_huffman_tree(symbol_prob)
    codes = build_huffman_codes(root)
    
    return codes

if __name__ == "__main__":
    # Example usage:
    # symbol_probabilities = {'a1a1': 0.281, 'a1a2': 0.196, 'a1a3': 0.053,
    #                         'a2a1': 0.196, 'a2a2': 0.137, 'a2a3': 0.037,
    #                         'a3a1': 0.053, 'a3a2': 0.037, 'a3a3': 0.01}

    symbol_probabilities = {'a1a1': 0.281, 'a1a2': 0.196, 'a1a3': 0.053,
                            'a2a1': 0.196, 'a2a2': 0.137, 'a2a3': 0.037,
                            'a3a1': 0.053, 'a3a2': 0.037, 'a3a3': 0.01}

    huffman_codes = huffman_encoding(symbol_probabilities)

    for symbol, code in huffman_codes.items():
        print(f"{symbol}: {code}")


