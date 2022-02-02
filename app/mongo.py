from typing import Dict

from pymongo import MongoClient

client = MongoClient('mongodb://root:example@mongo:27017/')
db = client.get_database("crawler")
collection = db.get_collection("usage_stats")


def write_elapsed_time(time: int) -> None:
    stats = _get_stats_doc()

    if stats:
        collection.replace_one(
            {"_id": stats["_id"]},
            {
                "count": stats["count"] + 1,
                "total_time": stats["total_time"] + time
            }
        )
    else:
        collection.insert_one({
            "count": 1,
            "total_time": time
        })


def get_usage_stats() -> Dict:
    doc = _get_stats_doc()

    if doc:
        return {
            "count": doc["count"],
            "avg_time": doc["total_time"] / doc["count"]
        }

    return None


def _get_stats_doc() -> Dict:
    return collection.find_one()
