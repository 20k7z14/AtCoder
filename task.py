import sys
import os
import glob
import shutil

collected_items = glob.glob(r'./collection_point/*.py')
collected_items = [i.replace('\\','/') for i in collected_items]
collected_items.sort()

for item in collected_items:
    file_name = item.split('/')[2]
    contest_name,time_name = file_name[:3],file_name[3:6]

    if os.path.isdir(f'/{contest_name}'):
        pass
    else:
        os.mkdir(f'/{contest_name}')

    if os.path.isdir(f'/{contest_name}/{time_name}'):
        pass
    else:
        os.mkdir(f'/{contest_name}/{time_name}')

    shutil.move(item,f'/{contest_name}/{time_name}/')
