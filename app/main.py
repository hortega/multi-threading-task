from typing import List

from fastapi import FastAPI
from pydantic import BaseModel

from app.crawler import crawl_domains

app = FastAPI()


class DomainsRequest(BaseModel):
    domains: List[str]


@app.get("/ping")
def ping():
    return "pong"


@app.post("/domains")
def crawl_domains_post(req: DomainsRequest):
    return {"titles": crawl_domains(req.domains)}
