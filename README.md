![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/a689ac73-c5de-43dc-90db-c8e64095c198)![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/7fe3d86c-5d11-4815-b431-32ad6a7a2487)![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/f3e02ac3-3acb-42a3-acf2-e69a967c6b50)
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

#### Analysis


----
### **Test-Case 2: Random Sequence**
***Sequence Value:*** <<ranging from 0-128>><br>
***Memory Access Count:*** 128

#### Sequence (Hit/Miss and Set) Placement
![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/6d4f2a5e-d6f4-49ae-8d3b-4309bc510cb6)

#### Final Cache Memory Snapshot
![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/23b42f50-84cb-41a0-b364-16537e20034c)

#### Analysis



----
### **Test-Case 3: Mid-Repeat Sequence**
***Sequence Value:*** [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63]<br>
***Memory Access Count:*** 368

#### Sequence (Hit/Miss and Set) Placement
![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/d738c082-8909-4e55-b3b7-e7d7a0982e16)

#### Final Cache Memory Snapshot
![image](https://github.com/charlsantiago/CSC512_4BSA_LRU/assets/77201252/77dcbd4a-6bfc-43ec-8138-63dc89eec2c9)

#### Analysis




