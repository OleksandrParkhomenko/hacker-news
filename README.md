# Hacker News
Simple news board API

## Functionality

- Create CRUD API to manage news posts. The post will have the next fields: title, link, creation date, amount of upvotes, author-name
- Posts should have CRUD API to manage comments on them. The comment will have the next fields: author-name, content, creation date
- There should be an endpoint to upvote the post
- We should have a recurring job running once a day to reset post upvotes count

## How to run localy 

- ```git clone https://github.com/OleksandrParkhomenko/hacker-news```
- ```sudo docker-compose up -d --build```
- API runs on http://0.0.0.0:8000/api/

## API Documentation 
All documentation with examples and tests you can find here: https://documenter.getpostman.com/view/9119556/T17NZis9

## Deployed version 
Check http://35.202.92.138/api for the deployed version of API.
