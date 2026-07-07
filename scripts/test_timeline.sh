#!/usr/bin/env bash

URL="http://localhost:5000/api/timeline_post"

# Make a random post so each run is unique.
NAME="Test User $RANDOM"
EMAIL="test$RANDOM@example.com"
CONTENT="Test post $RANDOM"

# Create post with and grab its id
echo "Creating a post..."
ID=$(curl -s -X POST "$URL" -d "name=$NAME" -d "email=$EMAIL" -d "content=$CONTENT" | jq '.id')
echo "Created post with id $ID"

# 2. Check the post shows up in GET.
echo "Checking the post was added..."
if curl -s "$URL" | grep -q "$CONTENT"; then
    echo "Post was added!"
else
    echo "Post was NOT found!"
fi

# 3. Delete the post to clean up.
echo "Deleting the post..."
curl -s -X DELETE "$URL/$ID"
echo
