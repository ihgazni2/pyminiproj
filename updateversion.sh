#
pip3 uninstall pyminiproj
git rm -r dist
git rm -r build
#
git rm -r pyminiproj.egg-info
rm -r dist
rm -r build
#
rm -r pyminiproj.egg-info
#
python3 setup_ver_update.py
git add .
git commit -m "remove old build"
git push origin master
python3 setup.py install --record install.txt
git add .
git commit -m "$1"
git push origin master

