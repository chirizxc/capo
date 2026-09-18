# Getting Started

## Installation

```
pip install capo-cost-and-usage-report-service
```

## Usage

```python
from capo_cost_and_usage_report_service import AsyncCostandUsageReportServiceClient


async def main():
    async with AsyncCostandUsageReportServiceClient() as costand_usage_report_service:
        # Example: call the delete_report_definition operation
        response = await costand_usage_report_service.delete_report_definition()
        print(response["response_message"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_cost_and_usage_report_service import AsyncCostandUsageReportServiceClient


async def main():
    async with AsyncCostandUsageReportServiceClient() as costand_usage_report_service:
        # Example: paginate over describe_report_definitions
        async for item in costand_usage_report_service.iter_describe_report_definitions():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_cost_and_usage_report_service import AsyncCostandUsageReportServiceClient
from capo_cost_and_usage_report_service.error import InternalErrorException


async def main():
    async with AsyncCostandUsageReportServiceClient() as costand_usage_report_service:
        try:
            await costand_usage_report_service.delete_report_definition()
        except InternalErrorException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_cost_and_usage_report_service import AsyncCostandUsageReportServiceClient


async def main():
    async with AsyncCostandUsageReportServiceClient() as costand_usage_report_service:
        # Default: 3 attempts for every operation
        response = await costand_usage_report_service.delete_report_definition()

        # Override per operation
        response = await costand_usage_report_service.delete_report_definition(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await costand_usage_report_service.delete_report_definition(config_overrides={"retry_max_attempts": 1})
```
