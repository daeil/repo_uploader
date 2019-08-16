#!/usr/bin/env python

import os
import sys
import subprocess

#############################################
### Plz change below for your environment ###

#SERVER='sel-odyssey-git.wrs.com'
SERVER='sel-odyssey-git.wrs.com'
SOURCE_DIR='/home/dkwon/Projects/PIVI/source/'
BRANCH_NAME='proteus_release'

#############################################


def upload_proj(proj_path, proj_name):
    if not proj_name: return
    print "upload_proj", proj_path, proj_name
    os.chdir(SOURCE_DIR + proj_path)
    cmd = 'git remote add %s ssh://%s/%s' % (BRANCH_NAME, SERVER, proj_name)
    subprocess.call(cmd, shell=True)
    cmd = 'git remote set-url %s ssh://%s/%s' % (BRANCH_NAME, SERVER, proj_name)
    subprocess.call(cmd, shell=True)
    #cmd = 'git push --no-thin -o skip-validation --no-verify %s %s' % (BRANCH_NAME, BRANCH_NAME)
    cmd = 'git push %s %s' % (BRANCH_NAME, BRANCH_NAME)
    subprocess.call(cmd, shell=True)

def create_proj(proj_name):
    if not proj_name: return
    print "proj_name", proj_name
    #subprocess.call(["ssh", "pivot", "gerrit", "create-project", proj_name])
    cmd = 'ssh ' + SERVER + ' gerrit create-project --empty-commit ' + proj_name
    subprocess.call(cmd, shell=True)

def main(project_list):
    f = open(project_list)
    for proj in f:
        proj_path = proj.split(' : ')[0]
        proj_name = proj.split(' : ')[1]
        #create_proj(proj_name)
        upload_proj(proj_path, proj_name)
    f.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print sys.argv[0], "project_list_file"
        exit()
    main(sys.argv[1])

