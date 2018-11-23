import os
import subprocess


def checkout_branch(branch: str):
    process = subprocess.Popen(['git', 'checkout', branch], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print('checkout branch ---> ', out)
    print('checkout branch ---> ', err)


def diff():
    process = subprocess.Popen(['git', 'diff'], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print('diff ---> ', out)
    print('diff ---> ', err)


def add(files: str):
    process = subprocess.Popen(['git', 'add', files], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print('add ---> ', out)
    print('add ---> ', err)


def commit(msg: str):
    process = subprocess.Popen(['git', 'commit', '-m', msg], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print('commit ---> ', out)
    print('commit ---> ', err)

def main():
    checkout_branch(branch='tercera_rama')
    diff()
    add('--all')
    commit('comiteando')

if __name__ == '__main__':
    main()
