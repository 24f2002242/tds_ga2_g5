
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
import json
import os

app = FastAPI()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins, methods, headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # Allow all domains
    allow_credentials=True,    # Allow cookies/auth if needed
    allow_methods=["*"],       # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],       # Allow all headers
)


class RequestBody(BaseModel):
    regions: list[str]
    threshold_ms: int

with open(("data.json")) as f:
    TELEMETRY = json.load(f)
@app.post("/")
async def metrics(body: RequestBody):
    result = {}
    for region in body.regions:
        # filter telemetry rows matching region
        records = [r for r in TELEMETRY if r["region"] == region]
        if not records:
            continue

        latencies = [r["latency_ms"] for r in records]
        uptimes = [r["uptime_pct"] for r in records]

        avg_latency = float(np.mean(latencies))
        p95_latency = float(np.percentile(latencies, 95))
        avg_uptime = float(np.mean(uptimes))
        breaches = sum(1 for l in latencies if l > body.threshold_ms)

        result[region] = {
            "avg_latency": avg_latency,
            "p95_latency": p95_latency,
            "avg_uptime": avg_uptime,
            "breaches": breaches,
        }
    return result
