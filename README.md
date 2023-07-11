
# Comparison between updated Docker images and Chainguard Images

Why not use popular Docker hub images, update all the OS packages, and call it a day?

## Target Images (2023-07-11)
Popular official docker images: https://hub.docker.com/search?q=&image_filter=official

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


Pull Rank | Image     | Docker                                                                   | Docker Image     | CG                                                                                                                                                                             | CG Image                            | 
--------- | --------- | ------------------------------------------------------------------------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------- | 
1         | alpine    |                                                                          |                  |                                                                                                                                                                                |                                     | 
2         | nginx     | [https://hub.docker.com/_/nginx](https://hub.docker.com/_/nginx)         | nginx:latest     | [https://edu.chainguard.dev/chainguard/chainguard-images/reference/nginx/overview/](https://edu.chainguard.dev/chainguard/chainguard-images/reference/nginx/overview/)         | cgr.dev/chainguard/nginx:latest     | 
3         | busybox   | [https://hub.docker.com/_/busybox](https://hub.docker.com/_/busybox)     | busybox:latest   | [https://edu.chainguard.dev/chainguard/chainguard-images/reference/busybox/overview/](https://edu.chainguard.dev/chainguard/chainguard-images/reference/busybox/overview/)     | cgr.dev/chainguard/busybox:latest   | 
4         | ubuntu    |                                                                          | ubuntu:latest    |                                                                                                                                                                                |                                     | 
5         | python    | [https://hub.docker.com/_/python](https://hub.docker.com/_/python)       | python:latest    | [https://edu.chainguard.dev/chainguard/chainguard-images/reference/python/overview/](https://edu.chainguard.dev/chainguard/chainguard-images/reference/python/overview/)       | cgr.dev/chainguard/python:latest    | 
6         | redis     | [https://hub.docker.com/_/redis](https://hub.docker.com/_/redis)         | redis:latest     | [https://edu.chainguard.dev/chainguard/chainguard-images/reference/redis/overview/](https://edu.chainguard.dev/chainguard/chainguard-images/reference/redis/overview/)         | cgr.dev/chainguard/redis:latest     | 
7         | postgres  | [https://hub.docker.com/_/postgres](https://hub.docker.com/_/postgres)   | postgres:latest  | [https://edu.chainguard.dev/chainguard/chainguard-images/reference/postgres/overview/](https://edu.chainguard.dev/chainguard/chainguard-images/reference/postgres/overview/)   | cgr.dev/chainguard/postgres:latest  | 
8         | node      | [https://hub.docker.com/_/node](https://hub.docker.com/_/node)           | node:latest      | [https://edu.chainguard.dev/chainguard/chainguard-images/reference/node/overview/](https://edu.chainguard.dev/chainguard/chainguard-images/reference/node/overview/)           | cgr.dev/chainguard/node:latest      | 
9         | httpd     |                                                                          | httpd:latest     |                                                                                                                                                                                |                                     | 
10        | mongo     |                                                                          | mongo:latest     |                                                                                                                                                                                |                                     | 
11        | memcached | [https://hub.docker.com/_/memcached](https://hub.docker.com/_/memcached) | memcached:latest | [https://edu.chainguard.dev/chainguard/chainguard-images/reference/memcached/overview/](https://edu.chainguard.dev/chainguard/chainguard-images/reference/memcached/overview/) | cgr.dev/chainguard/memcached:latest | 
12        | mysql     |                                                                          | mysql:latest     |                                                                                                                                                                                |                                     | 
13        | traefik   | [https://hub.docker.com/_/traefik](https://hub.docker.com/_/traefik)     | traefik:latest   | [https://edu.chainguard.dev/chainguard/chainguard-images/reference/traefik/overview/](https://edu.chainguard.dev/chainguard/chainguard-images/reference/traefik/overview/)     | cgr.dev/chainguard/traefik:latest   | 
14        | mariadb   | [https://hub.docker.com/_/mariadb](https://hub.docker.com/_/mariadb)     | mariadb:latest   | [https://edu.chainguard.dev/chainguard/chainguard-images/reference/mariadb/overview/](https://edu.chainguard.dev/chainguard/chainguard-images/reference/mariadb/overview/)     | cgr.dev/chainguard/mariadb:latest   | 
15        | docker    |                                                                          | docker:latest    |                                                                                                                                                                                |                                     | 
16        | rabbitmq  | [https://hub.docker.com/_/rabbitmq](https://hub.docker.com/_/rabbitmq)   | rabbitmq:latest  | [https://edu.chainguard.dev/chainguard/chainguard-images/reference/rabbitmq/overview/](https://edu.chainguard.dev/chainguard/chainguard-images/reference/rabbitmq/overview/)   | cgr.dev/chainguard/rabbitmq:latest  | 


## Results

```
$ bash ./scripts/update_comparison.sh
....

==============================================
Results for image -> postgres:latest
    - Original image vuln count: 113
    - Updated image vuln count: 113
    - Reduced vulns from updated image: 0
    - Chainguard image vuln count: 0
==============================================
==============================================
Results for image -> python:latest
    - Original image vuln count: 727
    - Updated image vuln count: 701
    - Reduced vulns from updated image: 26
    - Chainguard image vuln count: 1
==============================================
==============================================
Results for image -> node:latest
    - Original image vuln count: 701
    - Updated image vuln count: 675
    - Reduced vulns from updated image: 26
    - Chainguard image vuln count: 1
==============================================
==============================================
Results for image -> memcached:latest
    - Original image vuln count: 188
    - Updated image vuln count: 162
    - Reduced vulns from updated image: 26
    - Chainguard image vuln count: 0
==============================================
==============================================
Results for image -> nginx:latest
    - Original image vuln count: 90
    - Updated image vuln count: 90
    - Reduced vulns from updated image: 0
    - Chainguard image vuln count: 0
==============================================
==============================================
Results for image -> redis:latest
    - Original image vuln count: 169
    - Updated image vuln count: 169
    - Reduced vulns from updated image: 0
    - Chainguard image vuln count: 0
==============================================
==============================================
Results for image -> mariadb:latest
    - Original image vuln count: 25
    - Updated image vuln count: 25
    - Reduced vulns from updated image: 0
    - Chainguard image vuln count: 0
==============================================
==============================================
Results for image -> rabbitmq:latest
    - Original image vuln count: 15
    - Updated image vuln count: 15
    - Reduced vulns from updated image: 0
    - Chainguard image vuln count: 0
==============================================
==============================================
Results for image -> traefik:latest
    - Original image vuln count: 9
    - Updated image vuln count: 9
    - Reduced vulns from updated image: 0
    - Chainguard image vuln count: 0
==============================================
```