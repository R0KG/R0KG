



inp = [["London","NY"],["NY","Lolo"]]

def solution (paths: list[list[str]]) -> str:
    outs = set()
    ins = set()
    
    
    for a,b in paths:
        outs.add(a)
        ins.add(b)
        
    return [b for b in ins if b not in outs]
print(solution(inp))