# Import necessary libraries
from faker import Faker  # Library for generating fake data
import pandas as pd  # Library for data manipulation and analysis
from collections import Counter  # Library for counting occurrences of elements
import os  # Library for interacting with the operating system
import time  # Library for measuring time

print('\n---------------------------------- MapReduce with data partitioning ----------------------------------\n')

# Create a folder named 'partitions' if it doesn't exist
if not os.path.exists('partitions'):
    os.mkdir('partitions')
# else if the folder exists, delete all the files in it
else:
    for f in os.listdir('./partitions'):
        os.remove(f'./partitions/{f}')

# Create a Faker instance
fake = Faker()

# Define a function to generate a row of data
def generate_row():
    return {
        'name': fake.name(),
        'street': fake.street_name(),
        'city': fake.city(),
        'country': fake.country(),
        'email': fake.email(),
        'date_of_birth': fake.date_of_birth(minimum_age=22, maximum_age=90)
    }

# Generate a list of rows
rows = [generate_row() for _ in range(100000)]

# Convert the list of rows into a DataFrame
df = pd.DataFrame(rows)

# Partition the DataFrame by the 'country' column
partitions = dict(tuple(df.groupby('country')))

# Save each partition to a separate CSV file in the 'partitions' folder
for country, partition in partitions.items():
    partition.to_csv(f'partitions/{country}.csv', index=False)

# Get a list of all CSV files in the current directory
#csv_files = [f'main/partitions/{f}' for f in os.listdir('./main/partitions') if f.endswith('.csv')]
csv_file = 'partitions/Croatia.csv'

def process_file(csv_file):
    df = pd.read_csv(csv_file)
    map_step = map(lambda row: row['country'], df.to_dict('records'))
    return Counter(map_step).get('Croatia', 0)

# Initialize a Counter object to store the result
result = 0

start = time.time()

# Simulate processing by adding a delay of 0.5 seconds
time.sleep(0.5)

def map_function(row):
    return row['country']

def reduce_function(values):
    return Counter(values).get('Croatia', 0)

df = pd.read_csv(csv_file)
map_step = map(map_function, df.to_dict('records'))
reduce_step = reduce_function(map_step)
result += reduce_step

# End measuring time
end = time.time()

#Print the country count
print(f"Croatia: {result}")

# Calculate the total time taken for the execution
totalP = end-start

# Calculate the throughput
throughputP = round(len(rows)/totalP, 2)

# Print the time taken to process the data
print(f'\nTotal time taken: {totalP} seconds')
print(f'\nThroughput: {throughputP} rows/second')
print('\n--------------------------------------------------------------------\n')
      