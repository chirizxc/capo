# Getting Started

## Installation

```
pip install capo-cloudhsm-v2
```

## Usage

```python
from capo_cloudhsm_v2 import AsyncCloudHSMV2Client


async def main():
    async with AsyncCloudHSMV2Client() as cloud_hsmv2:
        # Example: call the copy_backup_to_region operation
        response = await cloud_hsmv2.copy_backup_to_region()
        print(response["destination_backup"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cloudhsm_v2 import AsyncCloudHSMV2Client


async def main():
    async with AsyncCloudHSMV2Client() as cloud_hsmv2:
        # Example: paginate over describe_backups
        async for item in cloud_hsmv2.iter_describe_backups():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloudhsm_v2 import AsyncCloudHSMV2Client
from capo_cloudhsm_v2.error import CloudHsmAccessDeniedException


async def main():
    async with AsyncCloudHSMV2Client() as cloud_hsmv2:
        try:
            await cloud_hsmv2.copy_backup_to_region()
        except CloudHsmAccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloudhsm_v2 import AsyncCloudHSMV2Client


async def main():
    async with AsyncCloudHSMV2Client() as cloud_hsmv2:
        # Default: 3 attempts for every operation
        response = await cloud_hsmv2.copy_backup_to_region()

        # Override per operation
        response = await cloud_hsmv2.copy_backup_to_region(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud_hsmv2.copy_backup_to_region(config_overrides={"retry_max_attempts": 1})
```
