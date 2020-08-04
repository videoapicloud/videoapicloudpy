from setuptools import setup, find_packages
import sys, os

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()
setup(
  name = 'videoapicloudpy',
  version = '1.0.0',
  py_modules = ['videoapicloud.job', 'videoapicloud.config'],
  packages=find_packages(exclude=['tests*']),
  author='VideoAPI.cloud Engineering Team',
  author_email='support@videoapi.cloud',
  description='A python wrapper for VideoAPI.cloud',
  license='MIT License',
  url='https://videoapi.cloud',
  keywords='VideoAPI.cloud cloud video encoding api',
  install_requires=[ "httplib2" ],
	long_description="""Client Library for VideoAPI.cloud.

For more information:

* VideoAPI.cloud: https://videoapi.cloud
* API Documentation: https://videoapi.cloud/docs

Changelogs

1.0.0
First version

"""
)
