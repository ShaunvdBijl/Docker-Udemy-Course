# Networks & Container Requests

In many applications, you will need more than one container for two main reasons:
1. **Single Responsibility:** It is considered good practice to focus each container on one main task (e.g., running a web server, running a database).
2. **Configuration Complexity:** It is difficult to configure and maintain a single container that performs multiple main tasks at once.

Multi-container applications are common in real-world applications and typically communicate across three targets:
* With the **World Wide Web (WWW)**
* With the **Host Machine**
* With **Other Containers**

---

## 1. Communicating with the World Wide Web (WWW)

Sending outbound HTTP/HTTPS requests to external APIs or third-party servers works out of the box with no extra configuration needed.

```javascript
fetch('[https://some-api.com/my-data').then](https://some-api.com/my-data').then)(...)
```

* The containerized application can send requests to public web domains without requiring custom network setup.

---

## 2. Communicating with the Host Machine

Connecting from inside a container to a service running directly on your host machine (e.g., a local database during development) requires a specific Docker domain.

> **Note:** Communicating with the host machine is typically done during local development. In remote server deployments, containers rarely need to communicate directly with the host.

### Why `localhost` Fails

```javascript
fetch('localhost:3000/demo').then(...)
```

* Inside a container, `localhost` resolves to the container's isolated local environment, not your host computer. This request will fail.

### The Solution: `host.docker.internal`

```javascript
fetch('host.docker.internal:3000/demo').then(...)
```

* `host.docker.internal` is a special address provided by Docker that resolves to the internal IP address of the host machine.
* Docker resolves the outgoing IP address at the network layer; it does not alter your application source code.

---

## 3. Communicating with Other Containers

There are two primary approaches for container-to-container communication:

1. **Manual IP Lookup (Not Recommended):** Manually inspect containers to find their internal IP addresses. This approach is fragile because container IPs change when containers are stopped or recreated.
2. **Docker Networks (Recommended):** Place communicating containers into a shared custom Docker network.

### Using Docker Networks

1. **Create the custom bridge network:**
   ```bash
   docker network create my-network-name
   ```

2. **Attach containers to the network on startup:**
   ```bash
   docker run --network my-network-name --name cont1 my-image
   docker run --network my-network-name --name cont2 my-other-image
   ```

3. **Communicate via container names:**
   When connected to the same custom network, Docker automatically provides internal DNS resolution so containers can address each other directly by name:
   ```javascript
   fetch('http://cont1:3000/my-data').then(...)
   ```