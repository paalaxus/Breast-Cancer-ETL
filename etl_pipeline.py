import pandas as pd

def extract(file_name):
    data_frame = pd.read_csv(file_name)
    return data_frame

def transform(data_frame):
    return data_frame.loc[:, ['diagnosis','radius_mean']]

def load(data_frame, file_name):
    data_frame.to_csv(file_name, index=False)

# Define file paths
input_file = "breast_cancer.csv"
output_file = "Diagnosis_Data.csv"

# Run the ETL pipeline
extracted_data = extract(input_file)
transformed_data = transform(extracted_data)
load(transformed_data, output_file)

print(f"ETL process completed. Transformed data saved to {output_file}")
