import random
from typing import Any

from fastapi import APIRouter, Query, Body, HTTPException

from webhooktesting.utils.lru_list import LRUList

router = APIRouter(prefix="/webhooktesting")


# This will be blown out with a restart of the server, but we are ok with that.
cache = LRUList(100)


@router.get(
    "/search",
    summary="Search for a string in the LRU cache",
)
def search(
    query: str = Query(
        ...,
        description="The string to search for",
        min_length=1,
    ),
):
    return cache.contains_substring(query)


@router.put(
    "",
    summary="Add a string to the LRU cache",
)
def add(
    data: Any = Body(...),
):
    cache.set(data)
    return f"Successfully added {str(data)}"


@router.put(
    "/unreliable",
    summary="Add a string to the LRU cache with a 50% chance of failure",
)
def unreliable_add(
    data: Any = Body(...),
):
    if random.random() > 0.5:
        cache.set(data)
        return f"Successfully added {str(data)}"
    else:
        raise HTTPException(status_code=400, detail="Failed to add data")


@router.get(
    "",
    summary="Get the LRU cache",
)
def list_cache():
    return str(cache)


@router.delete(
    "",
    summary="Clear the LRU cache",
)
def clear_cache():
    cache.clear()
    return "Successfully cleared cache"
