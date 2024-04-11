from time import perf_counter
star_time = perf_counter()
for i in range(100):
    print(i)
end_time = perf_counter()
total_time = end_time - star_time
print(f"Total Time for program execution:{total_time}")
