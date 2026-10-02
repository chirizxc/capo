import pytest
from capo_eventbridgev2._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_eventbridgev2._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_bus_arn_account_takes_precedence_over_th():
    """Bus ARN account takes precedence over the credentials-sourced account (cross-account call)."""
    params = EndpointParams(Region='us-east-1', EventBusArn='arn:aws:events:us-east-1:210987654321:event-busv2/owner-bus/abcdefghij0123456789abcde', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://210987654321.eventsv2.us-east-1.amazonaws.com'

def test_bus_arn_routing_works_without_a_credenti():
    """Bus ARN routing works without a credentials-sourced account ID."""
    params = EndpointParams(Region='us-east-1', EventBusArn='arn:aws:events:us-east-1:210987654321:event-busv2/owner-bus/abcdefghij0123456789abcde', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://210987654321.eventsv2.us-east-1.amazonaws.com'

def test_disabled_mode_ignores_the_bus_arn_and_th():
    """Disabled mode ignores the bus ARN and the credentials-sourced account."""
    params = EndpointParams(Region='us-east-1', EventBusArn='arn:aws:events:us-east-1:210987654321:event-busv2/owner-bus/abcdefghij0123456789abcde', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://eventsv2.us-east-1.amazonaws.com'

def test_an_unparseable_bus_arn_falls_through_to_():
    """An unparseable bus ARN falls through to the credentials-sourced account."""
    params = EndpointParams(Region='us-east-1', EventBusArn='not-an-arn', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2.us-east-1.amazonaws.com'

def test_fips_account_based_endpoint_from_the_bus():
    """FIPS account-based endpoint from the bus ARN."""
    params = EndpointParams(Region='us-east-1', EventBusArn='arn:aws:events:us-east-1:210987654321:event-busv2/owner-bus/abcdefghij0123456789abcde', AccountIdEndpointMode='preferred', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://210987654321.eventsv2-fips.us-east-1.amazonaws.com'

def test_dualstack_account_based_endpoint_from_th():
    """DualStack account-based endpoint from the bus ARN."""
    params = EndpointParams(Region='us-east-1', EventBusArn='arn:aws:events:us-east-1:210987654321:event-busv2/owner-bus/abcdefghij0123456789abcde', AccountIdEndpointMode='preferred', UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://210987654321.eventsv2.us-east-1.api.aws'

def test_fips___dualstack_account_based_endpoint_():
    """FIPS + DualStack account-based endpoint from the bus ARN."""
    params = EndpointParams(Region='us-east-1', EventBusArn='arn:aws:events:us-east-1:210987654321:event-busv2/owner-bus/abcdefghij0123456789abcde', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://210987654321.eventsv2-fips.us-east-1.api.aws'

def test_fips_account_based_endpoint_from_the_cre():
    """FIPS account-based endpoint from the credentials-sourced account."""
    params = EndpointParams(Region='us-east-1', AccountId='123456789012', AccountIdEndpointMode='preferred', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2-fips.us-east-1.amazonaws.com'

def test_fips___dualstack_account_based_endpoint_():
    """FIPS + DualStack account-based endpoint from the credentials-sourced account."""
    params = EndpointParams(Region='us-east-1', AccountId='123456789012', AccountIdEndpointMode='preferred', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2-fips.us-east-1.api.aws'

def test_explicit_endpoint_override_wins_over_acc():
    """Explicit endpoint override wins over account-based routing."""
    params = EndpointParams(Region='us-east-1', Endpoint='https://example.com', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_fips_cannot_be_combined_with_an_endpoint():
    """FIPS cannot be combined with an endpoint override."""
    params = EndpointParams(Region='us-east-1', Endpoint='https://example.com', UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_dualstack_cannot_be_combined_with_an_end():
    """DualStack cannot be combined with an endpoint override."""
    params = EndpointParams(Region='us-east-1', Endpoint='https://example.com', UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_account_based_endpoint_when_mode_is_pref():
    """Account-based endpoint when mode is preferred and account ID is available."""
    params = EndpointParams(Region='us-east-1', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2.us-east-1.amazonaws.com'

def test_regional_endpoint_when_mode_is_disabled_():
    """Regional endpoint when mode is disabled."""
    params = EndpointParams(Region='us-east-1', AccountId='123456789012', AccountIdEndpointMode='disabled')
    result = resolve(params)
    assert result.url == 'https://eventsv2.us-east-1.amazonaws.com'

def test_regional_fips_endpoint_when_mode_is_disa():
    """Regional FIPS endpoint when mode is disabled."""
    params = EndpointParams(Region='us-east-1', AccountId='123456789012', AccountIdEndpointMode='disabled', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://eventsv2-fips.us-east-1.amazonaws.com'

def test_regional_dualstack_endpoint_when_mode_is():
    """Regional DualStack endpoint when mode is disabled."""
    params = EndpointParams(Region='us-east-1', AccountId='123456789012', AccountIdEndpointMode='disabled', UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://eventsv2.us-east-1.api.aws'

def test_regional_fips___dualstack_endpoint_when_():
    """Regional FIPS + DualStack endpoint when mode is disabled."""
    params = EndpointParams(Region='us-east-1', AccountId='123456789012', AccountIdEndpointMode='disabled', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://eventsv2-fips.us-east-1.api.aws'

def test_regional_endpoint_when_no_account_id_is_():
    """Regional endpoint when no account ID is available and mode is preferred."""
    params = EndpointParams(Region='eu-west-1', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://eventsv2.eu-west-1.amazonaws.com'

def test_error_when_mode_is_required_but_no_accou():
    """Error when mode is required but no account ID is available."""
    params = EndpointParams(Region='us-east-1', AccountIdEndpointMode='required')
    with pytest.raises(EndpointError, match=re.escape('AccountIdEndpointMode is required but no AccountID was provided or able to be loaded')):
        resolve(params)

def test_account_based_endpoint_in_the_aws_cn_par():
    """Account-based endpoint in the aws-cn partition when mode is required (account routing works in every partition)."""
    params = EndpointParams(Region='cn-north-1', AccountId='123456789012', AccountIdEndpointMode='required')
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2.cn-north-1.amazonaws.com.cn'

def test_error_when_the_credentials_sourced_accou():
    """Error when the credentials-sourced account ID is not a valid host label."""
    params = EndpointParams(Region='us-east-1', AccountId='not/valid', AccountIdEndpointMode='preferred')
    with pytest.raises(EndpointError, match=re.escape('Credentials-sourced account ID parameter is invalid')):
        resolve(params)

def test_regional_endpoint_when_accountidendpoint():
    """Regional endpoint when AccountIdEndpointMode is not set at all, even with an account ID and bus ARN available. The explicit empty properties pin that regional endpoints carry no adoption metric."""
    params = EndpointParams(Region='us-east-1', EventBusArn='arn:aws:events:us-east-1:210987654321:event-busv2/owner-bus/abcdefghij0123456789abcde', AccountId='123456789012')
    result = resolve(params)
    assert result.url == 'https://eventsv2.us-east-1.amazonaws.com'

def test_account_based_endpoint_in_the_aws_us_gov():
    """Account-based endpoint in the aws-us-gov partition when mode is preferred (account routing works in every partition)."""
    params = EndpointParams(Region='us-gov-west-1', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2.us-gov-west-1.amazonaws.com'

def test_account_based_fips_endpoint_in_the_aws_u():
    """Account-based FIPS endpoint in the aws-us-gov partition when mode is required."""
    params = EndpointParams(Region='us-gov-west-1', AccountId='123456789012', AccountIdEndpointMode='required', UseFIPS=True)
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2-fips.us-gov-west-1.amazonaws.com'

def test_account_based_endpoint_in_the_aws_iso_pa():
    """Account-based endpoint in the aws-iso partition when mode is preferred, composing the iso DNS suffix."""
    params = EndpointParams(Region='us-iso-east-1', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2.us-iso-east-1.c2s.ic.gov'

def test_dualstack_account_based_endpoint_in_the_():
    """DualStack account-based endpoint in the aws-iso partition, composing the iso dualstack DNS suffix."""
    params = EndpointParams(Region='us-iso-east-1', AccountId='123456789012', AccountIdEndpointMode='preferred', UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2.us-iso-east-1.api.aws.ic.gov'

def test_a_parseable_bus_arn_whose_account_is_not():
    """A parseable bus ARN whose account is not a valid host label falls through to the credentials-sourced account."""
    params = EndpointParams(Region='us-east-1', EventBusArn='arn:aws:events:us-east-1:not_a_valid_label!:event-busv2/owner-bus/abcdefghij0123456789abcde', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2.us-east-1.amazonaws.com'

def test_a_bus_arn_for_another_service_falls_thro():
    """A bus ARN for another service falls through to the credentials-sourced account."""
    params = EndpointParams(Region='us-east-1', EventBusArn='arn:aws:sqs:us-east-1:210987654321:some-queue', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2.us-east-1.amazonaws.com'

def test_cross_region_bus_arn__the_arn_account_ro():
    """Cross-region bus ARN: the ARN account routes within the CLIENT region (cells are per-account per-region)."""
    params = EndpointParams(Region='us-west-2', EventBusArn='arn:aws:events:us-east-1:210987654321:event-busv2/owner-bus/abcdefghij0123456789abcde', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://210987654321.eventsv2.us-west-2.amazonaws.com'

def test_required_mode_succeeds_through_the_bus_a():
    """Required mode succeeds through the bus ARN account."""
    params = EndpointParams(Region='us-east-1', EventBusArn='arn:aws:events:us-east-1:210987654321:event-busv2/owner-bus/abcdefghij0123456789abcde', AccountIdEndpointMode='required')
    result = resolve(params)
    assert result.url == 'https://210987654321.eventsv2.us-east-1.amazonaws.com'

def test_account_based_endpoint_in_the_aws_cn_par():
    """Account-based endpoint in the aws-cn partition when mode is preferred, composing the cn DNS suffix."""
    params = EndpointParams(Region='cn-north-1', AccountId='123456789012', AccountIdEndpointMode='preferred')
    result = resolve(params)
    assert result.url == 'https://123456789012.eventsv2.cn-north-1.amazonaws.com.cn'