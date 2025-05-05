import matplotlib.pyplot as plt
import math

def plot_kinematic_results(results: dict, dim_label: str = ""):
    times = sorted(results.keys())
    dims = len(results[times[0]]['position'])

    # Determine grid layout
    cols = math.ceil(math.sqrt(dims))
    rows = math.ceil(dims / cols)

    fig, axs = plt.subplots(rows, cols, figsize=(6 * cols, 4 * rows), sharex=True)

    # Flatten axs safely
    if isinstance(axs, plt.Axes):
        axs = [axs]
    else:
        axs = axs.ravel()

    for d in range(dims):
        positions = [results[t]['position'][d] for t in times]
        velocities = [results[t]['velocity'][d] for t in times]
        accelerations = [results[t]['acceleration'][d] for t in times]

        ax = axs[d]
        ax.plot(times, positions, label='Position', color='blue')
        ax.plot(times, velocities, label='Velocity', color='green')
        ax.plot(times, accelerations, label='Acceleration', color='red')
        ax.set_title(f"{dim_label} - Dimension {d}")
        ax.set_ylabel("Value")
        ax.legend()
        ax.grid(True)

    # Hide any unused axes
    for i in range(dims, len(axs)):
        axs[i].axis("off")

    axs[0].set_xlabel("Time (s)")
    plt.tight_layout()
    plt.show()
