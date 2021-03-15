"""
- Check that CACHE_DIR exists, if not create it
- Map function and arguments to a filename
- See if file already exists
- If so, read in pickle
- Else, run function and pickle returned object
"""
import os
import pickle

CACHE_DIR = 'data'

def check_dir_exists(path):
    if not os.path.isdir(path):
        os.mkdir(path)
    if not os.path.isdir(path):
        raise Exception('Was unable to create directory {}'.format(path))

def simple_cache(func):
    def wrapper(*args, **kwargs):

        # Check that CACHE_DIR exists, if not create it
        check_dir_exists(CACHE_DIR)

        # Map func and its arguments to a filename
        filename = '_'.join([func.__name__] + [str(i) for i in args] 
                            + [str(i) for i in list(kwargs.values())]) + '.pkl'
        filename = os.path.join(CACHE_DIR, filename)
        print(filename)

        # If pickle already exists, read it in
        if os.path.exists(filename):
            print('cache exists, loading pickle')
            with open(filename, 'rb') as F:
                res = pickle.load(F)

        # Else run func and pickle its output
        else:
            print('no cache exists, fetching data')
            res = func(*args, **kwargs)

            with open(filename, 'wb') as F:
                pickle.dump(res, F)

        return res
    return wrapper
