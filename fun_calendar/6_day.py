
import re

with open('6_inp.txt') as file:
    text = file.read()
    nums = re.findall(r'\d+',text)
    
    res = 1
    temp = 0
    time_race = int(''.join(nums[:4]))
    dist_race = int(''.join(nums[4:]))
    
    
    
    for time in range(time_race):
        if ((time_race - time) * time) > dist_race:
                temp += 1
    print(temp)
    
        
    
    




