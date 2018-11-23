import os
import subprocess


class git_handler(object):
    ORIGIN = 'origin'
    MASTER_BRANCH = 'master'

    def __init__(self):
        pass

    def checkout_branch(self, branch: str):
        process = subprocess.Popen(['git', 'checkout', branch], stdout=subprocess.PIPE)
        out = process.communicate()
        print('checkout branch ---> ', out)

    def diff(self):
        process = subprocess.Popen(['git', 'diff'], stdout=subprocess.PIPE)
        out = process.communicate()
        print('diff ---> ', out)

    def add(self, files: str):
        process = subprocess.Popen(['git', 'add', files], stdout=subprocess.PIPE)
        out = process.communicate()
        print('add ---> ', out)

    def commit(self, msg: str):
        process = subprocess.Popen(['git', 'commit', '-m', msg], stdout=subprocess.PIPE)
        out = process.communicate()
        print('commit ---> ', out)

    def push(self, branch: str):
        process = subprocess.Popen(['git', 'push', git_handler.MASTER_BRANCH, branch], stdout=subprocess.PIPE)
        out = process.communicate()
        print('push ---> ', out)


def main():
    git = git_handler()
    git.checkout_branch(branch='tercera_rama')
    git.diff()
    git.add('--all')
    git.commit('comiteando')
    git.push(branch='tercera_rama')


if __name__ == '__main__':
    main()
