#!/bin/bash 

echo "create a mysql container.."
docker run -d --name mysql-sanhui \
           -v $(pwd)/conf.d:/etc/mysql/conf.d \
           -v $(pwd)/data:/var/lib/mysql \
           -e MYSQL_ROOT_PASSWORD="huawei@123" \
           -e MYSQL_DATABASE="sanhui" \
           -P \
       mysql:5.7.19 \
           --character-set-server=utf8 --collation-server=utf8_general_ci
