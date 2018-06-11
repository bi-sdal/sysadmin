from subprocess import call

import pandas as pd
from numpy import vectorize

gp_df = pd.read_csv('groups.csv')

print('sort by group:')
print(gp_df.sort_values(['group', 'pid']))
print('sort by pid:')
print(gp_df.sort_values(['pid', 'group']))

@vectorize
def add_user_to_group(gp, usr):
    print(f'Adding user:{usr} to group:{gp}')
    call(['sudo', 'usermod', '-aG', gp, usr])
    return None

add_user_to_group(gp_df['group'], gp_df['pid'])
