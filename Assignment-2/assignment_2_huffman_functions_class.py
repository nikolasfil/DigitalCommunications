import heapq
from pathlib import Path


class HuffmanNode:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


class HuffmanFunctions:
    def __init__(self) -> None:
        pass

    def build_huffman_tree(self, symbol_freq):
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

            self.print_huffman_tree(merged_node, "")

        return heap[0]

    def huffman(self, output):
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
            # add the combined node to the list of nodes

            nodes.append([combined_node, node1[1] + node2[1]])

            print(f"Node Tree: {len(nodes)} {nodes}")

            # add the combined node to the dictionary of codes

            for symbol in node1[0]:
                codes[symbol] = "0" + codes[symbol]
            for symbol in node2[0]:
                codes[symbol] = "1" + codes[symbol]

        return codes

    def huffman_encode_pairs(self, combinations_dict, pairs=2):
        """Returns the encoded huffman codes for the combinatios of x pairs"""
        result = ""
        huffman_encoded = self.huffman_encoding(combinations_dict)
        huffman_pairs_encoded = {
            key: value
            for key, value in huffman_encoded.items()
            if len(key) == 2 * pairs
        }
        result = f"\n\n| {'Combination':15} | {'Code':15} |\n| {'-':15} | {'-':15} |\n"
        for key in sorted(huffman_pairs_encoded.keys()):
            temp_result = f"| {key:15} | {huffman_pairs_encoded[key]:15} | "
            result += temp_result + "\n"

        return result, huffman_pairs_encoded

    def print_huffman_tree(self, node, val):
        # huffman code for current node
        # if node is not an edge node
        if node.left:
            self.print_huffman_tree(node.left, val + "0")
        if node.right:
            self.print_huffman_tree(node.right, val + "1")
        if not node.left and not node.right:
            print(f"{node.symbol} -> {val}")

    def huffman_encoding(self, symbol_prob):
        root = self.build_huffman_tree(symbol_prob)
        codes = self.build_huffman_codes(root)

        return codes

    def build_huffman_codes(self, node, code="", mapping=None):
        if mapping is None:
            mapping = {}

        if node is not None:
            if node.symbol is not None:
                mapping[node.symbol] = code
            self.build_huffman_codes(node.left, code + "0", mapping)
            self.build_huffman_codes(node.right, code + "1", mapping)

        return mapping


class HuffmanBrancher:
    def __init__(self, file, file_to_save) -> None:
        self.file = file
        self.file_to_save = file_to_save

        parent_folder = Path(__file__).parent
        self.file = Path(parent_folder, file)

    def get_huffman_lines(self):
        with open(self.file) as f:
            lines = f.readlines()
        return lines

    def splitting_huffman_lines(self, lines):
        # The result
        resulting_nodes = []
        noding = []
        numbering_nodes = {}

        for line in lines:
            noding.append([line.split(",")[0].split(":"), line.split(",")[1]])
            id_name = line.split(",")[0].split(":")[0]
            display_name = line.split(",")[0]
            branch = line.split(",")[1]
            temp_result = f'{id_name}["{display_name}"] \n\n-- {branch} -->  \n\n'

            resulting_nodes.append(temp_result)

            # num = len(id_name)//4
            # if num not in numbering_nodes.keys():
            #     numbering_nodes[num] = set()
            # numbering_nodes[num].add(id_name)

        # print(numbering_nodes)

        return resulting_nodes, noding

    def save_tree_to_file(self, file, noding):
        with open(file, "w") as f:
            f.write("```mermaid\ngraph LR; \n")
            for node in noding:
                f.write(node)
            f.write("\n```\n")

    def main(self):
        lines = self.get_huffman_lines()

        resulting_nodes, noding = self.splitting_huffman_lines(lines)

        parent_folder = Path(__file__).parent
        root_folder = Path(parent_folder.parent)

        file_to_save = Path(
            root_folder, "MD_Reports", "assignment-2", self.file_to_save
        )

        self.save_tree_to_file(file_to_save, resulting_nodes)


if __name__ == "__main__":
    functions = HuffmanFunctions()
    brancher = HuffmanBrancher("huffman_tree.txt", "assignment_2_huffman_tree_1.md")
    brancher.main()
