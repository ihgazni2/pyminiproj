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


License
=======

- MIT


