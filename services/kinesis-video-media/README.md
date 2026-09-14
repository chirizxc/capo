# Getting Started

## Installation

```
pip install capo-kinesis-video-media
```

## Usage

```python
from capo_kinesis_video_media import AsyncKinesisVideoMediaClient


async def main():
    async with AsyncKinesisVideoMediaClient() as kinesis_video_media:
        # Example: call the get_media operation
        response = await kinesis_video_media.get_media()
        print(response["content_type"])
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_kinesis_video_media import AsyncKinesisVideoMediaClient


async def main():
    async with AsyncKinesisVideoMediaClient() as kinesis_video_media:
        # Example: call get_media and read the streaming response
        async with kinesis_video_media.get_media() as response:
            async for chunk in response["payload"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_kinesis_video_media import AsyncKinesisVideoMediaClient
from capo_kinesis_video_media.error import ClientLimitExceededException


async def main():
    async with AsyncKinesisVideoMediaClient() as kinesis_video_media:
        try:
            await kinesis_video_media.get_media()
        except ClientLimitExceededException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_kinesis_video_media import AsyncKinesisVideoMediaClient


async def main():
    async with AsyncKinesisVideoMediaClient() as kinesis_video_media:
        # Default: 3 attempts for every operation
        response = await kinesis_video_media.get_media()

        # Override per operation
        response = await kinesis_video_media.get_media(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await kinesis_video_media.get_media(config_overrides={"retry_max_attempts": 1})
```
