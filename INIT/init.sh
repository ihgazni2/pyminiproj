#! /bin/bash
scheme="git"
git init


if [$scheme == "https"];then
    echo "$scheme is https"
    git remote add origin https://github.com:ihgazni2/pyminiproj.git
    git remote add origin-git git@github.com:ihgazni2/pyminiproj.git
    git remote add origin-https https://github.com:ihgazni2/pyminiproj.git
fi

if [$scheme == "git"];then
    echo "$scheme is git"
    eval `ssh-agent`
    ssh-add
    git remote add origin git@github.com:ihgazni2/pyminiproj.git
    git remote add origin-git git@github.com:ihgazni2/pyminiproj.git
    git remote add origin-https https://github.com:ihgazni2/pyminiproj.git
fi

git config --local user.name ihgazni2
git config --local user.email ihgazni2010@hotmail.com
git remote -v
git pull origin master
git add .
git commit -m "first commit"
git push origin master

