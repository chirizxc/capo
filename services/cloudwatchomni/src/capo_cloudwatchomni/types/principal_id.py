"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#PrincipalId``."""

from typing import TypeAlias

"""Principal receiving a grant. One field spans every AccessGrantPrincipalType: an IAM principal ARN (IAM_USER / IAM_ROLE / IAM_ROOT), an IdC UUID (IDC_USER / IDC_GROUP), or a service-defined id for ACCESS_PROFILE, ALERT, or AGENT. Must begin with an alphanumeric character. Set to the reserved value ALL (case-sensitive) to apply the grant to every ALERT principal in the space. ALL is supported only for the ALERT principal type, and only on CUSTOM grants whose single action is AssumeAccessProfile."""
PrincipalId: TypeAlias = str
