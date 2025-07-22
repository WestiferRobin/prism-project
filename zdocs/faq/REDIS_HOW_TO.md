Ah, perfect — Redis supports **native data structures** like strings, hashes, lists, sets, sorted sets, and more — all accessible via Python (`redis-py`) with both **sync and async** APIs.

Here’s a quick guide for **common Redis data structures** using **async Python** (recommended for FastAPI apps).

---

## ✅ Setup (Async Redis Client)

```python
import redis.asyncio as redis
from db import settings  # assuming settings.cache_url = "redis://localhost:6379"

r = redis.from_url(settings.cache_url, decode_responses=True)
```

---

## 1. **Strings** (`SET`, `GET`)

```python
await r.set("user:123:name", "Wesley")
name = await r.get("user:123:name")  # -> "Wesley"
```

---

## 2. **Hashes** (`HSET`, `HGET`, `HGETALL`)

```python
await r.hset("user:123", mapping={"name": "Wesley", "role": "admin"})

name = await r.hget("user:123", "name")         # -> "Wesley"
user_data = await r.hgetall("user:123")         # -> {'name': 'Wesley', 'role': 'admin'}
```

---

## 3. **Lists** (`LPUSH`, `RPUSH`, `LPOP`, `LRANGE`)

```python
await r.lpush("tasks", "task1", "task2")  # ["task2", "task1"]
await r.rpush("tasks", "task3")           # ["task2", "task1", "task3"]

first_task = await r.lpop("tasks")        # -> "task2"
all_tasks = await r.lrange("tasks", 0, -1)  # -> remaining list
```

---

## 4. **Sets** (`SADD`, `SMEMBERS`, `SISMEMBER`)

```python
await r.sadd("tags", "python", "fastapi")
await r.sadd("tags", "redis")

tags = await r.smembers("tags")             # -> {'python', 'fastapi', 'redis'}
is_in = await r.sismember("tags", "python") # -> True
```

---

## 5. **Sorted Sets** (`ZADD`, `ZRANGE`, `ZSCORE`)

```python
await r.zadd("leaderboard", {"alice": 100, "bob": 150})

top = await r.zrange("leaderboard", 0, -1, withscores=True)
# -> [('alice', 100.0), ('bob', 150.0)]

bob_score = await r.zscore("leaderboard", "bob")  # -> 150.0
```

---

## 🧠 Real Use Cases

| Use Case              | Redis Type |
| --------------------- | ---------- |
| Caching user sessions | Hash       |
| Task queues           | List       |
| User preferences      | Hash       |
| Unique tags           | Set        |
| Leaderboards          | Sorted Set |

---

Let me know if you want to wrap these in a reusable `RedisStore` service class, or see patterns like expiring keys, TTLs, or pub/sub.
