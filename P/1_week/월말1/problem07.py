############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# 반드시 재귀 함수 형태로 구현해야 합니다.
def reverse_string(s):
    n = len(s)
    # 인자로 받은 string의 길이가 0이나 1이라면 자기 자신 반환
    if 0 <= n <= 1:
        return s
    # 1 이상이라면 마지막 글자와 마지막 글자를 뺀 string을 인자로 받은 이 함수의 반환값을 붙여 반환
    else:
        return s[-1] + reverse_string(s[:n-1])
    

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(reverse_string("hello"))  # "olleh"
print(reverse_string("world"))  # "dlrow"
print(reverse_string("python"))  # "nohtyp"
#####################################################
