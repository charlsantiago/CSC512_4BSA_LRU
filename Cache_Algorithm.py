from random import randrange
import pandas as pd
import numpy as np

class Cache_Algorithm:
    def __init__(self, cache_blocks, line_size, policy, memory_blocks, associativity):
        self.cache_blocks = cache_blocks
        self.line_size = line_size
        self.policy = policy
        self.memory_blocks = memory_blocks
        self.associativity = associativity
        self.block_size = 4
        self.trace = [] 
        self.log = [] 
        self.access_count = 0
        self.hit_rate = 0
        self.miss_rate = 0
        self.hit_count = 0
        self.miss_count = 0
        self.avg_access_time = 0
        self.total_access_time = 0
        
        self.cache = {i: {'blocks': ['X'] * self.associativity, 'lru': list(range(self.associativity))}
                      for i in range(self.cache_blocks)}
        

    def snapshot(self, step, current_block):
        data_arr=[]
        snapshot = f"Step: {step}, Current Cache Memory:\n"
        if current_block is not None:
            snapshot += f"Block {current_block}\n"
        for index, data in enumerate(self.cache.values()):
            data_arr.append(data['blocks'])
        age_df = pd.DataFrame(data = np.array(data_arr), columns = ['Block 0', 'Block 1', 'Block 2', 'Block 3'] )
        snapshot+= age_df.to_string()
        snapshot += "\n--------------------------\n\n"

        return snapshot


    def statistics(self):
        self.hit_rate = self.hit_count / self.access_count * 100 if self.access_count > 0 else 0
        self.miss_rate = self.miss_count / self.access_count * 100 if self.access_count > 0 else 0
        #miss_penalty = 22
        miss_penalty = (4 * (1+10))

        avg_access_time_hit = (1 * (self.hit_count / self.access_count)) 
        avg_access_time_miss = (miss_penalty * (self.miss_count / self.access_count))
        self.avg_access_time = avg_access_time_hit + avg_access_time_miss

        total_access_time_hit = (4 * self.hit_count * 1) 
        total_access_time_miss = (self.miss_count * 1) + (self.miss_count * 4 * (1 + 10))
        self.total_access_time = total_access_time_hit + total_access_time_miss

        self.trace.append(f"Simulation Statistics:\n")
        self.trace.append(f"1. Memory Access Count: {self.access_count}\n")
        self.trace.append(f"2. Cache Hit Count: {self.hit_count}\n")
        self.trace.append(f"3. Cache Miss Count: {self.miss_count}\n")
        self.trace.append(f"4. Cache Hit Rate: {self.hit_rate:.2f}%\n")
        self.trace.append(f"5. Cache Miss Rate: {self.miss_rate:.2f}%\n")
        self.trace.append(f"6. Average Memory Access Time: {self.avg_access_time:.2f} cycles\n")
        self.trace.append(f"7. Total Memory Access Time: {self.total_access_time:.2f} cycles\n")


    def memory_access(self, block):
        self.access_count += 1
        cache_index = block % self.cache_blocks
        if block in self.cache[cache_index]['blocks']:
            self.log.append(f"Sequence: {block} | HIT | Set: {cache_index} \n")
            self.hit_count += 1
            block_index = self.cache[cache_index]['blocks'].index(block)
            self.cache[cache_index]['lru'].remove(block_index)
            self.cache[cache_index]['lru'].append(block_index)
        else:
            self.log.append(f"Sequence: {block} | MISS | Set: {cache_index} \n")
            self.miss_count += 1
            if len(self.cache[cache_index]['blocks']) < self.associativity:
                self.cache[cache_index]['blocks'][0] = block
            else:
                lru_index = self.cache[cache_index]['lru'].pop(0)
                self.cache[cache_index]['blocks'][lru_index] = block
                self.cache[cache_index]['lru'].append(lru_index)


    def run_simulation(self, test_case, step_by_step=True):
        sequence = self.generate_sequence(test_case)
        self.log = []
        for step, block in enumerate(sequence, start=1):
            self.memory_access(block)
            if step_by_step:
                self.trace.append(self.snapshot(step, block))

        if not step_by_step:
            self.trace.append(self.snapshot(len(sequence), None))
        self.statistics()

    def generate_sequence(self, test_case):
        sequence = []
        if test_case == 'Sequential':
            input = 63
            sequence = list(range(input + 1)) * 4
        elif test_case == 'Random':
            for i in range (128):
                sequence.append(randrange(128))
        elif test_case == 'Mid-Repeat':
            mid = []
            for i in range(28):
                 mid.append(4 + i)
            end = []
            for i in range(32):
                 end.append(32 + i)
            sequence = ([0,1,2,3] + mid + mid + end) *4
        else:
            raise ValueError("Invalid test case")
        return sequence
