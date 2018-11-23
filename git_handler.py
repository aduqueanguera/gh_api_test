import os
import subprocess


class git_handler(object):
    ORIGIN = 'origin'
    MASTER_BRANCH = 'master'

    def __init__(self):
        pass

    @staticmethod
    def checkout_branch(branch: str):
        process = subprocess.Popen(['git', 'checkout', branch], stdout=subprocess.PIPE)
        out = process.communicate()
        print('checkout branch ---> ', out)

    @staticmethod
    def diff():
        process = subprocess.Popen(['git', 'diff'], stdout=subprocess.PIPE)
        out = process.communicate()
        print('diff ---> ', out)

    @staticmethod
    def add(files: str):
        process = subprocess.Popen(['git', 'add', files], stdout=subprocess.PIPE)
        out = process.communicate()
        print('add ---> ', out)

    @staticmethod
    def commit(msg: str):
        process = subprocess.Popen(['git', 'commit', '-m', msg], stdout=subprocess.PIPE)
        out = process.communicate()
        print('commit ---> ', out)

    @staticmethod
    def push(branch: str):
        process = subprocess.Popen(['git', 'push', git_handler.ORIGIN, branch], stdout=subprocess.PIPE)
        out = process.communicate()
        print('push ---> ', out)


def main():
    git = git_handler()
    git.checkout_branch(branch='tercerra_rama')
    git.diff()
    git.add('--all')
    git.commit('comiteando')
    git.push(branch='tercera_rama')


if __name__ == '__main__':
    main()
