import matplotlib.pyplot as plt
import math

def plot_force_results(results: dict, dim_label: str = ""):
    times = sorted(results.keys())
    dims = len(results[times[0]]['acceleration'])  # assumes mass and acceleration are same length

    # Grid layout
    cols = math.ceil(math.sqrt(dims))
    rows = math.ceil(dims / cols)

    fig, axs = plt.subplots(rows, cols, figsize=(6 * cols, 4 * rows), sharex=True)

    # Flatten axes
    if isinstance(axs, plt.Axes):
        axs = [axs]
    else:
        axs = axs.ravel()

    for d in range(dims):
        masses = [results[t]['mass'] for t in times]
        accs = [results[t]['acceleration'][d] for t in times]
        forces = [results[t]['vector'][d] for t in times]

        ax = axs[d]
        ax.plot(times, masses, label='Mass', color='orange')
        ax.plot(times, accs, label='Acceleration', color='red')
        ax.plot(times, forces, label='Force', color='blue')
        ax.set_title(f"{dim_label} - Dimension {d}")
        ax.set_ylabel("Value")
        ax.legend()
        ax.grid(True)

    for i in range(dims, len(axs)):
        axs[i].axis("off")

    axs[0].set_xlabel("Time (s)")
    plt.tight_layout()
    plt.show()
