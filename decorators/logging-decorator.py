import functools
import time


def logging_decorator(func):
    stat_data = {
        'calls_count': 0,
        'total_time': 0,
        'avg_time': 0,
    }

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        process_time = time.time() - start_time
        stat_data['calls_count'] += 1
        stat_data['total_time'] += process_time
        stat_data['avg_time'] = stat_data['total_time'] / stat_data['calls_count']

        print(f'Function <{wrapper.__name__}> was called {stat_data["calls_count"]} times.'
              f' Total spent time in this function {stat_data["total_time"]} seconds,'
              f' {stat_data["avg_time"]} seconds in average')
        return result

    return wrapper


@logging_decorator
def sleeper():
    time.sleep(1)


if __name__ == '__main__':
    print(sleeper.__name__)
    sleeper()
    sleeper()
    sleeper()
    sleeper()
