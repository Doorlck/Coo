##0##
# 잡것..
import week01 # week01, week01파일에서 18번째 줄로 인해 week01이 출력이 됨.
print(__name__) # __main__
# 출력결과:
#          week01
#          __main__

if __name__ == "__main__":
    print("HELLO SUN")


##1##
#  재귀함수: 팩토리얼 함수
# def factorial(n):
#     if n <= 0:
#         return 1
#     return n*factorial(n-1)

# if __name__=="__main__": # 이 파일이 메인인 것은 어떻게 확인하지.. > print를 찍어보자
#     for i in range(1,6):
#         print(factorial(i))


##2##
# 재귀함수: 배열의 경우의 수 
def permutation(arr, start):
    if len(arr)-1 == start:
        print(arr)
        return

    for idx in range(start, len(arr)):
        arr[start], arr[idx] = arr[idx], arr[start]
        permutation(arr, start+1)
        arr[start], arr[idx] = arr[idx], arr[start]

if __name__=="__main__":
    arr=[1, 2, 3]
    permutation(arr, 0)