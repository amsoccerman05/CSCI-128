import csv
import matplotlib.pyplot as plt

# Function to read data from the CSV file
def read_survey_data(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            x, y, z = map(float, row)
            data.append((x, y, -1*z))
    return data

# Function to plot and save the horizontal section
def plot_horizontal_section(file, data, output_path):
    x = [point[0] for point in data]
    y = [point[1] for point in data]

    # x_min, x_max = min(x), max(x)
    # y_min, y_max = min(y), max(y)
    
    # Calculate data range
    #data_range = max(x_max - x_min, y_max - y_min)

    #plt.figure(figsize=(data_range, data_range))
    #plt.plot(x, y, 'b-')
    title = file[:-4]
    plt.plot(x, y)
    plt.xlabel('Easting, EW (ft)')
    plt.ylabel('Northing, NS (ft)')
    plt.title(title +' Horizontal Section')

    # plt.xlim(x_min, x_max)
    # plt.ylim(y_min, y_max)
    
    plt.savefig(output_path, format='png')
    plt.close()

# Function to plot and save the vertical section
def plot_vertical_section(file, data, output_path):
    x = [point[0] for point in data]
    z = [point[2] for point in data]

    # x_min, x_max = min(x), max(x)
    # z_min, z_max = min(z), max(z)

    # Calculate data range
    #data_range = max(x_max - x_min, z_max - z_min)
    title = file[:-4]
    #plt.figure(figsize=(data_range, data_range))
    plt.plot(x, z)
    plt.xlabel('East-West Crossection (ft)')
    plt.ylabel('True Vertical Depth (ft)')
    plt.title(title + ' Vertical Section')

    # plt.xlim(x_min, x_max)
    # plt.ylim(z_min, z_max)

    # Set aspect ratio to 'equal' to ensure correct scaling
    # plt.gca().set_aspect('equal')

    plt.savefig(output_path, format='png')
    plt.close()

# Main function
def main():
    input_path = input("INPUT_PATH> ")
    output_horizontal_path = input("OUTPUT_HS> ")
    output_vertical_path = input("OUTPUT_VS> ")

    survey_data = read_survey_data(input_path)

    plot_horizontal_section(input_path, survey_data, output_horizontal_path)
    plot_vertical_section(input_path, survey_data, output_vertical_path)

if __name__ == "__main__":
    main()
