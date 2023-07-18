#!/bin/bash

for IMAGE in python nginx redis postgres node memcached traefik mariadb rabbitmq php
do
    # Stop all containers
    docker stop $(docker ps -a -q)

    # Remove all containers
    docker rm $(docker ps -a -q)

    # Docker prune
    docker image prune -f

    # Pull the lastest Docker image
    docker pull $IMAGE:latest

    # Run grype on the freshly pulled docker image
    grype $IMAGE:latest -o json > ./grype-output/$IMAGE-grype.json

    # Update packages within the docker image
    # Try either apt or apk for distro type
    docker run -u 0 -it $IMAGE:latest /bin/sh -c "apt update && apt upgrade -y;apk update && apk upgrade --available;exit"

    # Commit changes to a new updated docker image
    docker commit $(docker ps -l --quiet) $IMAGE-updated

    # Run grype on the new updated docker image
    grype $IMAGE-updated -o json > ./grype-output/$IMAGE-updated-grype.json

    ##############################################################################
    ##############################################################################

    # pull the latest Chainguard image
    docker pull cgr.dev/chainguard/$IMAGE:latest

    # Run grype on the Chainguard image
    grype cgr.dev/chainguard/$IMAGE:latest -o json > ./grype-output/$IMAGE-cg-grype.json

    ##############################################################################
    ##############################################################################

    # generate SBOMs for each using syft
    syft cgr.dev/chainguard/$IMAGE:latest -o json > ./syft-output/$IMAGE-cg-sbom.json
    syft $IMAGE:latest -o json > ./syft-output/$IMAGE-sbom.json
    syft $IMAGE-updated -o json > ./syft-output/$IMAGE-updated-sbom.json
done

# Run the analysis to output vuln counts
python3 ./scripts/analysis.py