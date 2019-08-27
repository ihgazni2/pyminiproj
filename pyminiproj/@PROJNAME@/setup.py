from setuptools import setup, find_packages
setup(
      name="@projname@",
      version = "0.1",
      description="handle,.in progressing..,APIs",
      author="@author@",
      url="https://github.com/@username@/@projname@",
      author_email='@email@', 
      license="MIT",
      long_description = "refer to .md files in https://github.com/@username@/@projname@",
      classifiers=[
          'Environment :: Console',
          'Environment :: Web Environment',
          'Intended Audience :: End Users/Desktop',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Programming Language :: Python',
          ],
      packages= find_packages(),
      py_modules=['@projname@'], 
      )


# python3 setup.py bdist --formats=tar
# python3 setup.py sdist

