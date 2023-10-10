#!/bin/bash

function start_db {
	env=$1
	podman run \
		--pod pod-addresses \
		-d \
		--volume vol-addresses-db:/var/lib/postgresql/data/:Z \
		--env-file ./.env-db \
		--name addresses-db \
		docker.io/library/postgres:15-bullseye
}

start_db

