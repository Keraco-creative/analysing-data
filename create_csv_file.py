import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

csv_file_path = 'sample_data.csv'
df.to_csv(csv_file_path, index=False)

print(f"CSV file '{csv_file_path}' has been created successfully!")
