pip3 uninstall pyminiproj
git rm -r dist
git rm -r build
git rm -r pyminiproj.egg-info
rm -r dist
rm -r build
rm -r pyminiproj.egg-info
git add .
git commit -m "remove old build"

