#!/bin/bash

for IMAGE in nginx:alpine-slim python:alpine php:zts-alpine postgres:alpine node:alpine traefik rabbitmq:alpine memcached:alpine redis:alpine
do
    # Stop all containers
    docker stop $(docker ps -a -q)

    # Remove all containers
    docker rm $(docker ps -a -q)

    # Docker prune
    docker image prune -f

    docker pull $IMAGE

    # Run grype on the freshly pulled docker image
    grype $IMAGE -o json > ./grype-slim-output/$IMAGE-grype.json

    # Update packages within the docker image
    # Try either apt or apk for distro type
    docker run -u 0 -it $IMAGE /bin/sh -c "apt update && apt upgrade -y;apk update && apk upgrade --available;exit"

    # Commit changes to a new updated docker image
    docker commit $(docker ps -l --quiet) $IMAGE-updated

    # Run grype on the new updated docker image
    grype $IMAGE-updated -o json > ./grype-slim-output/$IMAGE-grype-updated.json

    ##############################################################################
    ##############################################################################

    # generate SBOMs for each using syft
    syft $IMAGE -o json > ./syft-slim-output/$IMAGE-sbom.json
    syft $IMAGE-updated -o json > ./syft-slim-output/$IMAGE-updated-sbom.json
done

# Run the analysis to output vuln counts
python3 ./scripts/analysis-slim.py