def dfs(depth, max_depth):
    global result
    if depth == max_depth:  
        result = max(result, int(''.join(inf)))
        return
    
    for i in range(len(inf)):
        for j in range(i + 1, len(inf)):  



                inf[i], inf[j] = inf[j], inf[i]  
                dfs(depth + 1, max_depth)  
                inf[i], inf[j] = inf[j], inf[i]  


# 그 숫자가 나왔었는지, 어디서 나왔었는지도 중요

T = int(input())
for tc in range(1, T + 1):
    inf_str, c = input().split()
    inf = list(inf_str)
    c = int(c) 
    result = 0  

    dfs(0, c)  

    print(f"#{tc} {result}")
