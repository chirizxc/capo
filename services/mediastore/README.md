# Getting Started

## Installation

```
pip install capo-mediastore
```

## Usage

```python
from capo_mediastore import AsyncMediaStoreClient


async def main():
    async with AsyncMediaStoreClient() as media_store:
        # Example: call the create_container operation
        response = await media_store.create_container()
        print(response["container"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_mediastore import AsyncMediaStoreClient


async def main():
    async with AsyncMediaStoreClient() as media_store:
        # Example: paginate over list_containers
        async for item in media_store.iter_list_containers():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_mediastore import AsyncMediaStoreClient
from capo_mediastore.error import ContainerInUseException


async def main():
    async with AsyncMediaStoreClient() as media_store:
        try:
            await media_store.create_container()
        except ContainerInUseException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_mediastore import AsyncMediaStoreClient


async def main():
    async with AsyncMediaStoreClient() as media_store:
        # Default: 3 attempts for every operation
        response = await media_store.create_container()

        # Override per operation
        response = await media_store.create_container(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await media_store.create_container(config_overrides={"retry_max_attempts": 1})
```
