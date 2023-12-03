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


import numpy as np
import matplotlib.pyplot as plt


# Function definition
def f1(t):
    if 0 <= t < 1:
        return 1 / np.sqrt(2)
    elif 1 <= t < 2:
        return -1 / np.sqrt(2)
    else:
        return 0


def f2(t):
    if 2 <= t <= 4:
        return -1 / np.sqrt(2)
    else:
        return 0


def f3(t):
    if 2 <= t < 3:
        return 1 / np.sqrt(2)
    elif 3 <= t < 4:
        return -1 / np.sqrt(2)
    else:
        return 0


def f4(t):
    if 0 <= t < 1:
        return -1 * ((np.sqrt(2)) / 2)
    elif 1 <= t < 2:
        return -1 * ((np.sqrt(2)) / 2)

    elif 2 <= t < 3:
        return 0
    elif 3 <= t <= 4:
        return 0
    else:
        return 0


def plot_f1(t_values, file):
    # Calculate corresponding f1 values
    values = [f1(t) for t in t_values]

    # Plot the function
    plt.plot(t_values, values, label=r"$f_{1}(t)=\frac{S_{1}}{\sqrt{2}}$")

    # Set x and y axis limits to start from 0
    plt.xlim(0, 4)
    plt.ylim(-1, 1)

    # Add labels and title
    plt.xlabel("t")
    plt.ylabel(r"$f_{1}(t)$")
    plt.title("Plot of $f_{1}(t)$ for $S_{1}=\pm1$")
    plt.grid(True)
    plt.legend()

    # Show the plot
    # plt.show()
    plt.savefig(file)
    plt.close()


def plot_f2(t_values, file):
    # Calculate corresponding f1 values
    values = [f2(t) for t in t_values]

    # Plot the function
    plt.plot(t_values, values, label=r"$f_{2}(t)=\frac{S_{2}}{\sqrt{2}}$")

    # Set x and y axis limits to start from 0
    plt.xlim(0, 4)
    plt.ylim(-1, 1)

    # Add labels and title
    plt.xlabel("t")
    plt.ylabel(r"$f_{2}(t)$")
    plt.title("Plot of $f_{2}(t)$ for $S_{2}=\pm1$")
    plt.grid(True)
    plt.legend()

    # Show the plot
    # plt.show()
    plt.savefig(file)
    plt.close()


def plot_f3(t_values, file):
    # Calculate corresponding f1 values
    values = [f3(t) for t in t_values]

    # Plot the function
    plt.plot(t_values, values, label=r"$f_{3}(t)=S_{3}$")

    # Set x and y axis limits to start from 0
    plt.xlim(0, 4)
    plt.ylim(-1, 1)  # Adjust the y-axis limits as needed based on the range of f3'

    # Add labels and title
    plt.xlabel("t")
    plt.ylabel(r"$f_{3}(t)$")
    plt.title("Plot of $f_{3}(t)$ for $S_{3}=\pm1$")
    plt.grid(True)
    plt.legend()

    # Show the plot
    # plt.show()
    plt.savefig(file)
    plt.close()


def plot_f4(t_values, file):
    # Calculate corresponding f1 values
    values = [f4(t) for t in t_values]

    # Plot the function
    plt.plot(t_values, values, label=r"$f_{4}(t)=\frac{f_{4}'}{\sqrt{2}}$")

    # Set x and y axis limits to start from 0
    plt.xlim(0, 4)
    plt.ylim(-1, 1)

    # Add labels and title
    plt.xlabel("t")
    plt.ylabel(r"$f_{4}(t)$")
    plt.title(
        r"Plot of $f_{4}=\left\{ - \frac{\sqrt{ 2 }}{2},- \frac{\sqrt{ 2 }}{2},0,0 \right\}$"
    )
    plt.grid(True)
    plt.legend()

    # Show the plot
    # plt.show()
    plt.savefig(file)
    plt.close()


def main():
    # Generate values for t
    t_values = np.linspace(0, 5, 1000)

    # Plot the function
    # plot_f1(t_values, "assignment_4_f1.png")
    # plot_f2(t_values, "assignment_4_f2.png")
    # plot_f3(t_values, "assignment_4_f3.png")
    plot_f4(t_values, "assignment_4_f4.png")
    # result = []

    # result.append("## Assignment-4\n\n")
    # result.append("\n\n")

    # print("".join(result))

    # Saving Code

    # result.append("## Code\n\n")
    # result.append("".join(save_code()))
    # result.append("\n\n")

    # save_to_file(result, "../MD_Reports/assignment-4-code-result.md")


if __name__ == "__main__":
    main()
