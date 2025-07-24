
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError('입력값은 숫자여야 합니다.')
    return a + b