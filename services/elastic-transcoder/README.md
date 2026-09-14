# Getting Started

## Installation

```
pip install capo-elastic-transcoder
```

## Usage

```python
from capo_elastic_transcoder import AsyncElasticTranscoderClient


async def main():
    async with AsyncElasticTranscoderClient() as elastic_transcoder:
        # Example: call the cancel_job operation
        response = await elastic_transcoder.cancel_job()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_elastic_transcoder import AsyncElasticTranscoderClient


async def main():
    async with AsyncElasticTranscoderClient() as elastic_transcoder:
        # Example: paginate over list_jobs_by_pipeline
        async for item in elastic_transcoder.iter_list_jobs_by_pipeline():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_elastic_transcoder import AsyncElasticTranscoderClient
from capo_elastic_transcoder.error import AccessDeniedException


async def main():
    async with AsyncElasticTranscoderClient() as elastic_transcoder:
        try:
            await elastic_transcoder.cancel_job()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_elastic_transcoder import AsyncElasticTranscoderClient


async def main():
    async with AsyncElasticTranscoderClient() as elastic_transcoder:
        # Default: 3 attempts for every operation
        response = await elastic_transcoder.cancel_job()

        # Override per operation
        response = await elastic_transcoder.cancel_job(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await elastic_transcoder.cancel_job(config_overrides={"retry_max_attempts": 1})
```
