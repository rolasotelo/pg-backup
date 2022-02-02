from setuptools import find_packages, setup


with open('README.md','r') as f:
    long_description = f.read()

setup(
    name='pgbackup',
    version='0.1.0',
    author='Rolando Sotelo',
    author_email='rola@hey.com',
    description='A utility for backing up postgreSQL databases.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/rolasotelo/pgbackup',
    packages=find_packages('src')
)
