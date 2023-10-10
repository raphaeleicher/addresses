#!/bin/bash

function start_app {
	env=$1
	podman run \
		--pod pod-addresses-app \
		-d \
		--name addresses-app \
		--volume ./.env-tst:/app/code/django_project/.env:Z \
		-l traefik.enable=true \
		-l traefik.http.routers.addresses-app.rule=Host\(\`addresses.vbox.local\`\) \
		-l traefik.http.services.addresses-app.loadbalancer.server.port=8080 \
		-l traefik.http.routers.addresses-app.tls=false \
		--replace \
		fdsgui-app:latest
}

start_app

