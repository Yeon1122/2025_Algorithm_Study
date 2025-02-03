############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.

def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    #user_data 딕셔너리의 키 id의 value 값의 가장 마지막 자리를 id_lastletter 변수에 저장합니다.
    id_lastletter = user_data['id'][-1]

    #id의 마지막 글자가 0부터 9 사이인 숫자로 끝나야 하니 반복문을 사용한다.
    for i in range(10):
        #추출한 id_lastletter의 type은 string이라 검증할 0-9를 string으로 타입 변환하여 비교한다.
        if id_lastletter == str(i):
            #동일하면 True 반환
            return True
    #True를 반환하지 못했다면 루프 종료 후 False를 반환한다.    
    return False   

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True


user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################