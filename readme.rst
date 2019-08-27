.. contents:: Table of Contents
   :depth: 5


*pyminiproj*
------------

- creat a python project template DIR 
- generate some shell-scripts for git and pypi


Installation
============

    ::
    
        pip3 install pyminiproj


Usage
=====

INIT
~~~~

- first creat a rep on github.com, such as **tstproj**
- 
- cd  WKDIR
- **pyminiproj -projname tstproj -username ihgazni2 -scheme git**
- cd **tstproj/**
- **./INIT/init.sh**
- 
- goto github.com check it

    ::
        
        cd  WKDIR
        
        pyminiproj -projname tstproj -username ihgazni2 -scheme git
        
        cd tstproj/
        
        ./INIT/init.sh
        
        #and will generate the below  files and dirs, its enough for a small python project
        
        tstproj# tree
        .
        ├── BACKUP
        │   └── dummy
        ├── docs
        │   └── dummy
        ├── DRAFT
        │   └── dummy
        ├── INIT
        │   ├── credential.sh
        │   └── init.sh
        ├── install.sh
        ├── install.txt
        ├── LICENSE
        ├── MANIFEST.in
        ├── pypiupload.sh
        ├── README.md
        ├── readme.rst
        ├── RESOURCES
        │   └── dummy
        ├── setup.py
        ├── setup_ver_update.py
        ├── srch.py
        ├── TEST
        │   └── dummy
        ├── tstproj
        │   ├── bin.py
        │   ├── Images
        │   │   └── dummp
        │   ├── __init__.py
        │   └── ReadMeDetailed
        │       └── dummy
        ├── uninstall.sh
        └── updateversion.sh
        
        9 directories, 23 files
        

UPDATE
~~~~~~

-   modify a file
-   **./updateversion.sh** "commit message"

    ::
        
        tstproj# touch tstproj/tstproj.py
        tstproj#
        tstproj# ./updateversion.sh "first commit"


PYPI 
~~~~

- **./pypiupload.sh**


FIND CONTENT  
~~~~~~~~~~~~

- **python3 srch.py** "string"

    ::
        
        tstproj# python3 srch.py "tstproj"
        ---location---
        cat ./build/lib/tstproj/bin.py
        ---rslt----
        import tstproj
            print("command line bin of tstproj !!")
        
        ----info---
        
        ---location---
        cat ./dist/tstproj-0.0.2-py3.6.egg
        ---rslt----
        Binary file (standard input) matches
        
        ----info---
        
        ---location---
        cat ./INIT/init.sh
        ---rslt----
            git remote add origin https://github.com:ihgazni2/tstproj.git
            git remote add origin-git git@github.com:ihgazni2/tstproj.git
            git remote add origin-https https://github.com:ihgazni2/tstproj.git
            git remote add origin git@github.com:ihgazni2/tstproj.git
        ......

CREDENTIAL
~~~~~~~~~~

- if you use https scheme ,such as https://github.com/ihgazni2/tstproj.git
- open **./INIT/credential.sh** ,check it and make sure you will exec it

    ::
        
        ./INIT/credential.sh


CLI HELP
~~~~~~~~
    
    ::
        
        # pyminiproj -h
        usage: pyminiproj [-h] [-projname PROJNAME] [-username USERNAME]
                          [-password PASSWORD] [-email EMAIL] [-scheme SCHEME]
                          [-author AUTHOR]
        
        optional arguments:
          -h, --help            show this help message and exit
          -projname     PROJNAME,   --projname PROJNAME  git repository names
          -username     USERNAME,   --username USERNAME  git config --local user.name
          -password     PASSWORD,   --password PASSWORD  git password
          -email        EMAIL,      --email EMAIL        git config --local user.email
          -scheme       SCHEME,     --scheme SCHEME      https or git
          -author       AUTHOR,     --author AUTHOR      used in setup.py.dflt is same with username
        


DEPENDANCY
==========

- `efdir <https://github.com/ihgazni2/efdir>`__


License
=======

- MIT


