"""
피보나치 수열이란 첫 번째 항과 두 번째 항이 1이고,
세 번째 항부터는 바로 앞의 두 항의 합으로 정의된 수열입니다.
예를 들어서 세 번째 항은 첫 번째 항(1)과 두 번째 항(1)을 더한 2이며,
네 번째 항은 두 번째 항(1)과 세 번째 항(2)을 더한 3이 될 것입니다.

파라미터로 1 이상의 자연수 **`n`**을 받고, n번째 피보나치 수를 리턴하는
재귀 함수 fibonacci 함수를 작성하세요. 예를 들어 n = 3이라면 2를 반환해주면 됩니다.

입력>
print(fibonacci(10))

출력>
55
"""

def fibonacci(num):
    if num<=1:
        return num
    print('{} + {} = {}'.format(fibonacci(num-1),fibonacci(num-2),fibonacci(num-1)+fibonacci(num-2)))
    print('---------------------------------')
    return fibonacci(num-1)+fibonacci(num-2)


print(fibonacci(3))
