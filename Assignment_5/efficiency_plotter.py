import matplotlib.pyplot as plt
from pathlib import Path


def plotter(values):
    # Create a bar plot
    file_dir = Path(__file__).parent

    plt.plot(
        range(1, len(values) + 1),
        values,
        color="blue",
        marker="o",
    )
    plt.xticks(range(1, len(values) + 1))
    # plt.stem(range(len(values)), values)

    # Adding labels and title
    plt.xlabel("J")
    plt.ylabel("Efficiency")
    plt.title("Efficiency Plotter")

    # Display the plot
    # plt.show()

    # save the plot
    file = Path(file_dir, "plot.png")
    plt.savefig(file, dpi=300, bbox_inches="tight")

    return "\n\n![700](plot.png)\n\n"


if __name__ == "__main__":
    plotter([0.917, 0.979, 0.987])
