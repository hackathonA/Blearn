#!/bin/sh
#!./.clear.sh



docker compose down -v

docker rmi $(docker images -q)

docker system prune