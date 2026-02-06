import pandas as pd
import os
import tempfile
from collections import defaultdict

def merge_csv_files(uploaded_files):
    temp_dir = tempfile.mkdtemp()                   #Temporary File Storage
    files_by_country = defaultdict(list)            #Dictionary to store csv by country code

    for uploaded_file in uploaded_files:
        filename = uploaded_file.name
        if not filename.lower().endswith('.csv'):
            continue

        country_code = filename[:2].upper()          #Gets Country Code from csv filename

        df = pd.read_csv(uploaded_file, encoding='utf-16', sep='\t')
        files_by_country[country_code].append(df)

    output_files = []
    for country_code, dfs in files_by_country.items():                  
        merged_df = pd.concat(dfs, ignore_index=True, sort=False)           #Merges csv files by country code
        out_file = os.path.join(temp_dir, f"{country_code}_merged.csv")     #Naming merged csv file (ex. PH_merged.csv)
        merged_df.to_csv(out_file, index=False, encoding='utf-8')
        output_files.append(out_file)

    return output_files
