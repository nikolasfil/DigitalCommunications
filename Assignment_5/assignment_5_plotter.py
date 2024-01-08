import matplotlib.pyplot as plt
import math


def plotting(
    points,
    file=None,
    titling=None,
    show=True,
    label=None,
    x_axis_name: str = "x",
    y_axis_name: str = "y",
):
    if label is None:
        label = "f(t)"
    # Extract x and y values from the points
    x_values, y_values = zip(*points)

    # Plot the function curve using lines

    plt.plot(
        x_values,
        y_values,
        marker="o",
        linestyle="-",
        color="blue",
        label=rf"${label}$",
    )

    # Set color to axis
    # ax = plt.gca()
    # ax.spines["bottom"].set_color("red")
    # ax.spines["left"].set_color("red")

    plt.axvline(x=0, color="red", linestyle="--")

    # Draw a horizontal line at y=0
    plt.axhline(y=0, color="red", linestyle="--")

    # Set labels and title
    plt.xlabel(x_axis_name)
    plt.ylabel(y_axis_name)
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
