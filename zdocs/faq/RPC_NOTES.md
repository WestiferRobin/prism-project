## 📡 `RPC_NOTES.md` — gRPC Usage Guide for Goose & Prism Projects

> 🧠 Applies to both: `goose-engine-service` and `prism-drone-service`

---

### 🚀 What is gRPC?

gRPC is a high-performance, open-source universal RPC framework from Google.

- Uses `.proto` files to define services & messages
- Auto-generates code for client/server communication
- Perfect for microservices in **Python**, **Go**, **Node.js**, etc.

---

### 📁 Recommended Project Structure

```
your-service/
├── rpc/
│   ├── proto/
│   │   ├── your_service.proto
│   ├── generated/
│   │   ├── your_service_pb2.py
│   │   └── your_service_pb2_grpc.py
```

> 🔁 Keep `proto/` for source files, `generated/` for compiled Python

---

### 📜 Step 1: Create Your `.proto` File

Example: `rpc/proto/your_service.proto`

```proto
syntax = "proto3";

package yourservice;

service TaskService {
  rpc RunTask (TaskRequest) returns (TaskResult);
}

message TaskRequest {
  string task_id = 1;
}

message TaskResult {
  string status = 1;
  string message = 2;
}
```

---

### ⚙️ Step 2: Compile Protobufs to Python

> 📌 Make sure you have `grpcio-tools` installed:

```bash
pip install grpcio grpcio-tools
```

Now compile:

```bash
.venv/bin/python -m grpc_tools.protoc \
  -I=protos \
  --python_out=messaging/rpc \
  --grpc_python_out=messaging/rpc \
  protos/*.proto

```

> 🛠 You can alias this as a script or add to a Makefile.

---

### ✅ Output

You'll get these two files:

```
rpc/generated/
├── your_service_pb2.py
├── your_service_pb2_grpc.py
```

Import and use them like:

```python
from rpc.generated import your_service_pb2, your_service_pb2_grpc
```

---

### 🔁 Optional: Add `rpc/generated/__init__.py` for clean imports

```bash
touch rpc/generated/__init__.py
```

---

### 🧼 Optional Makefile Entry

```makefile
proto:
	python -m grpc_tools.protoc \
	  -I rpc/proto \
	  --python_out=rpc/generated \
	  --grpc_python_out=rpc/generated \
	  rpc/proto/your_service.proto
```

Then just run:

```bash
make proto
```

---

### 🔐 Notes on Syncing Services

- Always update the `.proto` file first
- Regenerate before pushing changes
- Keep client and server in sync on `pb2` files

---

### 📦 Dependencies Required

```bash
pip install grpcio grpcio-tools
```

You can add these to your `requirements.txt` or `pyproject.toml`.

---