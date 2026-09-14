# Getting Started

## Installation

```
pip install capo-detective
```

## Usage

```python
from capo_detective import AsyncDetectiveClient


async def main():
    async with AsyncDetectiveClient() as detective:
        # Example: call the accept_invitation operation
        response = await detective.accept_invitation()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_detective import AsyncDetectiveClient


async def main():
    async with AsyncDetectiveClient() as detective:
        # Example: paginate over list_datasource_packages
        async for item in detective.iter_list_datasource_packages():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_detective import AsyncDetectiveClient
from capo_detective.error import AccessDeniedException


async def main():
    async with AsyncDetectiveClient() as detective:
        try:
            await detective.accept_invitation()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_detective import AsyncDetectiveClient


async def main():
    async with AsyncDetectiveClient() as detective:
        # Default: 3 attempts for every operation
        response = await detective.accept_invitation()

        # Override per operation
        response = await detective.accept_invitation(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await detective.accept_invitation(config_overrides={"retry_max_attempts": 1})
```
