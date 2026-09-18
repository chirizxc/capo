# Getting Started

## Installation

```
pip install capo-translate
```

## Usage

```python
from capo_translate import AsyncTranslateClient


async def main():
    async with AsyncTranslateClient() as translate:
        # Example: call the create_parallel_data operation
        response = await translate.create_parallel_data()
        print(response["name"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_translate import AsyncTranslateClient


async def main():
    async with AsyncTranslateClient() as translate:
        # Example: paginate over list_languages
        async for item in translate.iter_list_languages():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_translate import AsyncTranslateClient
from capo_translate.error import ConcurrentModificationException


async def main():
    async with AsyncTranslateClient() as translate:
        try:
            await translate.create_parallel_data()
        except ConcurrentModificationException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_translate import AsyncTranslateClient


async def main():
    async with AsyncTranslateClient() as translate:
        # Default: 3 attempts for every operation
        response = await translate.create_parallel_data()

        # Override per operation
        response = await translate.create_parallel_data(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await translate.create_parallel_data(config_overrides={"retry_max_attempts": 1})
```
