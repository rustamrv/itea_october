from functools import wraps
import time


def decorator(count_repetitions=3):
    def actual_decorator(func):
        @wraps(func)
        def wrapper(count):
            result = dict()
            result['name_func'] = wrapper.__name__
            arr = []
            all_time = 0
            for i in range(0, count_repetitions):
                start_time = time.time()
                res = func(count+i)
                print("-" * 5)
                end_time = time.time() - start_time
                arr.append(end_time)
                all_time += end_time
                result['last_result'] = res
            result['func_time'] = arr
            result['all_time'] = all_time
            return result

        return wrapper
    return actual_decorator


def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)


@decorator(5)
def target_f(n):
    res = fib(n)
    print(f"Число Фибоначчи {n} = {res}")
    return res


if __name__ == "__main__":
    result = target_f(25)
    for k, v in result.items():
        print(k, v)
