import sys


def yes_no(prompt, retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input(prompt)
        if ok in ('y', 'ye', 'yes', 'Y', 'Ye', 'Yes', 'YES'):
            return True
        if ok in ('n', 'no', 'nop', 'nope', 'N', 'No', 'NO'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

yes_no("Would you like to continue (Y/N): ")
