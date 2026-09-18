# Getting Started

## Installation

```
pip install capo-chime-sdk-media-pipelines
```

## Usage

```python
from capo_chime_sdk_media_pipelines import AsyncChimeSDKMediaPipelinesClient


async def main():
    async with AsyncChimeSDKMediaPipelinesClient() as chime_sdk_media_pipelines:
        # Example: call the create_media_capture_pipeline operation
        response = await chime_sdk_media_pipelines.create_media_capture_pipeline()
        print(response["media_capture_pipeline"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_chime_sdk_media_pipelines import AsyncChimeSDKMediaPipelinesClient


async def main():
    async with AsyncChimeSDKMediaPipelinesClient() as chime_sdk_media_pipelines:
        # Example: paginate over list_media_capture_pipelines
        async for item in chime_sdk_media_pipelines.iter_list_media_capture_pipelines():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_chime_sdk_media_pipelines import AsyncChimeSDKMediaPipelinesClient
from capo_chime_sdk_media_pipelines.error import BadRequestException


async def main():
    async with AsyncChimeSDKMediaPipelinesClient() as chime_sdk_media_pipelines:
        try:
            await chime_sdk_media_pipelines.create_media_capture_pipeline()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_chime_sdk_media_pipelines import AsyncChimeSDKMediaPipelinesClient


async def main():
    async with AsyncChimeSDKMediaPipelinesClient() as chime_sdk_media_pipelines:
        # Default: 3 attempts for every operation
        response = await chime_sdk_media_pipelines.create_media_capture_pipeline()

        # Override per operation
        response = await chime_sdk_media_pipelines.create_media_capture_pipeline(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await chime_sdk_media_pipelines.create_media_capture_pipeline(config_overrides={"retry_max_attempts": 1})
```
