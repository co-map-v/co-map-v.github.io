import os
from setuptools import setup, find_packages

PACKAGES = find_packages()


opts = dict(
    name='CO-MAP-V',
    version='0.1',
    url='https://github.com/co-map-v/co-map-v.github.io/',
    license='MIT',
    author=' ',
    author_email=' ',
    description='COVID Synthetic OMOP data visualization tool',
    packages=PACKAGES,
    package_data={'comapv': ['data/*', 'tests/*']}

)

if __name__ == '__main__':
    setup(**opts)