from random import random
start_times = [random() for i in range(100000)]
end_times = [start_time + random() for start_time in start_times]
print(sum(end_times) / len(end_times) - sum(start_times) / len(start_times))
print(sum([end - start for start, end in zip(start_times, end_times)])/len(start_times))