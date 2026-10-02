# Getting Started

## Installation

```
pip install capo-sesv2
```

## Usage

```python
from capo_sesv2 import AsyncSESv2Client


async def main():
    async with AsyncSESv2Client() as se_sv2:
        # Example: call the associate_email_identity_certificate operation
        response = await se_sv2.associate_email_identity_certificate()
        print(response)
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_sesv2 import AsyncSESv2Client


async def main():
    async with AsyncSESv2Client() as se_sv2:
        # Example: paginate over get_dedicated_ips
        async for item in se_sv2.iter_get_dedicated_ips():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_sesv2 import AsyncSESv2Client
from capo_sesv2.error import AlreadyExistsException


async def main():
    async with AsyncSESv2Client() as se_sv2:
        try:
            await se_sv2.associate_email_identity_certificate()
        except AlreadyExistsException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_sesv2 import AsyncSESv2Client


async def main():
    async with AsyncSESv2Client() as se_sv2:
        # Default: 3 attempts for every operation
        response = await se_sv2.associate_email_identity_certificate()

        # Override per operation
        response = await se_sv2.associate_email_identity_certificate(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await se_sv2.associate_email_identity_certificate(config_overrides={"retry_max_attempts": 1})
```
