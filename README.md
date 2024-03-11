# 4WAY BLOCK SET ASSOCIATIVE + LEAST RECENTLY USED
CSC512C - G02 - Group 2 (4 Way BSA + LRU)
----
## Temporary README.md

Design a cache simulation system and analyze the various test set scenarios of the assigned cache mapping and replacement policy.<br>
General Directions: <br>
• Application platform: Stand-alone or web-based. Regardless, there should be a GUI (graphics user interface) instead of “text "-based output.<br>
• Programming languages: any programming languages (C, Java, Python, etc.).<br>
• Application repository (source code and analysis writeup): GitHub (make sure that I can access it).<br>
<br>
Common Specifications:<br>
1. Number of cache blocks = 32 blocks<br>
2. Number of memory blocks = 1024 blocks<br>
3. Cache line = 16 words<br>
4. Read policy: non load-through<br>

Test cases (n is the number of cache blocks):<br>
a.) Sequential sequence: up to 64 blocks. Repeat the sequence four times. Example: 0,1,2,3,…,63 {4x}<br>
b.) Random sequence: from 128 memory blocks (random values between 0 to 127).<br>
c.) Mid-repeat blocks: 0,1,2,3, 4-31 (2x), 32-63, then repeat 3x (so total of 4 sequences)<br>

Output:<br>
a.) System output:<br>
    a. Cache memory snapshot.<br>
        i. Option for step-by-step animated tracing or final memory snapshot<br>
        ii. Provide a text log of the cache memory trace (regardless of whether it is a step-by-step or final memory snapshot).<br>
    b. Output: <br>
      1. memory access count; <br>
      2. cache hit count; <br>
      3. cache miss count; <br>
      4. cache hit rate; <br>
      5. cache miss rate; <br>
      6. average memory access time; <br>
      7. total memory access time <br>
b.) Detail analysis of the three test cases. It will be submitted as “readme” to your GitHub. Note: Don’t forget to specify the full specs of your cache simulation system <br>
c.) Video containing the “walkthrough” of your system. Specify the link, or it can be stored in GitHub. <br>
d.) Note: the source code /executable program (stand-alone) or link to the web-based app as well as the video and analysis writeup, should all be in GitHub.
e.) Project demo if needed. Either face-to-face or through Zoom.
