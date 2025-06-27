def fibo(n):
    """
    n번째 피보나치 수를 재귀적으로 반환
    Args:
        n (int): 0 이상의 정수
    Returns:
        int: n번째 피보나치 수
    """
    if n < 0:
        raise ValueError("Input cannot be a negative number.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)

if __name__ == "__main__":
    # 예시: fibo(4)는 3이 나와야 함
    print(f"fibo(4) = {fibo(4)}")

