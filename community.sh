#!/bin/bash

sudo mkdir testapi
sudo chmod 777 testapi
sudo docker-compose up -d

sudo docker exec -i pipeline_multirepo_web_1 python3 manage.py generateToken --n > out.txt
chmod 777 out.txt


tag=$(tail -n 1 out.txt)
echo "tag is $tag"
var1=$(echo $tag | cut -f1 -d:)
var2=$(echo $tag | cut -f2 -d:)
 echo "var is $var1"
 trimmed=$(echo $var2)

 echo "trimmed is $trimmed"


sudo sed -i "s,EVENT_API_TOKEN=7f8bbb37b78cd65ba1af7f669a1251d5e000b5ff,EVENT_API_TOKEN=$trimmed,g" .env.docker
sudo sed -i 's,COLLAB_ROOT=http://172.17.0.1:7000,COLLAB_ROOT=http://10.129.27.30:7000,g' .env.docker
sudo sed -i 's,H5P_ROOT=http://172.17.0.1:8000,H5P_ROOT=http://10.129.27.30:8000,g' .env.docker
sudo sed -i 's,URL_BASIC=http://localhost:8000/,URL_BASIC=http://10.129.27.30:7000/,g' .env.docker

sudo sed -i 's,NODESERVERURL=,NODESERVERURL=http://10.129.27.30,g' .env.docker
sudo sed -i 's,RecommendationIP=172.17.0.1,RecommendationIP=10.129.27.30,g' .env.docker
sudo sed -i 's,RecommendationPort=3445,RecommendationPort=3445,g' .env.docker

pwd
sleep 100s
sleep 250s
sudo docker cp  pipeline_multirepo_node_1:/code  testapi &
wait
cd testapi
cd code
file="APIKEY.txt"
apiid=$(cat "$file")
echo $apiid


cd ..
cd ..
pwd
sudo sed -i "s,APIKEY=,APIKEY=$apiid,g" .env.docker
sudo docker exec -i pipeline_multirepo_web_1 python3 manage.py migrate     

sudo docker-compose build        
sudo docker-compose up -d





