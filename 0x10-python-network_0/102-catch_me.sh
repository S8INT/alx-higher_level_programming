#!/bin/bash
# Make a request using curl and save the response in a file
curl -s -X POST -d "You got me!" http://0.0.0.0:5000/catch_me -o resp.txt
