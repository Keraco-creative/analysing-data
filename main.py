import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


try:
    df = pd.read_csv('sample_data.csv')
except FileNotFoundError:
    print("The file was not found. Please check the file path.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

print("First few rows of the dataset:")
print(df.head())

print("\nData types and missing values:")
print(df.dtypes)
print(df.isnull().sum())

df.fillna(df.mean(), inplace=True)

print("\nBasic statistics for numerical columns:")
print(df.describe())

if 'species' in df.columns and 'petal_length' in df.columns:
    grouped_data = df.groupby('species')['petal_length'].mean()
    print("\nAverage Petal Length per Species:")
    print(grouped_data)

try:
    if 'date' in df.columns and 'sales' in df.columns:
        df['date'] = pd.to_datetime(df['date']) 
        plt.figure(figsize=(10,6))
        plt.plot(df['date'], df['sales'], color='blue', marker='o')
        plt.title('Sales Trend Over Time')
        plt.xlabel('Date')
        plt.ylabel('Sales')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()
except Exception as e:
    print(f"Error generating the line chart: {e}")

plt.figure(figsize=(10,6))
sns.barplot(x='species', y='petal_length', data=df, palette='viridis')
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length')
plt.show()

plt.figure(figsize=(10,6))
plt.hist(df['sepal_length'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10,6))
plt.scatter(df['sepal_length'], df['petal_length'], color='orange')
plt.title('Sepal Length vs Petal Length')
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.show()

print("success!")
