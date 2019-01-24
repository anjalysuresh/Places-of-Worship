#!/bin/bash
sudo docker-compose down
sudo docker-compose up -d db
sudo docker-compose build        
sudo docker-compose up -d db
sudo docker exec -i places_of_worship_db_1 mysql -uroot -proot django < collab-updated.sql
