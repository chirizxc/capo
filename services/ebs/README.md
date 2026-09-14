# Getting Started

## Installation

```
pip install capo-ebs
```

## Usage

```python
from capo_ebs import AsyncEBSClient


async def main():
    async with AsyncEBSClient() as ebs:
        # Example: call the complete_snapshot operation
        response = await ebs.complete_snapshot()
        print(response["status"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ebs import AsyncEBSClient


async def main():
    async with AsyncEBSClient() as ebs:
        # Example: paginate over list_changed_blocks
        async for item in ebs.iter_list_changed_blocks():
            print(item)
```

## Streaming Request

Some operations accept a streaming request body. Pass an async iterator of `bytes` chunks, or the whole body as `bytes`, for the streaming parameter.

```python
from capo_ebs import AsyncEBSClient


async def main():
    async with AsyncEBSClient() as ebs:
        # Example: call put_snapshot_block with a streaming request body
        async def chunks():
            yield b'Hello, World!'

        response = await ebs.put_snapshot_block(block_data=chunks())
        print(response)

        # Or pass the whole body as bytes
        response = await ebs.put_snapshot_block(block_data=b'Hello, World!')
        print(response)
```

## Streaming Response

Some operations return a streaming response body. Use the operation as an async context manager and iterate over the response field to read chunks.

```python
from capo_ebs import AsyncEBSClient


async def main():
    async with AsyncEBSClient() as ebs:
        # Example: call get_snapshot_block and read the streaming response
        async with ebs.get_snapshot_block() as response:
            async for chunk in response["block_data"]:
                print(chunk)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ebs import AsyncEBSClient
from capo_ebs.error import AccessDeniedException


async def main():
    async with AsyncEBSClient() as ebs:
        try:
            await ebs.complete_snapshot()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ebs import AsyncEBSClient


async def main():
    async with AsyncEBSClient() as ebs:
        # Default: 3 attempts for every operation
        response = await ebs.complete_snapshot()

        # Override per operation
        response = await ebs.complete_snapshot(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ebs.complete_snapshot(config_overrides={"retry_max_attempts": 1})
```
