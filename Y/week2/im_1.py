###############################################
#
#
# 
#
#
# 
# 
# 
# 
###############################################

#변수
N, t1, t2 = list(map(int, input().split()))
t1_min = min(t1, t2)
t2_max = max(t1, t2)

tower_1 = []
tower_2 = []
box = list(map(int, input().split()))

box.sort(reverse=True)
#print(box, t1_min, t2_max, tower_1, tower_2)

for i in range(N):
    box_pop = box.pop(0)
    # print(i)
    # print(tower_1, tower_2) 
    if i // 2 < t1_min:
        if i%2 == 0:
            tower_1.append(box_pop)
        else:
            tower_2.append(box_pop)
    else:
        tower_2.append(box_pop)

print(tower_1, tower_2)

def box_sum(li_len, li):
    box_sum_result = 0
    for i in range(li_len):
        # print(i)
        box_sum_result += li[i]*(i+1)
        #print(box_sum_result)
    return box_sum_result

box_tower_1 = box_sum(t1_min, tower_1)
box_tower_2 = box_sum(t2_max, tower_2)
print(box_tower_1+box_tower_2)

# box_sum(t1_min, tower_1)
# box_sum(t2_max, tower_2)
# print(box_tower_1)
# print(box_tower_2)

# box_sum(t2, tower_2)