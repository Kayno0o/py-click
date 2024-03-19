import os
import json
import matplotlib.pyplot as plt
from datetime import datetime
from filename import get_reports_dir


def load_json_data(directory):
    json_data = {}

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                # Extracting date from filename
                date = datetime.strptime(
                    os.path.splitext(filename)[0], "%Y-%m-%d"
                ).strftime("%Y-%m-%d")
                try:
                    data = json.load(file)
                    # Adding data to json_data with date as key
                    json_data[date] = data
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in file {filename}: {e}")
    json_data = dict(sorted(json_data.items()))
    return json_data


def plot_fields(ax, json_data, fields, name):
    dates = list(json_data.keys())

    # Plotting each field
    for field_name in fields:
        field_values = []

        # Extract field values
        for data in json_data.values():
            field_values.append(
                data.get(field_name, 0)
            )  # Get field value, default to 0 if not present

        # Plotting
        ax.plot(
            dates,
            field_values,
            marker="o",
            linestyle="-",
            label=field_name.capitalize(),
        )

    # Plot configuration
    ax.set_title("{} over Time".format(name))
    ax.set_xlabel("Date")
    ax.set_ylabel("Value")
    ax.legend()


if __name__ == "__main__":
    directory = get_reports_dir()
    print(directory)
    json_data = load_json_data(directory)

    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    plot_fields(
        axs[0, 0],
        json_data,
        ["left_clicks", "right_clicks"],
        "Clicks",
    )

    plot_fields(
        axs[0, 1],
        json_data,
        ["scroll_up", "scroll_down"],
        "Scroll",
    )

    plot_fields(
        axs[1, 0],
        json_data,
        ["total_distance"],
        "Total Distance",
    )

    plot_fields(
        axs[1, 1],
        json_data,
        ["total_key_presses"],
        "Keys",
    )

    plt.tight_layout()
    plt.show()
