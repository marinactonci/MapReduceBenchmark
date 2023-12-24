# Import necessary libraries
from faker import Faker  # Library for generating fake data
from collections import Counter  # Library for counting occurrences of elements
import time  # Library for measuring time

# Create an instance of the Faker class
fake = Faker()

# Define a function to generate a single row of data
def generate_row():
    return {
        'name': fake.name(),
        'street': fake.street_name(),
        'city': fake.city(),
        'country': fake.country(),
        'email': fake.email(),
        'date_of_birth': fake.date_of_birth(minimum_age=22, maximum_age=90)
    }

# Generate a list of 20000 rows of data using list comprehension
rows = [generate_row() for _ in range(20000)]

# Start measuring the execution time
start = time.time()

# Apply the map function to extract the 'country' field from each row
map_step = map(lambda row: row['country'], rows)

# Count the occurrences of each country using the Counter function
reduce_step = Counter(map_step)

# Print the country count
# for country, count in reduce_step.items():
#     print(f'{country}: {count}')

# Stop measuring the execution time
end = time.time()

# Print the total time taken for the execution
print(f'Non partitioned data - Time taken: {(end - start)*1000} ms')