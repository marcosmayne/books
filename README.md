# BOOKS

A simple book management application using Python + Django.

# Requirements

1. Python 3.8.10
2. SQLite 3.31.1

# Setup

Create Python virtual environment:

    python3 -m venv venv
    source venv/bin/activate

Install required Python packages:

    pip install --upgrade pip
    pip install -r requirements.txt

Check for errors:

    python manage.py check

Migrate:

    python manage.py migrate

To clean out the database:

    rm db.sqlite3
    rm main/migrations/[0-9]*.py

To clean out Python caches:

    find . -type d -name "__pycache__" |xargs rm -rf

