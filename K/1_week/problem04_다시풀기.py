############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 set, sum 등 사용 시 감점

def analyze_items(items_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if items_list:
        for i in range(len(items_list)-1,0,-1):
            for j in range(0,i):
                if items_list[i]==items_list[j]:
                    items_list.pop(i)
        
        sum_plus=0
        sum_minus=0
        for item in items_list:
            if isinstance(item,int) and item>0:
                sum_plus+=item
            if isinstance(item,int) and item<0:
                sum_minus+=item
        return items_list, (sum_plus,sum_minus)

    else:
        return items_list,(0,0)
    


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(analyze_items([2, 2, 2, "a", "a", 3, 0, -2]))
# 예시 결과: ([2, "a", 3, 0, -2], (5, -2))

print(analyze_items([]))
# 예시 결과: ([], (0, 0))

print(analyze_items(["apple", "apple", "banana"]))
# 예시 결과: (["apple", "banana"], (0, 0))
#####################################################
