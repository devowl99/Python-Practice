def solution(phone_number):
    answer = '*'*(len(phone_number)-4)
    back = phone_number[-4:]

    return answer+back