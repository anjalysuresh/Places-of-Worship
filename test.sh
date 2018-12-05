#!/bin/bash
sudo docker exec -i pipeline_multirepo_web_1 python3 manage.py test --keepdb BasicArticle Community Group eventlog/tests 
