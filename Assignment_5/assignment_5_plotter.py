import matplotlib.pyplot as plt
import math


def plotting(points, file=None, titling=None, show=True):
    # Extract x and y values from the points
    x_values, y_values = zip(*points)

    # Plot the function curve using lines
    plt.plot(
        x_values, y_values, marker="o", linestyle="-", color="blue", label=r"$f_1(4-t)$"
    )

    # Set labels and title
    plt.xlabel("x")
    plt.ylabel("y")
    if not titling:
        titling = "Graph"
    plt.title(titling)

    # Add grid for better visualization
    plt.grid(True)

    # Add a legend
    plt.legend()

    if show:
        # Show the plot
        plt.show()

    if file:
        plt.savefig(file, dpi=300, bbox_inches="tight")

    # Close the plot
    plt.close()


if __name__ == "__main__":
    # Define the points
    points = [(1, 0), (1, -2), (2, -2), (2, 2), (3, 2), (3, 0)]
    plotting(points)
