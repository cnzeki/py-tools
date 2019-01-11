# -*- coding:utf-8 -*-
from __future__ import print_function
import math
import time
import os
import sys
import shutil

    
def get_so_list_file(list_file):    
    so_set = set()
    with open(list_file, 'r') as f:
        for line in f.readlines():
            line = line.strip()
            s = line.find('/') 
            if s < 0:
                continue
            # 
            so_path = line[s:]
            so_set.add(so_path)
            
    so_list = list(so_set)
    return so_list

    
def get_comand_output(cmd):
    #output = subprocess.Popen([cmd],stdout=subprocess.PIPE,shell=True).communicate()
    #return output[0]
    process = os.popen(cmd) 
    output = process.read()
    process.close()
    return output


def get_so_list_lines(lines):    
    so_set = set()
    for line in lines:
        line = line.strip()
        s = line.find('/') 
        if s < 0:
            continue
        # 
        line_mid = line[s:]
        e = line_mid.find(' ')
        so_path = line_mid[:e]
        so_set.add(so_path)
            
    so_list = list(so_set)
    return so_list


def is_file_so(so_path):
    fpath, fname=os.path.split(so_path)
    if fname.endswith('.so'):
        return True
    return fname.find('.so.') >= 0
    
    
def copy_so_list(so_list, dst_dir):    
    error_list = []
    omit_list = []
    ok_count = 0
    for idx, so_path in enumerate(so_list):
        fpath, fname=os.path.split(so_path)
        dst_path = os.path.join(dst_dir, fname)
        stat = ' ok '
        # check so type
        if not is_file_so(so_path):
            stat = 'omit'
            omit_list.append(so_path)
            print('[%s] %3d: %s' % (stat, idx+1, so_path))
            continue
        try:
            shutil.copyfile(so_path, dst_path)
            ok_count += 1
        except:
            stat = 'fail'
            error_list.append(dst_path)
            pass
        print('[%s] %3d: %s' % (stat, idx+1, so_path))
    # report
    print('-'*80)
    print('Total  :%d\nSuccess:%d\nFail   :%d' % (len(so_list), ok_count, len(error_list)))
    # report failures
    if len(error_list) > 0:
        print('Failures:%d' %(len(error_list)))
        for idx, error in enumerate(error_list):
            try:
                print('\t%3d: %s' % error)
                os.remove(error)
            except:
                pass
    # report omit
    if len(omit_list) > 0:
        print('Omit list:%d' % len(omit_list))
        for error in enumerate(omit_list):
            print('\t%3d: %s' % error)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('bin|list depends-dir')
        sys.exit()

    bin_path = sys.argv[1]
    dst_dir = sys.argv[2]
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    # check input type
    _, ext = os.path.splitext(bin_path)
    if ext == '.list':
        so_list = get_so_list_file(bin_path)
    else:
        # get list from `ldd` command
        cmd = 'ldd %s' % bin_path
        output = get_comand_output(cmd)
        lines = output.splitlines()
        # parsing
        so_list = get_so_list_lines(lines)
    so_list.sort()
    copy_so_list(so_list, dst_dir)