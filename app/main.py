from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from app.crawler import crawl_domains
from app.mongo import get_usage_stats

app = FastAPI()


class DomainsRequest(BaseModel):
    domains: List[str]


@app.get("/ping")
def ping():
    return "pong"


@app.post("/domains")
def crawl_domains_post(req: DomainsRequest):
    return {"titles": crawl_domains(req.domains)}


@app.get("/usage-stats")
def usage_stats():
    return get_usage_stats()
