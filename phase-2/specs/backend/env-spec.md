# Backend Environment Variables

Required:
- DATABASE_URL=postgresql://user:pass@host:port/dbname
- JWT_SECRET=<32+ char secret>
- JWT_EXPIRES_IN=7d
- CORS_ORIGIN=http://localhost:5173
- LOG_LEVEL=info

Optional:
- UV_PORT=8000
- UV_HOST=0.0.0.0
- DB_POOL_MIN=1
- DB_POOL_MAX=10

Rules:
- .env.example file required
- CI should inject real secrets; never commit them
- Application starts must fail gracefully if required env missing
