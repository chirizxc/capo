# Getting Started

## Installation

```
pip install capo-ecr-public
```

## Usage

```python
from capo_ecr_public import AsyncECRPUBLICClient


async def main():
    async with AsyncECRPUBLICClient() as ecrpublic:
        # Example: call the batch_check_layer_availability operation
        response = await ecrpublic.batch_check_layer_availability()
        print(response["layers"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_ecr_public import AsyncECRPUBLICClient


async def main():
    async with AsyncECRPUBLICClient() as ecrpublic:
        # Example: paginate over describe_images
        async for item in ecrpublic.iter_describe_images():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_ecr_public import AsyncECRPUBLICClient
from capo_ecr_public.error import InvalidParameterException


async def main():
    async with AsyncECRPUBLICClient() as ecrpublic:
        try:
            await ecrpublic.batch_check_layer_availability()
        except InvalidParameterException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_ecr_public import AsyncECRPUBLICClient


async def main():
    async with AsyncECRPUBLICClient() as ecrpublic:
        # Default: 3 attempts for every operation
        response = await ecrpublic.batch_check_layer_availability()

        # Override per operation
        response = await ecrpublic.batch_check_layer_availability(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await ecrpublic.batch_check_layer_availability(config_overrides={"retry_max_attempts": 1})
```
