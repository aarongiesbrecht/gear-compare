#!/bin/sh
echo "rebooting sql container"
docker start mysql

echo "launching gear compare container"
docker run --name gc -d -p 8000:5000 --rm -e SECRET_KEY=my-scret-key --link mysql:dbserver -e DATABASE_URL-mysql+pymysql://gear_compare:maple@dbserver/gear_compare gear_compare:latest

