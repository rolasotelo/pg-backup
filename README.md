pgbackup
========

CLI for backing up remote PostgreSQL databases locally or to AWS S3.

## Usage
Pass in a full database URL, the storage driver, and destination.

S3 Example w/ bucket name:


```shell
$ pgbackup postgres://bob@example.com:5432/db_one --driver s3 backups
```
Local Example w/ local path:

```shell
$ pgbackup postgres://bob@example.com:5432/db_one --driver local /var/local/db_one/backups
```

## Installation From Source
To install the package after you've cloned the repository, you'll want to run the following command from within the project directory:

```shell
$ pip install --user -e .
```

## Preparing for Development
Follow these steps to start developing with this project:

1. Ensure pip and pipenv are installed
2. Clone repository: git clone git@github.com:example/pgbackup
3. `cd` into the repository
4. Activate virtualenv: pipenv shell
5. Install dependencies: pipenv install

Adding a Gitignore File
Before we commit anything, we're going to pull in a default Python .gitignore (https://github.com/github/gitignore/blob/master/Python.gitignore) file from Github so that we don't track files in our repository that we don't need:

```shell
(pgbackup) $ curl -o .gitignore https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore
```

Build by running in the project's directory while pipenv is active
```shell
$ python setup.py bdist_wheel
```