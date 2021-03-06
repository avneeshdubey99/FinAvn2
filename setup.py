#!/usr/bin/env python
# coding: utf-8

# In[ ]:

from distutils.core import setup

def readme():
    with open('README.md') as f:
        return f.read()
setup(
  name = 'FinAvn2',
  packages = ['FinAvn2'],
  version = '1.2',
  license='MIT',
  description = 'Performing Financial Time series forecasting using Machine Learning',
  long_description= readme(),
  author = 'Avneesh Dubey',
  author_email = 'avneesh.d01@gmail.com',
  url = 'https://github.com/avneeshdubey99/FinAvn2',
  download_url = 'https://github.com/avneeshdubey99/FinAvn2.git',
  keywords = ['Machine Learning', 'Pandas', 'Numpy', 'Analysis', 'Regression', 'Classification', 'Dimensionality', 'Classifiers'],
  install_requires=[
          'numpy',
          'sklearn',
          'pandas'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
    
