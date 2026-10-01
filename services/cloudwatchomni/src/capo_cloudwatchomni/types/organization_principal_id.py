"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#OrganizationPrincipalId``."""

from typing import TypeAlias

"""Principal receiving an organization-level domain access grant. One field spans every OrganizationGrantPrincipalType: an IAM principal ARN (IAM_USER / IAM_ROLE / IAM_ROOT) or an IdC UUID (IDC_USER / IDC_GROUP). Must begin with an alphanumeric character."""
OrganizationPrincipalId: TypeAlias = str
