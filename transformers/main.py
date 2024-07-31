
import pandas as pd
import os
def convert_tsv_to_parquet():
    # Get the current working directory
    cwd = os.getcwd()
    
  
    

    parquet_file = "global_chem.parquet"
    # Check if the Parquet file already exists
    if os.path.isfile(parquet_file):
        print(f"Warning: The Parquet file '{parquet_file}' already exists. Skipping conversion.")
        return
    

    
    # Read the TSV file
    df = pd.read_csv("https://raw.githubusercontent.com/Global-Chem/global-chem/development/global_chem/global_chem.tsv", sep='\t')
    
    # Define the output file path
        # Print a message indicating the conversion process
    print(f"Converting to Parquet...")
    parquet_file = os.path.join(cwd, parquet_file)
    
    # Convert to Parquet
    df.to_parquet(parquet_file, index=False)


convert_tsv_to_parquet()