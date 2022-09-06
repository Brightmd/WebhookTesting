from typing import Any

from fastapi import APIRouter, Query, Body

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
    return str(cache)
