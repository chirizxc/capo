# Getting Started

## Installation

```
pip install capo-route53-recovery-control-config
```

## Usage

```python
from capo_route53_recovery_control_config import AsyncRoute53RecoveryControlConfigClient


async def main():
    async with AsyncRoute53RecoveryControlConfigClient() as route53_recovery_control_config:
        # Example: call the create_cluster operation
        response = await route53_recovery_control_config.create_cluster()
        print(response["cluster"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_route53_recovery_control_config import AsyncRoute53RecoveryControlConfigClient


async def main():
    async with AsyncRoute53RecoveryControlConfigClient() as route53_recovery_control_config:
        # Example: paginate over list_associated_route53_health_checks
        async for item in route53_recovery_control_config.iter_list_associated_route53_health_checks():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_route53_recovery_control_config import AsyncRoute53RecoveryControlConfigClient
from capo_route53_recovery_control_config.error import AccessDeniedException


async def main():
    async with AsyncRoute53RecoveryControlConfigClient() as route53_recovery_control_config:
        try:
            await route53_recovery_control_config.create_cluster()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_route53_recovery_control_config import AsyncRoute53RecoveryControlConfigClient


async def main():
    async with AsyncRoute53RecoveryControlConfigClient() as route53_recovery_control_config:
        # Default: 3 attempts for every operation
        response = await route53_recovery_control_config.create_cluster()

        # Override per operation
        response = await route53_recovery_control_config.create_cluster(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await route53_recovery_control_config.create_cluster(config_overrides={"retry_max_attempts": 1})
```
