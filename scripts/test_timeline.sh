#!/usr/bin/env bash

URL="http://localhost:5000/api/timeline_post"


NAME="Test User $RANDOM"
EMAIL="test$RANDOM@example.com"
CONTENT="Test post $RANDOM"

# Create post with and grab its id
echo "Creating a post.."
ID=$(curl -s -X POST "$URL" -d "name=$NAME" -d "email=$EMAIL" -d "content=$CONTENT" | jq '.id')
echo "Created post with id $ID"

# Check the post shows up 
echo "Checking the post was added.."
curl -s "$URL" | grep -q "$CONTENT"
echo "Post was added"

# Delete the post
echo "Deleting the post.."
curl -s -X DELETE "$URL/$ID"
echo
