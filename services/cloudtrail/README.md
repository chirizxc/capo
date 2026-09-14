# Getting Started

## Installation

```
pip install capo-cloudtrail
```

## Usage

```python
from capo_cloudtrail import AsyncCloudTrailClient


async def main():
    async with AsyncCloudTrailClient() as cloud_trail:
        # Example: call the add_tags operation
        response = await cloud_trail.add_tags()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cloudtrail import AsyncCloudTrailClient


async def main():
    async with AsyncCloudTrailClient() as cloud_trail:
        # Example: paginate over get_query_results
        async for item in cloud_trail.iter_get_query_results():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudtrail import AsyncCloudTrailClient
from capo_cloudtrail.error import ChannelARNInvalidException


async def main():
    async with AsyncCloudTrailClient() as cloud_trail:
        try:
            await cloud_trail.add_tags()
        except ChannelARNInvalidException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudtrail import AsyncCloudTrailClient


async def main():
    async with AsyncCloudTrailClient() as cloud_trail:
        # Default: 3 attempts for every operation
        response = await cloud_trail.add_tags()

        # Override per operation
        response = await cloud_trail.add_tags(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_trail.add_tags(config_overrides={"retry_max_attempts": 1})
```
