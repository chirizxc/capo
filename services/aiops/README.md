# Getting Started

## Installation

```
pip install capo-aiops
```

## Usage

```python
from capo_aiops import AsyncAIOpsClient


async def main():
    async with AsyncAIOpsClient() as ai_ops:
        # Example: call the list_tags_for_resource operation
        response = await ai_ops.list_tags_for_resource()
        print(response["tags"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_aiops import AsyncAIOpsClient


async def main():
    async with AsyncAIOpsClient() as ai_ops:
        # Example: paginate over list_investigation_groups
        async for item in ai_ops.iter_list_investigation_groups():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_aiops import AsyncAIOpsClient
from capo_aiops.error import AccessDeniedException


async def main():
    async with AsyncAIOpsClient() as ai_ops:
        try:
            await ai_ops.list_tags_for_resource()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_aiops import AsyncAIOpsClient


async def main():
    async with AsyncAIOpsClient() as ai_ops:
        # Default: 3 attempts for every operation
        response = await ai_ops.list_tags_for_resource()

        # Override per operation
        response = await ai_ops.list_tags_for_resource(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ai_ops.list_tags_for_resource(config_overrides={"retry_max_attempts": 1})
```
