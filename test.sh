#!/bin/bash
sudo docker exec -i places_of_worship_web_1 python3 manage.py test --keepdb BasicArticle Community Group eventlog/tests 
