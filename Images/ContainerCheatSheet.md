# Docker Quick Reference Guide
> A compact quick reference for managing Docker images and containers.

##  Building & Running

**Build image:**
```bash
docker build -t my-image:tag .
```

**Run container (foreground):**
```bash
docker run --rm -p 80:80 --name my-container my-image:tag
```

**Run container (detached):**
```bash
docker run -d -p 80:80 --name my-container my-image:tag
```

**Port mapping and volumes (examples):**
```bash
docker run -p 8080:80 -v C:\host\path:/data my-image
```

---

## Lifecycle Management

**List containers:**
```bash
docker ps        # running
docker ps -a     # all
```

**Stop / start / restart:**
```bash
docker stop my-container
docker start my-container
docker restart my-container
```

**Remove container / image:**
```bash
docker rm my-container
docker rmi my-image:tag
```

---

## Interaction & Debugging

**View logs / attach / exec:**
```bash
docker logs my-container
docker attach my-container             # attach to main process
docker exec -it my-container /bin/sh   # run shell inside
```

**Inspect / show details:**
```bash
docker inspect my-container
docker inspect my-image:tag
```

---

## Images & Registry

**Manage images:**
```bash
docker images
docker pull image:tag
docker push repo/image:tag
```

---

## Maintenance

**Useful cleanup:**
```bash
docker system prune      # remove unused data
docker container prune   # remove stopped containers
```

---

## Quick Tips
* Use `-d` to run in **detached** mode.
* Use `-p HOST:CONTAINER` to map **ports**.
* Use `-v HOST:CONTAINER` to map **volumes**.