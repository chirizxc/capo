# Getting Started

## Installation

```
pip install capo-athena
```

## Usage

```python
from capo_athena import AsyncAthenaClient


async def main():
    async with AsyncAthenaClient() as athena:
        # Example: call the batch_get_named_query operation
        response = await athena.batch_get_named_query()
        print(response["named_queries"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_athena import AsyncAthenaClient


async def main():
    async with AsyncAthenaClient() as athena:
        # Example: paginate over get_query_results
        async for item in athena.iter_get_query_results():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_athena import AsyncAthenaClient
from capo_athena.error import InternalServerException


async def main():
    async with AsyncAthenaClient() as athena:
        try:
            await athena.batch_get_named_query()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_athena import AsyncAthenaClient


async def main():
    async with AsyncAthenaClient() as athena:
        # Default: 3 attempts for every operation
        response = await athena.batch_get_named_query()

        # Override per operation
        response = await athena.batch_get_named_query(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await athena.batch_get_named_query(config_overrides={"retry_max_attempts": 1})
```
