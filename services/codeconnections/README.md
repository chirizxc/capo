# Getting Started

## Installation

```
pip install capo-codeconnections
```

## Usage

```python
from capo_codeconnections import AsyncCodeConnectionsClient


async def main():
    async with AsyncCodeConnectionsClient() as code_connections:
        # Example: call the create_connection operation
        response = await code_connections.create_connection()
        print(response["connection_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_codeconnections import AsyncCodeConnectionsClient


async def main():
    async with AsyncCodeConnectionsClient() as code_connections:
        # Example: paginate over list_connections
        async for item in code_connections.iter_list_connections():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_codeconnections import AsyncCodeConnectionsClient
from capo_codeconnections.error import LimitExceededException


async def main():
    async with AsyncCodeConnectionsClient() as code_connections:
        try:
            await code_connections.create_connection()
        except LimitExceededException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_codeconnections import AsyncCodeConnectionsClient


async def main():
    async with AsyncCodeConnectionsClient() as code_connections:
        # Default: 3 attempts for every operation
        response = await code_connections.create_connection()

        # Override per operation
        response = await code_connections.create_connection(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await code_connections.create_connection(config_overrides={"retry_max_attempts": 1})
```
