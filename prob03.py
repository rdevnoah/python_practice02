# 다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복
# 없이 각 단어를 순서대로 출력하세요.
s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""
s = s.upper()
s = s.replace('.', '')
s = s.replace(',', '')
s = s.replace('\n', ' ')
l = s.split(' ')
s1 = set(l)
l1 = list(s1)
l1.sort()
for n in l1:
    print(n, l.count(n), sep=':')

