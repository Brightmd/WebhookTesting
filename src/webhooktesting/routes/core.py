import random
import secrets
from typing import Any

from fastapi import APIRouter, Query, Body, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.status import HTTP_401_UNAUTHORIZED

from webhooktesting.utils.lru_list import LRUList

router = APIRouter(prefix="/webhooktesting")


security = HTTPBasic()

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
    "/auth",
    summary="Add a string to the LRU cache with basic auth - intentionally insecure",
)
def add_with_auth(
    credentials: HTTPBasicCredentials = Depends(security),
    data: Any = Body(...),
):
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = b"PUBLIC"  # This is not a secret
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = b"PUBLIC"  # This is not a secret
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

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
    return cache.as_json()


@router.delete(
    "",
    summary="Clear the LRU cache",
)
def clear_cache():
    cache.clear()
    return "Successfully cleared cache"
