from mapReduceNP import totalNP, throughputNP
from mapReduceP import totalP, throughputP
import matplotlib.pyplot as plt

print('\n--------- Benchmark ---------\n')
print('Final results:\n')

print('Total time taken:')
print('Non-partitioned:', totalNP, 'seconds')
print('Partitioned:', totalP, 'seconds\n')

print('Throughput:')
print(f'Non-partitioned: {throughputNP} rows/second')
print(f'Partitioned: {throughputP} rows/second')

values = [throughputNP, throughputP]

labels = ['Non-partitioned', 'Partitioned']

plt.barh(labels, values)

plt.xlabel('Throughput (rows/second)')
plt.ylabel('Data partitioning')

plt.title('Comparison of throughput for MapReduce with and without data partitioning')

plt.show()