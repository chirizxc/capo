# Getting Started

## Installation

```
pip install capo-resiliencehub
```

## Usage

```python
from capo_resiliencehub import AsyncresiliencehubClient


async def main():
    async with AsyncresiliencehubClient() as resiliencehub:
        # Example: call the accept_resource_grouping_recommendations operation
        response = await resiliencehub.accept_resource_grouping_recommendations()
        print(response["app_arn"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_resiliencehub import AsyncresiliencehubClient


async def main():
    async with AsyncresiliencehubClient() as resiliencehub:
        # Example: paginate over list_alarm_recommendations
        async for item in resiliencehub.iter_list_alarm_recommendations():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_resiliencehub import AsyncresiliencehubClient
from capo_resiliencehub.error import AccessDeniedException


async def main():
    async with AsyncresiliencehubClient() as resiliencehub:
        try:
            await resiliencehub.accept_resource_grouping_recommendations()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_resiliencehub import AsyncresiliencehubClient


async def main():
    async with AsyncresiliencehubClient() as resiliencehub:
        # Default: 3 attempts for every operation
        response = await resiliencehub.accept_resource_grouping_recommendations()

        # Override per operation
        response = await resiliencehub.accept_resource_grouping_recommendations(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await resiliencehub.accept_resource_grouping_recommendations(config_overrides={"retry_max_attempts": 1})
```
