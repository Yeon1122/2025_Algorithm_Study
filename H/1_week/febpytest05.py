def count_happy(diary):
    result_value = 0
    search_word = "happy"
    word_length = len(search_word)
    diary_length = len(diary)

    for i in range(diary_length - word_length + 1):  # 문자열을 순차적으로 탐색
        if diary[i:i+word_length] == search_word:  # 현재 부분 문자열이 'happy'인지 확인
            result_value += 1

    return result_value

# TC
print(count_happy("I feel happy. HAPPY! so happy!"))  # 2
print(count_happy("happyhappy"))                      # 2
print(count_happy("nothing here"))                    # 0
print(count_happy("happy happy happy!"))              # 3
print(count_happy("haphappyhappyhappyend"))           # 3
