# Getting Started

## Installation

```
pip install capo-cloud9
```

## Usage

```python
from capo_cloud9 import AsyncCloud9Client


async def main():
    async with AsyncCloud9Client() as cloud9:
        # Example: call the create_environment_ec2 operation
        response = await cloud9.create_environment_ec2()
        print(response["environment_id"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cloud9 import AsyncCloud9Client


async def main():
    async with AsyncCloud9Client() as cloud9:
        # Example: paginate over describe_environment_memberships
        async for item in cloud9.iter_describe_environment_memberships():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cloud9 import AsyncCloud9Client
from capo_cloud9.error import BadRequestException


async def main():
    async with AsyncCloud9Client() as cloud9:
        try:
            await cloud9.create_environment_ec2()
        except BadRequestException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cloud9 import AsyncCloud9Client


async def main():
    async with AsyncCloud9Client() as cloud9:
        # Default: 3 attempts for every operation
        response = await cloud9.create_environment_ec2()

        # Override per operation
        response = await cloud9.create_environment_ec2(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await cloud9.create_environment_ec2(config_overrides={"retry_max_attempts": 1})
```
