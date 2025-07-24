
def subtract(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('숫자만 입력 가능합니다.')
    return a - b