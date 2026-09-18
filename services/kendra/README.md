# Getting Started

## Installation

```
pip install capo-kendra
```

## Usage

```python
from capo_kendra import AsynckendraClient


async def main():
    async with AsynckendraClient() as kendra:
        # Example: call the associate_entities_to_experience operation
        response = await kendra.associate_entities_to_experience()
        print(response["failed_entity_list"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_kendra import AsynckendraClient


async def main():
    async with AsynckendraClient() as kendra:
        # Example: paginate over get_snapshots
        async for item in kendra.iter_get_snapshots():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_kendra import AsynckendraClient
from capo_kendra.error import AccessDeniedException


async def main():
    async with AsynckendraClient() as kendra:
        try:
            await kendra.associate_entities_to_experience()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_kendra import AsynckendraClient


async def main():
    async with AsynckendraClient() as kendra:
        # Default: 3 attempts for every operation
        response = await kendra.associate_entities_to_experience()

        # Override per operation
        response = await kendra.associate_entities_to_experience(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await kendra.associate_entities_to_experience(config_overrides={"retry_max_attempts": 1})
```
