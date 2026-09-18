# Getting Started

## Installation

```
pip install capo-connectcases
```

## Usage

```python
from capo_connectcases import AsyncConnectCasesClient


async def main():
    async with AsyncConnectCasesClient() as connect_cases:
        # Example: call the list_tags_for_resource operation
        response = await connect_cases.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_connectcases import AsyncConnectCasesClient


async def main():
    async with AsyncConnectCasesClient() as connect_cases:
        # Example: paginate over get_case
        async for item in connect_cases.iter_get_case():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_connectcases import AsyncConnectCasesClient
from capo_connectcases.error import AccessDeniedException


async def main():
    async with AsyncConnectCasesClient() as connect_cases:
        try:
            await connect_cases.list_tags_for_resource()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_connectcases import AsyncConnectCasesClient


async def main():
    async with AsyncConnectCasesClient() as connect_cases:
        # Default: 3 attempts for every operation
        response = await connect_cases.list_tags_for_resource()

        # Override per operation
        response = await connect_cases.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await connect_cases.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
