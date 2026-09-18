# Getting Started

## Installation

```
pip install capo-snowball
```

## Usage

```python
from capo_snowball import AsyncSnowballClient


async def main():
    async with AsyncSnowballClient() as snowball:
        # Example: call the cancel_cluster operation
        response = await snowball.cancel_cluster()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_snowball import AsyncSnowballClient


async def main():
    async with AsyncSnowballClient() as snowball:
        # Example: paginate over describe_addresses
        async for item in snowball.iter_describe_addresses():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_snowball import AsyncSnowballClient
from capo_snowball.error import InvalidJobStateException


async def main():
    async with AsyncSnowballClient() as snowball:
        try:
            await snowball.cancel_cluster()
        except InvalidJobStateException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_snowball import AsyncSnowballClient


async def main():
    async with AsyncSnowballClient() as snowball:
        # Default: 3 attempts for every operation
        response = await snowball.cancel_cluster()

        # Override per operation
        response = await snowball.cancel_cluster(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await snowball.cancel_cluster(config_overrides={"retry_max_attempts": 1})
```
