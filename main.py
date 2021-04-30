import os

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

if __name__ == '__main__':
    init('my-sample-repo')
