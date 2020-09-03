import os
from setuptools import find_packages, setup

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
README_PATH = os.path.join(BASE_DIR, 'README.md')
README = open(README_PATH, 'r', encoding='utf-8').read()

setup(
    name='drf-narito-gallery',
    version='1.0',
    description='simple gallery api',
    long_description=README,
    long_description_content_type='text/markdown',
    author='Narito Takizawa',
    author_email='toritoritorina@gmail.com',
    url='https://github.com/naritotakizawa/drf-narito-gallery/',
    packages=find_packages(exclude=('tests', 'project')),
    install_requires=('djangorestframework', 'django-admin-sortable2', 'pillow'),
    include_package_data=True,
    license='MIT',
)
