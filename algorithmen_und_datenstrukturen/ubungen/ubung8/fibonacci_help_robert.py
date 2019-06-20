from multiprocessing import Process, Queue, TimeoutError
import sys


def run_10s(function, *args, **kwargs):
    '''
    Run `function` with given arguments for at most 10 seconds.
    If it terminates before that, its return value is returned.
    If an exception is raised within 10 seconds, that exception is propagated.
    If it does not terminate within 10 seconds, a `TimeoutError` is raised.
    '''
    def execute(queue):
        sys.stdout = None  # suppress output
        sys.stderr = None
        try:
            queue.put(function(*args, **kwargs))
        except BaseException as e:
            queue.put(e)
            raise e

    queue = Queue()
    process = Process(target=execute, args=(queue,))
    process.start()
    # wait until process stops or 10s have passed
    process.join(10)
    if process.is_alive():
        process.terminate()
        raise TimeoutError('10s exceeded')
    elif process.exitcode != 0:
        exception = queue.get()
        assert isinstance(exception, BaseException)
        raise exception
    else:
        result = queue.get()
        return result
