Absolutely — here’s a practical guide on how to use `AsyncSession` from SQLAlchemy for any query (CRUD) using modern 2.0-style with `async`/`await`.

---

### ✅ 1. **Setup Overview**

Assuming you're using:

* `SQLAlchemy 2.x` with async support
* `AsyncSession` from `sqlalchemy.ext.asyncio`

You'll usually inject an `AsyncSession` like this:

```python
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

async def get_channel(db: AsyncSession = Depends(get_db)):
    ...
```

---

### ✅ 2. **Query (SELECT)**

```python
from sqlalchemy import select
from models import ChannelModel  # your model

async def get_channel_by_username(username: str, db: AsyncSession):
    stmt = select(ChannelModel).where(ChannelModel.channel_username == username)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()  # returns one or None
```

---

### ✅ 3. **Insert (CREATE)**

```python
from models import ChannelModel
import uuid

async def create_channel(db: AsyncSession, name: str, username: str):
    new_channel = ChannelModel(
        id=uuid.uuid4(),
        channel_name=name,
        channel_username=username
    )
    db.add(new_channel)
    await db.commit()
    await db.refresh(new_channel)  # loads data from DB (e.g., defaults)
    return new_channel
```

---

### ✅ 4. **Update**

```python
async def update_channel_username(channel_id: uuid.UUID, new_username: str, db: AsyncSession):
    stmt = select(ChannelModel).where(ChannelModel.job_id == channel_id)
    result = await db.execute(stmt)
    channel = result.scalar_one_or_none()

    if not channel:
        return None

    channel.channel_username = new_username
    await db.commit()
    await db.refresh(channel)
    return channel
```

---

### ✅ 5. **Delete**

```python
async def delete_channel(channel_id: uuid.UUID, db: AsyncSession):
    stmt = select(ChannelModel).where(ChannelModel.job_id == channel_id)
    result = await db.execute(stmt)
    channel = result.scalar_one_or_none()

    if channel:
        await db.delete(channel)
        await db.commit()
    return channel
```

---

### 🔁 6. **Get Multiple Rows**

```python
async def list_channels(db: AsyncSession):
    stmt = select(ChannelModel).order_by(ChannelModel.channel_name)
    result = await db.execute(stmt)
    return result.scalars().all()  # returns a list of ChannelModel objects
```

---

### 🧠 Tip: Using `.scalars()` vs `.scalar_one()`

| Method                  | Purpose                         |
| ----------------------- | ------------------------------- |
| `.scalar_one()`         | Get exactly one row, else error |
| `.scalar_one_or_none()` | Get one or None, else error     |
| `.scalars().all()`      | Get multiple results            |

---

Would you like me to give you a reusable service layer or FastAPI endpoint example next?
