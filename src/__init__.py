"""

TODO: We're doing a major refactor

-

my-service/
├── src/                         # 🔧 Internal Python logic
│   ├── core/                   # - Core domain logic
│   ├── models/                 # - Pydantic or ORM models
│   ├── services/               # - Internal service logic
│   └── app.py                  # - App factory or entrypoint logic
│
├── api/                         # 🌐 REST or gRPC definitions
│   ├── routers/               # - FastAPI routers or gRPC handlers
│   ├── grpc/                  # - Protobuf .proto files and generated stubs
│   └── websocket/             # - WebSocket handlers if needed
│
├── tests/                      # ✅ Pytest tests
│   └── unit/                  # - Unit tests
│   └── integration/           # - Service or gRPC tests
│
├── Dockerfile                  # 🐳 Docker build
├── requirements.txt            # 📦 Runtime deps
├── pyproject.toml              # 🧱 Build system
├── .env                        # 🔐 Env vars (for dev)
├── README.md                   # 📘 Docs
├── alembic/                    # 🧬 DB migrations
├── grpc_tools.sh               # 🛠️ Proto compiler
├── scripts/                    # 🧪 DevOps scripts (e.g. run, test)
└── deployment/                 # 🚀 Kubernetes, Docker Compose, etc.




"""