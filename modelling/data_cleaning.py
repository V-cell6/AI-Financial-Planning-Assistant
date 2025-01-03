import csv

def delete_rows_with_negative_values(input_file, output_file):
    # Open the input CSV file in read mode
    with open(input_file, 'r') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header row

        # Create a list to store the rows without negative values
        rows_without_negative = [header]

        # Iterate through the rows and filter out rows with negative values
        for row in reader:
            if not any(float(val) < 0 for val in row):
                rows_without_negative.append(row)

    # Write the filtered data to the output CSV file
    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows_without_negative)

# Example usage:
input_csv_file = 'financial_dataset.csv'
output_csv_file = 'financial_dataset_clean.csv'
delete_rows_with_negative_values(input_csv_file, output_csv_file)
