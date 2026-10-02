# Getting Started

## Installation

```
pip install capo-rum
```

## Usage

```python
from capo_rum import AsyncRUMClient


async def main():
    async with AsyncRUMClient() as rum:
        # Example: call the list_tags_for_resource operation
        response = await rum.list_tags_for_resource()
        print(response["resource_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_rum import AsyncRUMClient


async def main():
    async with AsyncRUMClient() as rum:
        # Example: paginate over list_app_monitors
        async for item in rum.iter_list_app_monitors():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_rum import AsyncRUMClient
from capo_rum.error import InternalServerException


async def main():
    async with AsyncRUMClient() as rum:
        try:
            await rum.list_tags_for_resource()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_rum import AsyncRUMClient


async def main():
    async with AsyncRUMClient() as rum:
        # Default: 3 attempts for every operation
        response = await rum.list_tags_for_resource()

        # Override per operation
        response = await rum.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await rum.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
