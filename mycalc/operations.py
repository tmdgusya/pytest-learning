
def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('숫자만 입력 가능합니다.')
    return a - b

def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('숫자만 입력이 가능합니다.')
    if b == 0:
        raise ZeroDivisionError('0으로 나눌 수 없습니다')
    return a / b