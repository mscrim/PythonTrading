"""
- Check that cache_dir exists, if not create it
- Map function and arguments to a filename
- See if file already exists
- If so, read in pickle
- Else, run function and pickle returned object
"""
import os
import pickle


def check_dir_exists(path):
    if not os.path.isdir(path):
        os.mkdir(path)
    if not os.path.isdir(path):
        raise Exception('Was unable to create directory {}'.format(path))

def simple_cache(func):
    def wrapper(*args):

        # Check that cache_dir exists, if not create it
        cache_dir = 'data'
        check_dir_exists(cache_dir)

        # Map func and its arguments to a filename
        filename = '_'.join([func.__name__] + [str(i) for i in args]) + '.pkl'
        filename = os.path.join(cache_dir, filename)

        # If pickle already exists, read it in
        if os.path.exists(filename):
            with open(filename, 'rb') as F:
                res = pickle.load(F)

        # Else run func and pickle its output
        else:
            res = func(*args)

            with open(filename, 'wb') as F:
                pickle.dump(res, F)

        return res
    return wrapper
