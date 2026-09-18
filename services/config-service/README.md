# Getting Started

## Installation

```
pip install capo-config-service
```

## Usage

```python
from capo_config_service import AsyncConfigServiceClient


async def main():
    async with AsyncConfigServiceClient() as config_service:
        # Example: call the associate_resource_types operation
        response = await config_service.associate_resource_types()
        print(response["configuration_recorder"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_config_service import AsyncConfigServiceClient


async def main():
    async with AsyncConfigServiceClient() as config_service:
        # Example: paginate over describe_aggregate_compliance_by_config_rules
        async for item in config_service.iter_describe_aggregate_compliance_by_config_rules():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_config_service import AsyncConfigServiceClient
from capo_config_service.error import ConflictException


async def main():
    async with AsyncConfigServiceClient() as config_service:
        try:
            await config_service.associate_resource_types()
        except ConflictException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_config_service import AsyncConfigServiceClient


async def main():
    async with AsyncConfigServiceClient() as config_service:
        # Default: 3 attempts for every operation
        response = await config_service.associate_resource_types()

        # Override per operation
        response = await config_service.associate_resource_types(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await config_service.associate_resource_types(config_overrides={"retry_max_attempts": 1})
```
