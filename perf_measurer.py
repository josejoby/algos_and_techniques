from time import perf_counter

def log_time(func):

    def inner(*args, **kwargs):
        t = perf_counter()
        result = func(*args, **kwargs)
        took = perf_counter()-t
        print(f"{func.__name__} took {took*1000} ms")
        return result

    return inner
    