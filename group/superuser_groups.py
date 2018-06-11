import os
from pathlib import Path
from subprocess import call

import pandas as pd

def get_groups(proj_path):
    # list high level groups (/home/sdal/projects)
    sdal_projects = proj_path
    cats = os.listdir(sdal_projects)

    all_groups = set()

    # list project folders in each group
    for sponsor in cats:
        print('*' * 80)
        print(sponsor)
        if os.path.islink(sponsor):
            print('Found symlink, skipping directory...')
            continue
        else:
            sponsor_projects = os.listdir(sdal_projects + sponsor)
            print(sponsor_projects)
            for proj in sponsor_projects:
                proj_path = os.path.join(sdal_projects, sponsor, proj)
                print(proj_path)
                path_info = Path(proj_path)
                try:
                    print("Owner: {}".format(path_info.owner()))
                    print("Group: {}".format(path_info.group()))
                    grp = path_info.group()
                    all_groups.add(grp)
                except KeyError:
                    continue

    print(all_groups)
    return(all_groups)

if __name__ == '__main__':

    super_users = ['chend', 'ian85', 'aschroed', 'sallie41']
    all_groups = get_groups('/home/sdal/projects/')

    for gp in all_groups:
        for usr in super_users:
            call(['sudo', 'usermod', '-aG', gp, usr])

    base_groups = ['users', 'sdal', 'lightfoot']

    dspg18 = {'business_innovation': [],
              'oss': [],
              'stem_edu': [],
              'arl_dhs': [],
              'dhs_link_char': []
    }

# needs to be chown-d
# ari2
# arl_pd
# cpn
# rc (regional commission) - roa ala
# vt
# vce
# vdss
# umfs
# roanoke
