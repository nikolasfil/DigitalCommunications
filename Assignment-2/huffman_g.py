import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(char_freq):
    heap = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged_node = HuffmanNode(None, node1.freq + node2.freq)
        merged_node.left = node1
        merged_node.right = node2

        heapq.heappush(heap, merged_node)

    return heap[0]

def build_huffman_codes(node, code="", mapping=None):
    if mapping is None:
        mapping = {}

    if node is not None:
        if node.char is not None:
            mapping[node.char] = code
        build_huffman_codes(node.left, code + "0", mapping)
        build_huffman_codes(node.right, code + "1", mapping)

    return mapping

def huffman_encoding(text, char_prob):
    root = build_huffman_tree(char_prob)
    codes = build_huffman_codes(root)
    
    encoded_text = ''.join(codes[char] for char in text)
    
    return encoded_text, codes

def huffman_decoding(encoded_text, codes):
    reversed_codes = {code: char for char, code in codes.items()}
    
    decoded_text = ""
    current_code = ""
    
    for bit in encoded_text:
        current_code += bit
        if current_code in reversed_codes:
            decoded_text += reversed_codes[current_code]
            current_code = ""
    
    return decoded_text

if __name__ == "__main__":
    # Example usage:
    letter_probabilities = {'A': 0.1, 'B': 0.2, 'C': 0.4, 'D': 0.3}
    text = "ABBACD"

    encoded_text, huffman_codes = huffman_encoding(text, letter_probabilities)
    print("Original text:", text)
    print("Encoded text:", encoded_text)
    
    decoded_text = huffman_decoding(encoded_text, huffman_codes)
    print("Decoded text:", decoded_text)
