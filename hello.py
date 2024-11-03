import traceback
import math

# 汎用例外ラップ関数
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            print(f"Exception caught in {func.__name__}:")
            traceback.print_exc()
            print("#" * 10)
    return wrapper

@handle_exceptions
def raise_value_error():
    raise ValueError("A ValueError occurred")

@handle_exceptions
def divide_by_zero():
    result = 1 / 0

@handle_exceptions
def math_domain_error():
    result = math.sqrt(-1)

@handle_exceptions
def simulate_connection_error():
    # 模擬的な接続エラーを発生させる
    import requests
    # WARN: 私が試した当初は以下のドメインを利用しましたが、将来的には動作保証が担保できていないためコメントアウトしています。
    # 実際に試す場合は、自己責任でお願いします。
    # requests.get('http://invalid-url')

def main():
    print("Hello from traceback-tmp!")

    # 各種エラーを試す
    raise_value_error()        # ValueError
    divide_by_zero()           # ZeroDivisionError
    math_domain_error()        # math domain error
    simulate_connection_error() # 模擬的な接続エラー

if __name__ == "__main__":
    main()
