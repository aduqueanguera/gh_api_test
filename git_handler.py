import os
import subprocess


class git_handler(object):
    ORIGIN = 'origin'
    MASTER_BRANCH = 'master'

    def __init__(self):
        self

    def checkout_branch(self, branch: str):
        process = subprocess.Popen(['git', 'checkout', branch], stdout=subprocess.PIPE)
        out, err = process.communicate()
        print('checkout branch ---> ', out)
        print('checkout branch ---> ', err)

    def diff(self):
        process = subprocess.Popen(['git', 'diff'], stdout=subprocess.PIPE)
        out, err = process.communicate()
        print('diff ---> ', out)
        print('diff ---> ', err)

    def add(self, files: str):
        process = subprocess.Popen(['git', 'add', files], stdout=subprocess.PIPE)
        out, err = process.communicate()
        print('add ---> ', out)
        print('add ---> ', err)

    def commit(self, msg: str):
        process = subprocess.Popen(['git', 'commit', '-m', msg], stdout=subprocess.PIPE)
        out, err = process.communicate()
        print('commit ---> ', out)
        print('commit ---> ', err)

    def push(self, branch: str):
        process = subprocess.Popen(['git', 'push', git_handler.MASTER_BRANCH, branch], stdout=subprocess.PIPE)
        out, err = process.communicate()
        print('push ---> ', out)
        print('push ---> ', err)


def main():
    git = git_handler()
    git.checkout_branch(branch='tercera_rama')
    git.diff()
    git.add('--all')
    git.commit('comiteando')
    git.push(branch=tercera_rama)


if __name__ == '__main__':
    main()
