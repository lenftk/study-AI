#"123123" 큰따움표 안에 둘러싸여있으면 숫자더라도 문자로 처리한다!
"Hello World"
'python is fun(?)'
"""what is python I don't like it"""
'''lenftk is my github name'''
#문자열을 만드는 방식은 위와 같이 4가지가 있다.

from email.errors import FirstHeaderLineIsContinuationDefect
string = "Hello World"
#문자열을 변수로 저장할때는 큰따옴표 사용하기
#ex)
>>> food = 'Python's favorite food is perl'
  File "<stdin>", line 1
    food = 'Python's favorite food is perl'
                   ^
SyntaxError: invalid syntax
#위와 같이 작은 따옴표를 사용하면 오류가 발생한다. 

#문자열에 큰따옴표를 넣을때는 작은 따옴표로 구분
say = '"Python is very easy." he says.'

#작은따옴표나 큰따옴표를 문자열에 포함시키는 또 다른 방법은
# 역슬래시(\)를 사용하는 것이다. 역슬래시를 작은따옴표나 큰따옴표 앞에 삽입하면
# 역슬래시 뒤의 작은따옴표나 큰따옴표는 문자열을 둘러싸는 기호가 아니라
# 문자 그 자체를 뜻한다.
say = "He said, \"Python is very easy.\""
print(say)
#result = He said, "Python is very easy."

#줄바꿈 (이스케이프 코드)
string = "hello\nworld"
string = """
hello
world
"""
string = '''
hello
world
'''

#\n	문자열 안에서 줄을 바꿀 때 사용
#\t	문자열 사이에 탭 간격을 줄 때 사용
#\\	\를 그대로 표현할 때 사용
#\'	작은따옴표(')를 그대로 표현할 때 사용
#\"	큰따옴표(")를 그대로 표현할 때 사용
#\r	캐리지 리턴(줄 바꿈 문자, 커서를 현재 줄의 가장 앞으로 이동)
#\f	폼 피드(줄 바꿈 문자, 커서를 현재 줄의 다음 줄로 이동)
#\a	벨 소리(출력할 때 PC 스피커에서 '삑' 소리가 난다)
#\b	백 스페이스
#\000	널 문자


#문자열 연산(?)
first = "Hello"
second = " World"
print(first + second)
#result = Hello World

a = "python"
print(a * 3)
#result = pythonpythonpython

#문자열 길이
lenftk = "this is my github name"
print(len(lenftk))
#result = 21

#문자열 인덱싱 & 슬라이싱
#indexing 가리키는것, slicing 잘라낸다는것

a = 'python'
print(a[3])
#result = h 컴퓨터는 0부터 시작임을 잘 알아둘것 즉, 3이면 4번째 글자가 인덱싱 된다
#a[-1]뒤에서 시작해서 첫번째 글자 그럼 a[-0]는? 뒤에서 0번째 글자 즉 첫번째 글자와 같다.

print(a[0:3])
#result = pyt 이렇게 통으로 뽑아오는 방법이 슬라이싱 이다.
#0:3 0 <= a < 3

#문자열 바꾸기
a = 'pithon'
a[1] = 'y'
#result = error 문자열의 요솟값은 변경 불가능!
print(a[:1] + 'y' + a[2:])
#result = python

#문자열 포매팅
"현재 온도는 %d도 입니다." % 30
#result = 현재 온도는 30도 입니다.
"I eat %s apples." % "five"
#result = I eat five apples.
# 숫자는 %d 문자는  %s

"현재 온도는 %d도 이고 나는 사과를 %d개 먹었다" % (30, 5)
#result = 현재 온도는 30도 이고 나는 사과를 5개 먹었다

# %s	문자열(String)
# %c	문자 1개(character)
# %d	정수(Integer)
# %f	부동소수(floating-point)
# %o	8진수
# %x	16진수
# %%	Literal % (문자 % 자체)
# %d%(x) => %d%%(o)

"%10s" % "hi"
#result = '     hi'
# 10은 10칸을 차지하고 오른쪽 정렬로 hi를 놓겠다는 의미

"%-10sjane." % 'hi'
#result = 'hi        jane.'
# -10은 10칸을 차지하고 왼쪽 정렬로 hi를 놓겠다는 의미

"%0.5f" % 3.14159265358979
#result = 3.14159
#소수점 5자리까지 표현하겠다는 의미 0생략 가능 %.5f

"%10.5f" % 3.14159265358979
#result = '     3.14159'
#10칸을 차지하고 오른쪽 정렬로 3.14159를 놓겠다는 의미

"I eat {0} apples".format(5)
#result = I eat 5 apples

"I eat {0} apples".format("five")
#result = I eat five apples

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)
#result = I ate 10 apples. so I was sick for three days.

"I ate {number} apples. so I was sick for {day} days.".format(number=10, day=3)
#result = I ate 10 apples. so I was sick for 3 days.

"{0:<10}".format("hi")
#result = 'hi        '
# 10칸을 차지하고 왼쪽 정렬로 hi를 놓겠다는 의미

"{0:>10}".format("hi")
#result = '        hi'
# 10칸을 차지하고 오른쪽 정렬로 hi를 놓겠다는 의미

"{0:^10}".format("hi")
#result = '    hi    '
# 10칸을 차지하고 가운데 정렬로 hi를 놓겠다는 의미

"{0:=^10}".format("hi")
#result = '====hi===='
# 10칸을 차지하고 가운데 정렬로 hi를 놓겠다는 의미

"{0:!<10}".format("hi")
#result = 'hi!!!!!!!!'
# 10칸을 차지하고 왼쪽 정렬로 hi를 놓겠다는 의미

"{{ and }}".format()
#result = '{ and }'
# 중괄호를 문자열로 처리하고 싶을때는 {{}}를 사용

name = '홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
#result = 나의 이름은 홍길동입니다. 나이는 30입니다.
#접두사

age = 30
f'나는 내년이면 {age + 1}살이 된다.'
#result = 나는 내년이면 31살이 된다.

d = {'name':'홍길동', 'age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'
#result = 나의 이름은 홍길동입니다. 나이는 30입니다.


f"난 {1500000:,}원이 필요해"
#result = 난 1,500,000원이 필요해
#콤마를 사용하면 3자리마다 ,를 추가한다.

#문자 개수 세기
a = "hobby"
a.count('b')
#result = 2

#위치 찾기1
a = "python"
a.find('o')
#result = 4
#문자열 없을때 -1 반환

#위치 찾기2
a = "python"
a.index('o')
#result = 4
#문자열 없으면 에러남

#문자열 삽입
",".join('abcd')
#result = 'a,b,c,d'

#소문자를 대문자로 바꾸기
a = "python"
a.upper()
#result = 'PYTHON'

#대문자를 소문자로 바꾸기
a = "python"
a.lower()
#result = 'python'

#왼쪽 공백 지우기
a = " python"
a.lstrip()
#result = 'python'

#오른쪽 공백 지우기
a = "python "
a.rstrip()
#result = 'python'

#양쪽 공백 지우기
a = " python "
a.strip()
#result = 'python'

#문자열 바꾸기
a = "python"
a.replace('python', 'java')
#result = 'java'

#문자열 나누기
>>> a = "Life is too short"
a.split()
#result = ['Life', 'is', 'too', 'short']
b = "a:b:c:d"
b.split(':')
#result = ['a', 'b', 'c', 'd']

#is alphabet?
s = "Python"
s.isalpha()
#result = True
s = "Python3"
s.isalpha()
#result = False
s = "Hello World"
s.isalpha()
#result = False

#is number?
s = "123"
s.isdigit()
#result = True
s = "123abc"
s.isdigit()
#result = False

#문자열이 특정 문자열로 시작하는지 확인
s = "Life is too short"
s.startswith("Life")
#result = True
s.startswith("short")
#result = False

#문자열이 특정 문자열로 끝나는지 확인
s = "Life is too short"
s.endswith("short")
#result = True
s.endswith("Life")
#result = False