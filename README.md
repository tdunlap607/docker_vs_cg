
# Comparison between updated Docker images and Chainguard Images

Why not use popular Docker hub images, update all the OS packages, and call it a day?

## Target Images (2023-07-11)
[Popular official docker images](https://hub.docker.com/search?q=&image_filter=official)

<!-- <ol>
<li>Alpine</li>
    <ul>
    <li>CG: N/A</li>
    </ul>

<li>NGINX</li>
    <ul>
    <li>Docker: https://hub.docker.com/_/nginx</li>
    <li>CG: https://edu.chainguard.dev/chainguard/chainguard-images/reference/nginx/overview/</li>
    </ul>

<li>BusyBox</li>
    <ul>
    <li>Docker: https://hub.docker.com/_/busybox</li>
    <li>CG: https://edu.chainguard.dev/chainguard/chainguard-images/reference/busybox/overview/</li>
    </ul>

<li>Ubuntu</li>
    <ul>
    <li>CG: N/A</li>
    </ul>

<li>Python</li>
    <ul>
    <li>Docker: https://hub.docker.com/_/python</li>
    <li>CG: https://edu.chainguard.dev/chainguard/chainguard-images/reference/python/overview/</li>
    </ul>

<li>Redis</li>
    <ul>
    <li>Docker: https://hub.docker.com/_/redis</li>
    <li>CG: https://edu.chainguard.dev/chainguard/chainguard-images/reference/redis/overview/</li>
    </ul>

<li>Postgres</li>
    <ul>
    <li>Docker: https://hub.docker.com/_/postgres</li>
    <li>CG: https://edu.chainguard.dev/chainguard/chainguard-images/reference/postgres/overview/</li>
    </ul>

<li>Node</li>
    <ul>
    <li>Docker: https://hub.docker.com/_/node</li>
    <li>CG: https://edu.chainguard.dev/chainguard/chainguard-images/reference/node/overview/</li>
    </ul>

<li>httpd</li>
    <ul>
    <li>CG: N/A</li>
    </ul>

<li>Mongo</li>
    <ul>
    <li>CG: N/A</li>
    </ul>

<li>Memcached</li>
    <ul>
    <li>Docker: https://hub.docker.com/_/memcached</li>
    <li>CG: https://edu.chainguard.dev/chainguard/chainguard-images/reference/memcached/overview/</li>
    </ul>

<li>mysql</li>
    <ul>
    <li>CG: N/A</li>
    </ul>

<li>Traefik</li>
    <ul>
    <li>Docker: https://hub.docker.com/_/traefik</li>
    <li>CG: https://edu.chainguard.dev/chainguard/chainguard-images/reference/traefik/overview/</li>
    </ul>

<li>MariaDB</li>
    <ul>
    <li>Docker: https://hub.docker.com/_/mariadb 
    <li>CG: https://edu.chainguard.dev/chainguard/chainguard-images/reference/mariadb/overview/</li>
    </ul>

<li>Docker</li>
    <ul>
    <li>CG: N/A</li>
    </ul>

<li>Rabbitmq</li>
    <ul>
    <li>Docker: https://hub.docker.com/_/rabbitmq</li>
    <li>CG: https://edu.chainguard.dev/chainguard/chainguard-images/reference/rabbitmq/overview/</li>
    </ul>

</ol> -->


Pull Rank | Image     | Docker                                                 | CG                                                                                                                           | 
--------- | --------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- | 
1         | alpine    |                                                        |                                                                                                                              |
2         | nginx     | [nginx:latest](https://hub.docker.com/_/nginx)         | [cgr.dev/chainguard/nginx:latest](https://edu.chainguard.dev/chainguard/chainguard-images/reference/nginx/overview/)         | 
3         | busybox   | [busybox:latest](https://hub.docker.com/_/busybox)     | [cgr.dev/chainguard/busybox:latest](https://edu.chainguard.dev/chainguard/chainguard-images/reference/busybox/overview/)     | 
4         | ubuntu    |                                                        |                                                                                                                              |
5         | python    | [python:latest](https://hub.docker.com/_/python)       | [cgr.dev/chainguard/python:latest](https://edu.chainguard.dev/chainguard/chainguard-images/reference/python/overview/)       | 
6         | redis     | [redis:latest](https://hub.docker.com/_/redis)         | [cgr.dev/chainguard/redis:latest](https://edu.chainguard.dev/chainguard/chainguard-images/reference/redis/overview/)         | 
7         | postgres  | [postgres:latest](https://hub.docker.com/_/postgres)   | [cgr.dev/chainguard/postgres:latest](https://edu.chainguard.dev/chainguard/chainguard-images/reference/postgres/overview/)   | 
8         | node      | [node:latest](https://hub.docker.com/_/node)           | [cgr.dev/chainguard/node:latest](https://edu.chainguard.dev/chainguard/chainguard-images/reference/node/overview/)           | 
9         | httpd     |                                                        |                                                                                                                              |
10        | mongo     |                                                        |                                                                                                                              |
11        | memcached | [memcached:latest](https://hub.docker.com/_/memcached) | [cgr.dev/chainguard/memcached:latest](https://edu.chainguard.dev/chainguard/chainguard-images/reference/memcached/overview/) | 
12        | mysql     |                                                        |                                                                                                                              |
13        | traefik   | [traefik:latest](https://hub.docker.com/_/traefik)     | [cgr.dev/chainguard/traefik:latest](https://edu.chainguard.dev/chainguard/chainguard-images/reference/traefik/overview/)     | 
14        | mariadb   | [mariadb:latest](https://hub.docker.com/_/mariadb)     | [cgr.dev/chainguard/mariadb:latest](https://edu.chainguard.dev/chainguard/chainguard-images/reference/mariadb/overview/)     | 
15        | docker    |                                                        |                                                                                                                              |
16        | rabbitmq  | [rabbitmq:latest](https://hub.docker.com/_/rabbitmq)   | [cgr.dev/chainguard/rabbitmq:latest](https://edu.chainguard.dev/chainguard/chainguard-images/reference/rabbitmq/overview/)   | 
24        | php       | [php:latest](https://hub.docker.com/_/php)             | [cgr.dev/chainguard/php:latest](https://edu.chainguard.dev/chainguard/chainguard-images/reference/php/overview/)             |

## Methodology
We have created a simple [script](./scripts/update_comparison.sh) to download docker images, run grype on the image, update the packages within the image, run grype again on the updated image, and then run grype on the equivalent Chainguard image. The script can be seen below:

```shell
#!/bin/bash

for IMAGE in python nginx redis postgres node memcached traefik mariadb rabbitmq php
do
    # Stop all containers
    docker stop $(docker ps -a -q)

    # Remove all containers
    docker rm $(docker ps -a -q)

    # Docker prune
    docker image prune -f

    # Pull the latest image
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
done
```

## Results

```
$ bash ./scripts/update_comparison.sh

....

==============================================
Results for image -> node:latest
    - Original image CVE count: 701
    - Updated image CVE count: 675
    - Reduced CVE from updated image: 26
    - Chainguard image CVE count: 1
==============================================
==============================================
Results for image -> python:latest
    - Original image CVE count: 727
    - Updated image CVE count: 701
    - Reduced CVE from updated image: 26
    - Chainguard image CVE count: 1
==============================================
==============================================
Results for image -> mariadb:latest
    - Original image CVE count: 25
    - Updated image CVE count: 25
    - Reduced CVE from updated image: 0
    - Chainguard image CVE count: 0
==============================================
==============================================
Results for image -> postgres:latest
    - Original image CVE count: 113
    - Updated image CVE count: 113
    - Reduced CVE from updated image: 0
    - Chainguard image CVE count: 0
==============================================
==============================================
Results for image -> redis:latest
    - Original image CVE count: 169
    - Updated image CVE count: 169
    - Reduced CVE from updated image: 0
    - Chainguard image CVE count: 0
==============================================
==============================================
Results for image -> rabbitmq:latest
    - Original image CVE count: 15
    - Updated image CVE count: 15
    - Reduced CVE from updated image: 0
    - Chainguard image CVE count: 0
==============================================
==============================================
Results for image -> php:latest
    - Original image CVE count: 291
    - Updated image CVE count: 265
    - Reduced CVE from updated image: 26
    - Chainguard image CVE count: 0
==============================================
==============================================
Results for image -> memcached:latest
    - Original image CVE count: 188
    - Updated image CVE count: 162
    - Reduced CVE from updated image: 26
    - Chainguard image CVE count: 0
==============================================
==============================================
Results for image -> traefik:latest
    - Original image CVE count: 9
    - Updated image CVE count: 9
    - Reduced CVE from updated image: 0
    - Chainguard image CVE count: 0
==============================================
==============================================
Results for image -> nginx:latest
    - Original image CVE count: 90
    - Updated image CVE count: 90
    - Reduced CVE from updated image: 0
    - Chainguard image CVE count: 0
==============================================
```

We can see a consistent reduction of 26 CVEs from the updated docker images.
This is due to only a single package updating from 'apt update && apt upgrade':
```bash
The following packages will be upgraded:
  linux-libc-dev
1 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```