![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/f3e02ac3-3acb-42a3-acf2-e69a967c6b50)
----
## Instructions in Running the Program:
1. Open your machine's CLI
2. Go to the project directory containing Cache_GUI.py
3. Run python Cache_GUI.py
4. The TKinter GUI will open.
5. Check or Uncheck the "Step-by-step Animation" option.
6. To run the simulation, choose the Test Case among the following options: (Sequential, Random, Mid-Repeat)
7. After running the simulation, press "Reset" button to cleanup the output.


## Link to Video Walkthrough:
https://drive.google.com/file/d/1SWOVWOcq94HJRUwPKYwgR1X7Khxu7kp5/view?usp=drive_link


## Common Specifications:
1. Number of Cache Blocks: 32 blocks
2. Number of Memory Blocks: 1024 blocks
3. Cache Line: 16 words
4. Cache Block Size: 4
5. Read Policy: Non Load-Through
6. Miss Penalty: 44
7. Cache Hit Default Time: 1 ns
8. Cache Miss Default Time: 10 ns

----
## Analysis
### **Test-Case 1: Sequential Sequence**
***Sequence Value (4x):*** [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]<br>
***Memory Access Count:*** 256

#### Sequence (Hit/Miss and Set) Placement
![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/6d4f2a5e-d6f4-49ae-8d3b-4309bc510cb6)

#### Final Cache Memory Snapshot
![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/b5089bf6-30bf-4b73-b64f-b9fbf7e42a40)

#### Test Case Analysis
> In test case 1 (Sequential Access), there are 256 memory access counts in the main memory. In total, there are 0 Cache Hit Counts and 256 Cache Miss Counts, since there are no blocks found in the cache memory in the sequence. With a 0% Hit Rate and 100% Miss Count, the Average Memory Access Time is 44ns, and the Total Memory Access Time is 11520ns. In this scenario, it is expected to have 0 hit counts since the sequence to pass in the cache memory will not repeat within the 32 blocks. The Sequential Access scenario will have the slowest XXXXXX since the CPU will have to fetch the memory in the main memory every time as it is not available in the cache memory.


----
### **Test-Case 2: Random Sequence**
***Sequence Value:*** <<ranging from 0-128>><br>
***Memory Access Count:*** 128

#### Sequence (Hit/Miss and Set) Placement
![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/4e925eeb-069f-441c-a0fc-cc1cd159ba22)

#### Final Cache Memory Snapshot
![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/23b42f50-84cb-41a0-b364-16537e20034c)

#### Test Case Analysis
> In test case 2 (Random Access), there are 128 memory access counts in the main memory. For this scenario, there are X Cache Hit Counts (30.43% Hit Rate) and X Cache Miss Counts (69.57% Miss Count), the Average Memory Access Time is X ns, and the Total Memory Access Time is X ns. Since the sequence of this test case is random, the values of the counts, the rates, and the access time vary per execution. In this scenario, we cannot actually declare if it is faster or slower than the Mid-Repeat Access test case; however, we can have an insight into how caching really works in an unsorted scenario.


----
### **Test-Case 3: Mid-Repeat Sequence**
***Sequence Value:*** [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]<br>
***Memory Access Count:*** 368

#### Sequence (Hit/Miss and Set) Placement
![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/f16dc9d3-a274-4b93-b46f-87aefbdd7a4e)

#### Final Cache Memory Snapshot
![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/77dcbd4a-6bfc-43ec-8138-63dc89eec2c9)

#### Test Case Analysis
In test case 3 (Mid-Repeat Access), there are 368 memory access counts in the main memory. In total, there are 112 Cache Hit Counts and 256 Cache Miss Counts, since there are no blocks found in the cache memory in the sequence. With a 30.43% Hit Rate and 69.57% Miss Count, the Average Memory Access Time is 30.92 ns, and the Total Memory Access Time is 11968 ns. In this scenario, it is expected to have 112 hit counts (28 hits per set of the sequence) since the block will be available within the 32 cache block replacement. It is also expected that the values from 4 to 31 are expected to have a HIT since it is repeated after the first 4-31. The Mid-Repeat Access Scenario will be much faster than the Sequential Access (and may or may not be faster than the Random Access) since it is expected that the blocks from 4 to 31 (repeated after the first loop) will be found in the cache memory, so there is no need to fetch it anymore in the main memory.


## Summary:
In conclusion, we have noticed that the 4-Way Block-Set Associative using Least Recently Used as the replacement algorithm will make the caching memory to be breakdown in 8 sets with 4 blocks each. Given that the cache memory has only 32 blocks, the Sequential Access (for 64 sequenced values) is expected to be slower than the Mid-Repeat Access (for 28 sequenced values) since there will be no hit counts found while the Mid-Repeat Access is expected to have 28 hit counts. The Random Access is a perfect scenario for an unsorted sequence. We can also conclude that the Memory Access Time will be affected if there are more MISS counts. However, if the sequence will have a 100% Hit, then we can assume that the memory access time will be the hit counts times the block size. Also, take note that for every HIT, the CPU will just search within the Cache Memory and for every MISS, the CPU will have to search within the Main Memory causing the caching to be slower.


