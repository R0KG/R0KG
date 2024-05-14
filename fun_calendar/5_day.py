
import re




def part_2(input_txt):
    segments = input_txt.split('\n\n')
    seeds = re.findall(r'\d+',segments[0])
    min_value = float('inf')
    
    for i in range (0,20,2):
        main_seed,dest_seed = map(int,(seeds[i],seeds[i+1]))
        for seed in range(main_seed,dest_seed):
            for segment in segments[1:]:
                for conversion in re.findall(r'(\d+) (\d+) (\d+)',segment):
                    dest,start,delta = map(int,conversion)
                    if seed in range(start,start+delta):
                        seed += dest - start
                        break
            min_value = min(seed, min_value)
    return min_value


def part_1(input_txt):
    
    segments = input_txt.split('\n\n')
    seeds = re.findall(r'\d+',segments[0])
    min_value = float('inf')
    
    for seed in map(int,seeds):
        for segment in segments[1:]:
            for conversion in re.findall(r'(\d+) (\d+) (\d+)',segment):
                dest,start,delta = map(int,conversion)
                if seed in range(start,start+delta):
                    seed += dest - start
                    break
        min_value = min(seed, min_value)
    return min_value
                
with open("5_day_inp.txt", "r") as text:
    inp = text.read()
    print(part_2(inp))
    
