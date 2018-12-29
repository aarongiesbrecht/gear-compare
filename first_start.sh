#!/bin/sh
echo "launching sql container"
docker run --name mysql -d -e MYSQL_RANDOM_ROOT_PASSWORD=yes -e MYSQL_DATABASE=gear_compare -e MYSQL_USER=gear_compare -e MYSQL_PASSWORD=maple mysql/mysql-server:5.7

echo launching gear compare container
docker run --name gc -d -p 8000:5000 --rm -e SECRET_KEY=my-scret-key --link mysql:dbserver -e DATABASE_URL-mysql+pymysql://gear_compare:maple@dbserver/gear_compare gear_compare:latest

