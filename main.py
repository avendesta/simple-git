import os
import hashlib
import zlib

# Initializing a git repository
def init(repo):
    ''' Create directory for repo and initialize .git directory. '''
    os.mkdir(repo)
    os.mkdir(os.path.join(repo, '.git'))
    for name in ['objects', 'refs', 'refs/heads']:
        os.mkdir(os.path.join(repo, '.git', name))
    with open(os.path.join(repo, '.git', 'HEAD'), 'wb') as f:
        f.write(b'ref:refs/heads/master')
    print(f'initialized empty repository: {repo}')

# Hashing objects
def hash_object(data, obj_type, write=True):
    ''' Compute has of object data of a given type and write to object
    store if "write" is True. Return SHA-1 object hash as hex string.
    '''
    header = f"{obj_type} {len(data)}".encode()
    full_data = header+b'\x00'+data
    sha1 = hashlib.sha1(full_data).hexdigest()
    print(sha1)
    if write:
        path = os.path.join('.git', 'objects', sha1[:2], sha1[2:])
        if not os.path.exists(path):
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'wb') as f:
                f.write(zlib.compress(full_data))
    return sha1


if __name__ == '__main__':
    init('my-sample-repo')
    os.chdir('my-sample-repo')
    hash_object(b'test data', 'object type', True)
