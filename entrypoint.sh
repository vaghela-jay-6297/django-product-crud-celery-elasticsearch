#!/bin/sh

# Wait for Elasticsearch to be available
until curl -s http://elasticsearch:9200 > /dev/null; do
  echo "Waiting for Elasticsearch..."
  sleep 2
done

# Run migrations
python manage.py migrate

# Rebuild the search index with automatic 'yes' response
yes | python manage.py search_index --rebuild

# Start the Django server
python manage.py runserver 0.0.0.0:8000
