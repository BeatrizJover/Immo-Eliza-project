import pandas as pd

def read_csv(file_path):
    try:
        
        df = pd.read_csv(file_path)
        print("CSV file successfully loaded!")
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: The file contains parsing errors.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None  


file_path = '/home/betty/Desktop/Becode_training_path/Projects/Immo-Eliza-project/Alek_scrapper_results/apartment_data.csv'
df = read_csv(file_path)
if df is not None:
    print(df.info()) 

print(df.shape)
# print(df.describe())
# print(df.isna().any())
# print(df.isna().sum())
# print(df.dtypes)
# print(df['subtype_of_property'])
# print(df['equipped_kitchen'])

# Get unique values
unique_values = df['subtype_of_property'].unique()

# Factorizing subtype of property
unique_values_list = unique_values.tolist()
df['subtype_of_property'], unique_categories = pd.factorize(df['subtype_of_property'])
print("Mapping of categories to numbers:", dict(enumerate(unique_categories)))
print(df['subtype_of_property'])

# Factorizing equipped_kitchen
unique_values = df['equipped_kitchen'].unique()
unique_values_list = unique_values.tolist()
df['equipped_kitchen'], unique_categories = pd.factorize(df['equipped_kitchen'])
print("Mapping of categories to numbers:", dict(enumerate(unique_categories)))
print(df['equipped_kitchen'])

print(df.dtypes)
print(df.describe())
