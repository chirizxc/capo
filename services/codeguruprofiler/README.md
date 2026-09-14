# Getting Started

## Installation

```
pip install capo-codeguruprofiler
```

## Usage

```python
from capo_codeguruprofiler import AsyncCodeGuruProfilerClient


async def main():
    async with AsyncCodeGuruProfilerClient() as code_guru_profiler:
        # Example: call the get_findings_report_account_summary operation
        response = await code_guru_profiler.get_findings_report_account_summary()
        print(response["report_summaries"])
```

## Pagination

Some operations in this SDK support pagination. If the operation supports pagination it will have an `iter_` prefixed method that returns an async iterator.

```python
from capo_codeguruprofiler import AsyncCodeGuruProfilerClient


async def main():
    async with AsyncCodeGuruProfilerClient() as code_guru_profiler:
        # Example: paginate over get_findings_report_account_summary
        async for item in code_guru_profiler.iter_get_findings_report_account_summary():
            print(item)
```

## Error Handling

The SDK raises exceptions for errors returned by the API. Catch them to handle failures gracefully.

```python
from capo_codeguruprofiler import AsyncCodeGuruProfilerClient
from capo_codeguruprofiler.error import InternalServerException


async def main():
    async with AsyncCodeGuruProfilerClient() as code_guru_profiler:
        try:
            await code_guru_profiler.get_findings_report_account_summary()
        except InternalServerException as e:
            print(f"Error: {e}")
            print(e.data)  # additional error data
```

## Retrying

The SDK retries failed operations automatically. Retry behaviour follows the Smithy specification: errors are retried based on their `is_retryable` and `is_throttling_error` attributes. Throttling errors use a longer base delay. Network-level failures (connection errors and timeouts) are also retried. Non-retryable errors, such as client errors without the `@retryable` trait, are raised immediately without further attempts.

The number of attempts defaults to 3 and can be changed at the client level via `retry_max_attempts`, or per call via `config_overrides`.

```python
from capo_codeguruprofiler import AsyncCodeGuruProfilerClient


async def main():
    async with AsyncCodeGuruProfilerClient() as code_guru_profiler:
        # Default: 3 attempts for every operation
        response = await code_guru_profiler.get_findings_report_account_summary()

        # Override per operation
        response = await code_guru_profiler.get_findings_report_account_summary(config_overrides={"retry_max_attempts": 5})

        # Disable retries for this call
        response = await code_guru_profiler.get_findings_report_account_summary(config_overrides={"retry_max_attempts": 1})
```
