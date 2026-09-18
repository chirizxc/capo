# Getting Started

## Installation

```
pip install capo-pricing
```

## Usage

```python
from capo_pricing import AsyncPricingClient


async def main():
    async with AsyncPricingClient() as pricing:
        # Example: call the describe_services operation
        response = await pricing.describe_services()
        print(response["services"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_pricing import AsyncPricingClient


async def main():
    async with AsyncPricingClient() as pricing:
        # Example: paginate over describe_services
        async for item in pricing.iter_describe_services():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_pricing import AsyncPricingClient
from capo_pricing.error import AccessDeniedException


async def main():
    async with AsyncPricingClient() as pricing:
        try:
            await pricing.describe_services()
        except AccessDeniedException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_pricing import AsyncPricingClient


async def main():
    async with AsyncPricingClient() as pricing:
        # Default: 3 attempts for every operation
        response = await pricing.describe_services()

        # Override per operation
        response = await pricing.describe_services(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await pricing.describe_services(config_overrides={"retry_max_attempts": 1})
```
