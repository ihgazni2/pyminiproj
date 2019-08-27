from setuptools import setup, find_packages
setup(
      name="pyminiproj",
      version = "0.1",
      description="creat a python project template DIR , includes some shell-scripts for git and pypi",
      author="dli",
      url="https://github.com/ihgazni2/pyminiproj",
      author_email='ihgazni2010@hotmail.com', 
      license="MIT",
      long_description = "refer to .md files in https://github.com/ihgazni2/pyminiproj",
      entry_points = {
         'console_scripts': ['pyminiproj=pyminiproj.bin:main']
      },
      classifiers=[
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Programming Language :: Python',
          ],
      packages= find_packages(),
      py_modules=['pyminiproj'], 
      )


# python3 setup.py bdist --formats=tar
# python3 setup.py sdist

