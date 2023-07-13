
# CG Images vs. Docker Images w/Updated OS Packages

Why not use popular Docker hub images, update all the OS packages, and call it a day?

## Target Images (2023-07-12)

The analysis is completed on a set of popular Docker images: [Popular official docker images](https://hub.docker.com/search?q=&image_filter=official)
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
We have created a simple [script](./scripts/update_comparison.sh) to download docker images, run grype on the image, update the packages within the image, run grype again on the updated image, and then run grype on the equivalent Chainguard image. We also build the SBOM using syft to identify the updated packages during the process. The script can be seen below:

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

    ##############################################################################
    ##############################################################################

    # generate SBOMs for each using syft
    syft cgr.dev/chainguard/$IMAGE:latest -o json > ./syft-output/$IMAGE-cg-sbom.json
    syft $IMAGE:latest -o json > ./syft-output/$IMAGE-sbom.json
    syft $IMAGE-updated -o json > ./syft-output/$IMAGE-updated-sbom.json
done
```

## Results

```
$ bash ./scripts/update_comparison.sh

....

==============================================
Results for image -> mariadb:latest
    - Original package count: 156
    - Original image CVE count: 25
    - Updated image CVE count: 25
    - Reduced CVE from updated image: 0
    - Total packages updated: 0

    - Chainguard image CVE count: 0
    - Chainguard package count: 47
==============================================
==============================================
Results for image -> redis:latest
    - Original package count: 108
    - Original image CVE count: 169
    - Updated image CVE count: 169
    - Reduced CVE from updated image: 0
    - Total packages updated: 0

    - Chainguard image CVE count: 0
    - Chainguard package count: 21
==============================================
==============================================
Results for image -> php:latest
    - Original package count: 175
    - Original image CVE count: 291
    - Updated image CVE count: 265
    - Reduced CVE from updated image: 26
    - Total packages updated: 1
        - linux-libc-dev(deb): 6.1.27-1 -> 6.1.37-1

    - Chainguard image CVE count: 0
    - Chainguard package count: 69
==============================================
==============================================
Results for image -> postgres:latest
    - Original package count: 147
    - Original image CVE count: 113
    - Updated image CVE count: 113
    - Reduced CVE from updated image: 0
    - Total packages updated: 0

    - Chainguard image CVE count: 0
    - Chainguard package count: 46
==============================================
==============================================
Results for image -> python:latest
    - Original package count: 435
    - Original image CVE count: 730
    - Updated image CVE count: 704
    - Reduced CVE from updated image: 26
    - Total packages updated: 1
        - linux-libc-dev(deb): 6.1.27-1 -> 6.1.37-1

    - Chainguard image CVE count: 0
    - Chainguard package count: 45
==============================================
==============================================
Results for image -> traefik:latest
    - Original package count: 300
    - Original image CVE count: 9
    - Updated image CVE count: 9
    - Reduced CVE from updated image: 0
    - Total packages updated: 3
        - busybox(apk): 1.36.1-r0 -> 1.36.1-r1
        - busybox-binsh(apk): 1.36.1-r0 -> 1.36.1-r1
        - ssl_client(apk): 1.36.1-r0 -> 1.36.1-r1

    - Chainguard image CVE count: 0
    - Chainguard package count: 291
==============================================
==============================================
Results for image -> memcached:latest
    - Original package count: 109
    - Original image CVE count: 188
    - Updated image CVE count: 162
    - Reduced CVE from updated image: 26
    - Total packages updated: 1
        - linux-libc-dev(deb): 6.1.27-1 -> 6.1.37-1

    - Chainguard image CVE count: 0
    - Chainguard package count: 37
==============================================
==============================================
Results for image -> nginx:latest
    - Original package count: 151
    - Original image CVE count: 91
    - Updated image CVE count: 91
    - Reduced CVE from updated image: 0
    - Total packages updated: 0

    - Chainguard image CVE count: 0
    - Chainguard package count: 28
==============================================
==============================================
Results for image -> node:latest
    - Original package count: 667
    - Original image CVE count: 704
    - Updated image CVE count: 678
    - Reduced CVE from updated image: 26
    - Total packages updated: 1
        - linux-libc-dev(deb): 6.1.27-1 -> 6.1.37-1

    - Chainguard image CVE count: 1
    - Chainguard package count: 279
==============================================
==============================================
Results for image -> rabbitmq:latest
    - Original package count: 105
    - Original image CVE count: 15
    - Updated image CVE count: 15
    - Reduced CVE from updated image: 0
    - Total packages updated: 0

    - Chainguard image CVE count: 0
    - Chainguard package count: 37
==============================================
```

We can see a consistent reduction of 26 CVEs from the updated docker images.
This is due to only a single package updating from 'apt update && apt upgrade':
```bash
The following packages will be upgraded:
  linux-libc-dev
1 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```


## Challenges with updating vulnerable dependencies

Here we dive into the vulnerabilities of the [Traefik Docker Image](https://hub.docker.com/_/traefik). 

[Traefik](https://traefik.io/) is a popular reverse proxy and load balancer software. The [latest traefik official docker image](https://hub.docker.com/_/traefik) averages over 1.6MM pulls per week and has over 1B+ pulls during its lifetime. Safe to say, Traefik is frequently used. So let's dig into some vulnerabilities within the popular docker image. First, we'll pull the latest docker image:

```bash
$ docker pull traefik:latest
latest: Pulling from library/traefik
31e352740f53: Pull complete 
4b9a9b499d7a: Pull complete 
d581263ee7dc: Pull complete 
f5f0f39a1a90: Pull complete 
Digest: sha256:c272e8c32fb7356c2166bc5d170ab0a2c73da7bfec561234c52f255ece1dd07c
Status: Downloaded newer image for traefik:latest
docker.io/library/traefik:latest
```

Let's validate this is the latest stable version of Traefik, 2.10.3 at the time of writing (July 12, 2023):
```bash
$ docker run -u 0 -it traefik:latest traefik version
Version:      2.10.3
Codename:     saintmarcelin
Go version:   go1.20.5
Built:        2023-06-19T16:18:54Z
OS/Arch:      linux/amd64
```

Let's see what vulnerabilities exist within the Traefik image using [Grype](https://github.com/anchore/grype):

```bash
$ grype traefik:latest
 ✔ Vulnerability DB        [no update available]
 ✔ Loaded image            
 ✔ Parsed image            
 ✔ Cataloged packages      [300 packages]
 ✔ Scanning image...       [9 vulnerabilities]
   ├── 0 critical, 3 high, 6 medium, 0 low, 0 negligible
   └── 6 fixed
NAME                            INSTALLED               FIXED-IN      TYPE       VULNERABILITY        SEVERITY 
github.com/docker/distribution  v2.8.1+incompatible     2.8.2-beta.1  go-module  GHSA-hqxw-f8mx-cpmw  High      
github.com/docker/docker        v20.10.21+incompatible  20.10.24      go-module  GHSA-232p-vwff-86mp  High      
github.com/docker/docker        v20.10.21+incompatible  20.10.24      go-module  GHSA-33pg-m6jh-5237  Medium    
github.com/docker/docker        v20.10.21+incompatible  20.10.24      go-module  GHSA-6wrf-mxfj-pf5p  Medium    
github.com/hashicorp/consul     v1.10.12                              go-module  CVE-2021-41803       High      
github.com/hashicorp/consul     v1.10.12                              go-module  CVE-2022-40716       Medium    
github.com/hashicorp/consul     v1.10.12                              go-module  CVE-2023-0845        Medium    
github.com/hashicorp/consul     v1.10.12                1.11.9        go-module  GHSA-m69r-9g56-7mv8  Medium    
github.com/hashicorp/consul     v1.10.12                1.14.5        go-module  GHSA-c57c-7hrj-6q6v  Medium 
```

Nine unique vulnerabilities exist, all coming from go modules. So the question arises, how do we update these vulnerable go modules? The first thought would simply be ```go get example.com/theirmodule@latest```, so let's try it. We can interact with the shell inside of the running container in an attempt to update the go modules:

```bash
$ docker run -u 0 -it traefik:latest /bin/sh
= '/bin/sh' is not a Traefik command: assuming shell execution.
/ # go version
/bin/sh: go: not found
```

The problem is ```go``` is not shipped with the Traefik Docker image. The vulnerability comes from go-modules, and understanding where they are located is key to upgrading them. Let's find out where one of the go modules ``github.com/hashicorp/consul`` is installed using [Syft](https://github.com/anchore/syft):

```bash
$ syft traefik:latest -o json | jq '.artifacts | .[] | select(.name=="github.com/hashicorp/consul")'
 ✔ Loaded image            
 ✔ Parsed image            
 ✔ Cataloged packages      [300 packages]

{
  "id": "1b96b8706474448f",
  "name": "github.com/hashicorp/consul",
  "version": "v1.10.12",
  "type": "go-module",
  "foundBy": "go-module-binary-cataloger",
  "locations": [
    {
      "path": "/usr/local/bin/traefik",
      "layerID": "sha256:b75dbb2e05822bee5bb6f2715169d6202af91e2a83cade5a40fc69bbee0fbbbf",
      "annotations": {
        "evidence": "primary"
      }
    }
  ],
  "licenses": [],
  "language": "go",
  "cpes": [
    "cpe:2.3:a:hashicorp:consul:v1.10.12:*:*:*:*:*:*:*"
  ],
  "purl": "pkg:golang/github.com/hashicorp/consul@v1.10.12",
  "metadataType": "GolangBinMetadata",
  "metadata": {
    "goCompiledVersion": "go1.20.5",
    "architecture": "amd64",
    "h1Digest": "h1:xMazys3KaH5JsZS4Ra6KEAXO0nAj20EsTpsDyhd/3Do=",
    "mainModule": "github.com/traefik/traefik/v2"
  }
}
```

We can see that the path to the location is in ```"path": "/usr/local/bin/traefik"```, which is the binary for traefik. The binary for trafeik is installed in an intermediate layer during the build process of the docker image. Examing the [Dockerfile](https://github.com/traefik/traefik-library-image/blob/v2.10.3/alpine/Dockerfile): 

```Dockerfile
FROM alpine:3.18
RUN apk --no-cache add ca-certificates tzdata
RUN set -ex; \
  apkArch="$(apk --print-arch)"; \
  case "$apkArch" in \
    armhf) arch='armv6' ;; \
    aarch64) arch='arm64' ;; \
    x86_64) arch='amd64' ;; \
    s390x) arch='s390x' ;; \
    *) echo >&2 "error: unsupported architecture: $apkArch"; exit 1 ;; \
  esac; \
  wget --quiet -O /tmp/traefik.tar.gz "https://github.com/traefik/traefik/releases/download/v2.10.3/traefik_v2.10.3_linux_$arch.tar.gz"; \
  tar xzvf /tmp/traefik.tar.gz -C /usr/local/bin traefik; \
  rm -f /tmp/traefik.tar.gz; \
  chmod +x /usr/local/bin/traefik
COPY entrypoint.sh /
EXPOSE 80
ENTRYPOINT ["/entrypoint.sh"]
CMD ["traefik"]
```

Depending on the architecture, it constructs a URL to download the Traefik binary for that architecture from the official Traefik GitHub repository.
It uses wget to download the Traefik binary tarball and saves it to /tmp/traefik.tar.gz.
The tarball is then extracted to /usr/local/bin using tar.
After extraction, the tarball is removed (rm -f).
Finally, the executable permission is set on the Traefik binary using chmod.

So the vulnerability comes from the upstream Traefik binary, bringing up the old-aged problem of dependency lag. 
Updating the consul package requires rebuilding the Traefik binary with the updated non-vulnerable vulnerable version of consul.
Within the [go.mod](https://github.com/traefik/traefik/blob/v2.10.3/go.mod) file of Traefik we can see consul is pinned at the [vulnerable version of 1.10.12](https://github.com/traefik/traefik/blob/v2.10.3/go.mod#L29), even though patch is in the available version of consul [1.15.3](https://github.com/hashicorp/consul/releases). 

Thankfully, Chainguard has done the heavy lifting of updating vulnerable versions of dependencies.
We can see Chainguard has updated the consul package to the non-vulnerable version of 1.15.3 within the latest [cgr.dev/chainguard/traefik](https://edu.chainguard.dev/chainguard/chainguard-images/reference/traefik/overview/) image:
```bash
$ syft cgr.dev/chainguard/traefik:latest -o json | jq '.artifacts | .[] | select(.name=="github.com/hashicorp/consul")'
 ✔ Loaded image            
 ✔ Parsed image            
 ✔ Cataloged packages      [291 packages]
{
  "id": "7adfeebf788f965c",
  "name": "github.com/hashicorp/consul",
  "version": "v1.15.3",
  "type": "go-module",
  "foundBy": "go-module-binary-cataloger",
  "locations": [
    {
      "path": "/usr/bin/traefik",
      "layerID": "sha256:eea78a04e2cbe0cff6c52418a0ec87dc21f9872259e96e4991f03244c4f77350",
      "annotations": {
        "evidence": "primary"
      }
    }
  ],
  "licenses": [],
  "language": "go",
  "cpes": [
    "cpe:2.3:a:hashicorp:consul:v1.15.3:*:*:*:*:*:*:*"
  ],
  "purl": "pkg:golang/github.com/hashicorp/consul@v1.15.3",
  "metadataType": "GolangBinMetadata",
  "metadata": {
    "goCompiledVersion": "go1.20.5",
    "architecture": "amd64",
    "h1Digest": "h1:ErNocU3HT14vdAdBpO/42pjkEpSkZYwuHzTzvrlmr0c=",
    "mainModule": "github.com/traefik/traefik/v2"
  }
}
```