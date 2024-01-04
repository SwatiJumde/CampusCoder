import pandas as pd

def generate_car_matrix():
    # Assuming you have already loaded the dataset-1.csv into a DataFrame named df
    # If not, you can use: df = pd.read_csv('dataset-1.csv')

    # Pivot the DataFrame to create the desired matrix
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set diagonal values to 0
    for col in car_matrix.columns:
        car_matrix.at[col, col] = 0

    return car_matrix

# Example usage:
# Replace 'dataset-1.csv' with the actual path to your dataset file
df = pd.read_csv('dataset-1.csv')
result_matrix = generate_car_matrix()
print(result_matrix)
