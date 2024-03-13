import math
import pandas as pd

#test

cache_array = [1,7,5,0,2,1,5,6,5,2,2,0]
cache_block = 4
set_size = 2
block_size = 2
cache_size = len(cache_array)

cols = int(math.sqrt(cache_block))
default_val = [None]*cols
row_index = [i for i in range(set_size)]

#2D Array
arr = []
for x in row_index:
    arr.append(default_val)
cache = []
age = []
for x in row_index:
    cache.append(arr)
    age.append(arr)
cache_df = pd.DataFrame(data = cache[0], index=row_index)
age_df = pd.DataFrame(data = age[0], index=row_index)

# STATE ARRAY
for i in range(len(cache_array)):
#for i in range(1):
    print("")
    print(f"STATE: {i} ----------------------")

    current_cache = cache_array.pop(0)
    set_dir = current_cache % set_size
    print(f"Current Cache: {current_cache}")
    print(f"Set Size: {set_dir}")

    print("")
    print("Cache DF")
    print(cache_df)

    print("Age DF")
    print(age_df)

    print(cache_df[0][0])
    if cache_df[0][0] == None:
        cache_df[0][0] = current_cache
        print("D")
        print(cache_df)

    if cache_df[0][0] != current_cache:
        age_df
