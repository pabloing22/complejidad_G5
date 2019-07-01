from time import time,clock

def delta_time(n):
    def count_elapsed_time(f):
       
        def w(*args, **kwargs):
            # Start counting.
            start_time = clock()
            # Take the original function's return value.
            ret = f(*args, **kwargs)
            # Calculate the elapsed time.
            elapsed_time = (clock()) - start_time
            print(n+"--> Tardo: %.8f Seconds."% elapsed_time)
            return ret
        
        return w
    return count_elapsed_time