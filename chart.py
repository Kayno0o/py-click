import os
import json
import matplotlib.pyplot as plt
import sys
from filename import get_reports_dir


def load_json_data(directory):
    json_data = {}

    # Iterate over files in the directory
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename), "r") as file:
                # Extracting date from filename
                date = os.path.splitext(filename)[0]
                try:
                    data = json.load(file)
                    # Adding data to json_data with date as key
                    json_data[date] = data
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON in file {filename}: {e}")
    return json_data


def plot_fields(json_data, field_names, save_path=None):
    dates = list(json_data.keys())

    # Plotting each field
    for field_name in field_names:
        field_values = []

        # Extract field values
        for data in json_data.values():
            field_values.append(
                data.get(field_name, 0)
            )  # Get field value, default to 0 if not present

        # Plotting
        plt.plot(
            dates,
            field_values,
            marker="o",
            linestyle="-",
            label=field_name.capitalize(),
        )

    # Plot configuration
    plt.title("Fields over Time")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()

    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)

    plt.show()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python chart.py <field_name1> <field_name2> ...")
        sys.exit(1)

    # Field names from command-line arguments
    field_names = sys.argv[1:]

    # Specify the directory containing reports
    directory = get_reports_dir()

    # Load JSON data
    json_data = load_json_data(directory)

    # Specify the save path
    save_path = os.path.join(directory, "charts", "_".join(field_names) + ".png")

    # Plot specified fields and save if save path is provided
    plot_fields(json_data, field_names, save_path)
