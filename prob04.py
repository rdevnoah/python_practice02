# 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에
# 출력해보세요. 1부터 99까지만 실행하세요.

d = {}
for i in range (0, 100):
    s = str(i)
    if '3' in s or '6' in s or '9' in s:
        d.update({i: int(s.count('3')) + int(s.count('6')) + int(s.count('9'))})


d2 = d.items()

for k, v in d2:
    s = ''
    for j in range(0, v):
        s += '짝'
    print(k, s)
