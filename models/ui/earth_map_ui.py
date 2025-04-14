import matplotlib.pyplot as plt

def run_earth_map_ui(earth_data, city_data):
    # Plot the map with cities
    fig, ax = plt.subplots()
    earth_data.plot(ax=ax, edgecolor="black", facecolor="lightgray")

    # Plot cities as red dots
    city_data.plot(ax=ax, color="red", markersize=50)

    # Annotate city names
    for idx, row in city_data.iterrows():
        ax.text(row.geometry.x + 2, row.geometry.y, row["city"], fontsize=9, color="darkred")

    plt.title("World Map with Sample Cities", fontsize=16)
    plt.axis("off")
    plt.tight_layout()
    plt.show()
