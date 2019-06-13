# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
s = '/usr/local/bin/python'

l = s.split('/')
l.remove('')
print(l)

l2 = s.split(l[len(l)-1])

print(l2[0], l[len(l)-1], sep=',')

