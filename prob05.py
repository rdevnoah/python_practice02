# 문제5.
# 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.


def mysum(*args):
    result = 0
    for n in args:
        result += n
    return result


print(mysum(2, 3, 4))