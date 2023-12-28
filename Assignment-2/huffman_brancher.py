def get_huffman_lines():
    with open("huffman_tree.txt", "r") as f:
        lines = [line.strip("\n") for line in f.readlines()]
    return lines[1:]


def splitting_huffman_lines(lines):
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


def save_tree_to_file(file, noding):
    with open(file, "w") as f:
        f.write("```mermaid\ngraph LR; \n")
        for node in noding:
            f.write(node)
        f.write("\n```\n")


def main():
    lines = get_huffman_lines()

    # for line in lines:
    #     print(line)
    resulting_nodes, noding = splitting_huffman_lines(lines)
    # for i in noding:
    #     print(i)
    save_tree_to_file("assignment_2_huffman_tree_1.md", resulting_nodes)


if __name__ == "__main__":
    main()


# def splitting_huffman_lines1(lines):
#     resulting_nodes = []
#     noding = []
#     individual_nodes = set()
#     multiple_nodes = set()


#     for line in lines:
#         noding.append([line.split(",")[0].split(":"),line.split(",")[1]])
#         id_name = line.split(",")[0].split(":")[0]
#         display_name = line.split(",")[0]
#         resulting_nodes.append(f'{id_name}["{display_name}"]\n\n')


#         if len(id_name) == 4:
#             individual_nodes.add(id_name)
#         elif len(id_name) == 8):
#             multiple_nodes.add(id_name)


#     multiple_nodes = list(multiple_nodes)
#     mutliple_nodes_breakdown = []

#     for node in multiple_nodes:
#         node_small_list = []
#         for i in range(0,len(node),4):
#             node_small_list.append(node[i:i+4])
#         mutliple_nodes_breakdown.append(node_small_list)

#     for i,nodes in  enumerate(mutliple_nodes_breakdown):
#         for node in individual_nodes:
#             if node in nodes:
#                 resulting_nodes.append(f'{node} --> {multiple_nodes[i]}\n')
#     # print(mutliple_nodes_breakdown)

#     return resulting_nodes,noding
