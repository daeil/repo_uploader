# REPO uploader
This is a small script to upload all gerrit repositories from your local PC to new gerrit server.
This might be helpful to setup the local mirror server.

## Prerequsites
1. create project.list file from existing source tree
```
repo list > project.list
```

2. Specify your environments into repo-uploader.py
- server address
- source directory in your local PC
- branch name for uploaded projects

## Upload all projects
```
python repo-uploader.py project.list
```
