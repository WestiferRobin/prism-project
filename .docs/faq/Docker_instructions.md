# 🚀 DOCKER INSTRUCTIONS

## 🔧 One-Time Setup (First Use Only)

Create a shared Docker network so services like `mood-engine-service` and `prism-content-service` can talk to the same RabbitMQ container:

```bash
docker network create prism_config-web
````

---

## 🔁 How to Use

### ▶️ Start Engine + Databases (for full integration testing)

```bash
docker-compose -f docker-compose.yml up --build -d
```

### ▶️ Start Only Databases + Infrastructure for Local Dev

```bash
docker-compose -f docker-compose.local.yml up -d
```

Make sure your `docker-compose.local.yml` files are set to use the shared network:

```yaml
networks:
  default:
    external:
      name: prism_config-web
```

And remove individual `networks:` from each service unless needed for advanced config.

---

## ✅ Environment Variables

Update your `.env` or settings files to use these **Docker-compatible service hostnames**:

### 📦 For Goose Engine:

```env
POSTGRES_URL=postgresql://goose:goose@goose-postgres:5432/goosedb
REDIS_URL=redis://goose-redis:6379
```

### 🧠 For Mood Engine:

```env
RABBITMQ_URL=amqp://prism-content:prism-content@prism-content-rabbitmq:5672/
```

> 👆 `prism-content-rabbitmq` is the container name for RabbitMQ, reachable from any service using the shared `prism-net`.

---

## 🧪 Useful Commands

* 🔍 View logs:

  ```bash
  docker compose logs -f
  ```

* 🧼 Clean up containers and volumes:

  ```bash
  docker compose down -v
  ```

* 📦 Build only:

  ```bash
  docker compose build
  ```

* 🛑 Stop all services:

  ```bash
  docker compose down
  ```

---

## 🧠 Tips

* Use [http://localhost:15672](http://localhost:15672) to access RabbitMQ UI (`guest / guest` or your custom creds)
* Logs from RabbitMQ or any broken service will tell you if there’s a hostname, port, or auth issue
* To simplify further, consider creating a `docker-compose.dev.yml` with all services unified into one file

---
