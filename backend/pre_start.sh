#! /usr/bin/env bash

# Let the DB start
python /app/ysv/backend_pre_start.py

# Run migrations
alembic upgrade head

# Create initial data in DB
python /app/ysv/initial_data.py
