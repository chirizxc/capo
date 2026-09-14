# Getting Started

## Installation

```
pip install capo-forecastquery
```

## Usage

```python
from capo_forecastquery import AsyncforecastqueryClient


async def main():
    async with AsyncforecastqueryClient() as forecastquery:
        # Example: call the query_forecast operation
        response = await forecastquery.query_forecast()
        print(response["forecast"])
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_forecastquery import AsyncforecastqueryClient
from capo_forecastquery.error import InvalidInputException


async def main():
    async with AsyncforecastqueryClient() as forecastquery:
        try:
            await forecastquery.query_forecast()
        except InvalidInputException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_forecastquery import AsyncforecastqueryClient


async def main():
    async with AsyncforecastqueryClient() as forecastquery:
        # Default: 3 attempts for every operation
        response = await forecastquery.query_forecast()

        # Override per operation
        response = await forecastquery.query_forecast(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await forecastquery.query_forecast(config_overrides={"retry_max_attempts": 1})
```
