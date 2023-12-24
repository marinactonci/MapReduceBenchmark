# Import necessary libraries
from faker import Faker  # Library for generating fake data
import pandas as pd  # Library for data manipulation and analysis
from collections import Counter  # Library for counting occurrences of elements
import os  # Library for interacting with the operating system
import time  # Library for measuring time

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
rows = [generate_row() for _ in range(20000)]

# Convert the list of rows into a DataFrame
df = pd.DataFrame(rows)

# Partition the DataFrame by the 'country' column
partitions = dict(tuple(df.groupby('country')))

# Create the 'partitions' folder if it doesn't exist
if not os.path.exists('partitions'):
    os.makedirs('partitions')
# else if the folder exists, delete all the files in it
else:
    for file in os.listdir('partitions'):
        os.remove(f'partitions/{file}')

# Save each partition to a separate CSV file in the 'partitions' folder
for country, partition in partitions.items():
    partition.to_csv(f'partitions/{country}.csv', index=False)

# Get a list of all CSV files in the current directory
csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]

# Initialize a Counter object to store the result
result = Counter()

# Start measuring time
start = time.time()

# Iterate over each CSV file
for csv_file in csv_files:
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)
    
    # Extract the 'country' column values and create a map object
    map_step = map(lambda row: row['country'], df.to_dict('records'))
    
    # Count the occurrences of each country using Counter
    reduce_step = Counter(map_step)
    
    # Add the counts to the result Counter
    result += reduce_step

# Print the country count
# for country, count in result.items():
#     print(f'{country}: {count}')

# End measuring time
end = time.time()

# Print the time taken to process the data
print(f'Partitioned data - Time taken: {(end - start)*1000} ms')