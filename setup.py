from setuptools import setup, find_packages

import os
import sys
import platform

__packagename__ = "ina260"
install_requires = ['smbus2']

setup(
    name=__packagename__,
    version='0.0.1',
    packages=find_packages(),
    author='Josh Veitch-Michaelis',
    author_email='j.veitchmichaelis@gmail.com',
    license='MIT',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    zip_safe=False,
    include_package_data=True,
    install_requires = install_requires
)
