import pandas as pd
import glob
import os
import chardet

def detect_encoding(file_path):
    """Detect the encoding of a file."""
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

def merge_csv_files(folder_path, output_file):
    try:
        # Get all CSV file paths in the folder
        csv_files = glob.glob(os.path.join(folder_path, "*.csv"))
        if not csv_files:
            raise FileNotFoundError("No CSV files found in the specified folder.")

        column_sets = []
        dataframes = []

        for file in csv_files:
            # Detect the encoding
            encoding = detect_encoding(file)
            print(f"Detected encoding for {file}: {encoding}")

            # Read the CSV file with the detected encoding
            df = pd.read_csv(file, encoding=encoding)
            dataframes.append(df)

            # Collect column names
            column_sets.append(set(df.columns))

        # Check if all files have the same columns
        first_column_set = column_sets[0]
        if not all(cols == first_column_set for cols in column_sets):
            raise ValueError("CSV files have mismatched columns.")

        # Concatenate all files (aligning columns automatically)
        merged_df = pd.concat(dataframes, ignore_index=True)

        # Save to the output file
        merged_df.to_csv(output_file, index=False)
        print(f"CSV files successfully merged into {output_file}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


folder_path = "/home/betty/Desktop/Becode_training_path/Projects/Immo-Eliza-project/Beatriz_scraper_class/CSV_folder"
output_file = "/home/betty/Desktop/Becode_training_path/Projects/Immo-Eliza-project/merged_file.csv"
merge_csv_files(folder_path, output_file)