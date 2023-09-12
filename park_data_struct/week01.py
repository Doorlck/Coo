##1##
# solution 정의를 보면 함수인데 왜 괄호가 없을까. 괄호가 없이 정의가 됐는데 왜 함수일까.
solution = int.__add__
print(solution(1,2))

'''
def ff():
    print()
a = ff 
a()

괄호가 없는 것은 함수의 주소를 받아오기만해서임. 
실제로 실행을 하려면 당연히 괄호가 필요함.
위의 예시 코드를 보면 함수ff의 주소를 받아오는 변수 a, 실제 함수 정의엔 ()있음.
'''

##2##
# week01과 data_struct_01의 __name__의 차이를 알아보시오.
print(__name__)

'''
실행되고있는 파일의 이름은 무조건 __main__이지만, 
파일을 참조하게 된다면 해당 파일의 이름이 __name__의 결과로 출력이 됨.
즉, data_struct_01.py에서 import week01을 한 후 실행을 하면 week01.py의 print(__name__)은 week01이 됨.
'''

##3##
