# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
s = '/usr/local/bin/python'

l = s.split('/')
l.remove('')
print(l)

directory = '/'

for n in range(0, len(l)-1):
    directory += l[n] + '/'

exe = l[len(l)-1]
print(directory, exe, sep=',')

