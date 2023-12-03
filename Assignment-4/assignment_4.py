def save_to_file(result, file):
    with open(file, "w") as f:
        for line in result:
            f.write(line)


def save_code():
    lines = ["```python\n\n"]
    with open(__file__, "r") as f:
        for line in f:
            lines.append(line)
    lines.append("```")
    return lines


def main():
    result = []

    result.append("## Assignment-4\n\n")
    result.append("\n\n")

    print("".join(result))

    # Saving Code

    # result.append("## Code\n\n")
    # result.append("".join(save_code()))
    # result.append("\n\n")

    save_to_file(result, "../MD_Reports/assignment-4-code-result.md")


if __name__ == "__main__":
    main()
