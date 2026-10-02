import pytest
from capo_wellarchitected._rule_engine._endpoint_rule_set import EndpointParams, resolve
from capo_wellarchitected._rule_engine._endpoint_runtime import EndpointError
import re
import zapros

def test_for_custom_endpoint_with_region_not_set_():
    """For custom endpoint with region not set and fips disabled"""
    params = EndpointParams(Endpoint='https://example.com', UseFIPS=False)
    result = resolve(params)
    assert result.url == 'https://example.com'

def test_for_custom_endpoint_with_fips_enabled():
    """For custom endpoint with fips enabled"""
    params = EndpointParams(Endpoint='https://example.com', UseFIPS=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: FIPS and custom endpoint are not supported')):
        resolve(params)

def test_for_custom_endpoint_with_fips_disabled_a():
    """For custom endpoint with fips disabled and dualstack enabled"""
    params = EndpointParams(Endpoint='https://example.com', UseFIPS=False, UseDualStack=True)
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Dualstack and custom endpoint are not supported')):
        resolve(params)

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wellarchitected-fips.us-east-1.api.aws'

def test_for_region_us_east_1_with_fips_enabled_a():
    """For region us-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected-fips.us-east-1.amazonaws.com'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wellarchitected.us-east-1.api.aws'

def test_for_region_us_east_1_with_fips_disabled_():
    """For region us-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected.us-east-1.amazonaws.com'

def test_for_region_cn_northwest_1_with_fips_enab():
    """For region cn-northwest-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wellarchitected-fips.cn-northwest-1.api.amazonwebservices.com.cn'

def test_for_region_cn_northwest_1_with_fips_enab():
    """For region cn-northwest-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected-fips.cn-northwest-1.amazonaws.com.cn'

def test_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wellarchitected.cn-northwest-1.api.amazonwebservices.com.cn'

def test_for_region_cn_northwest_1_with_fips_disa():
    """For region cn-northwest-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='cn-northwest-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected.cn-northwest-1.amazonaws.com.cn'

def test_for_region_eusc_de_east_1_with_fips_enab():
    """For region eusc-de-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='eusc-de-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected-fips.eusc-de-east-1.amazonaws.eu'

def test_for_region_eusc_de_east_1_with_fips_disa():
    """For region eusc-de-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eusc-de-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected.eusc-de-east-1.amazonaws.eu'

def test_for_region_us_iso_east_1_with_fips_enabl():
    """For region us-iso-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected-fips.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_iso_east_1_with_fips_disab():
    """For region us-iso-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-iso-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected.us-iso-east-1.c2s.ic.gov'

def test_for_region_us_isob_east_1_with_fips_enab():
    """For region us-isob-east-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected-fips.us-isob-east-1.sc2s.sgov.gov'

def test_for_region_us_isob_east_1_with_fips_disa():
    """For region us-isob-east-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isob-east-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected.us-isob-east-1.sc2s.sgov.gov'

def test_for_region_eu_isoe_west_1_with_fips_enab():
    """For region eu-isoe-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='eu-isoe-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected-fips.eu-isoe-west-1.cloud.adc-e.uk'

def test_for_region_eu_isoe_west_1_with_fips_disa():
    """For region eu-isoe-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='eu-isoe-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected.eu-isoe-west-1.cloud.adc-e.uk'

def test_for_region_us_isof_south_1_with_fips_ena():
    """For region us-isof-south-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-isof-south-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected-fips.us-isof-south-1.csp.hci.ic.gov'

def test_for_region_us_isof_south_1_with_fips_dis():
    """For region us-isof-south-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-isof-south-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected.us-isof-south-1.csp.hci.ic.gov'

def test_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wellarchitected-fips.us-gov-west-1.api.aws'

def test_for_region_us_gov_west_1_with_fips_enabl():
    """For region us-gov-west-1 with FIPS enabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=True, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected-fips.us-gov-west-1.amazonaws.com'

def test_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack enabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=True)
    result = resolve(params)
    assert result.url == 'https://wellarchitected.us-gov-west-1.api.aws'

def test_for_region_us_gov_west_1_with_fips_disab():
    """For region us-gov-west-1 with FIPS disabled and DualStack disabled"""
    params = EndpointParams(Region='us-gov-west-1', UseFIPS=False, UseDualStack=False)
    result = resolve(params)
    assert result.url == 'https://wellarchitected.us-gov-west-1.amazonaws.com'

def test_missing_region():
    """Missing region"""
    params = EndpointParams()
    with pytest.raises(EndpointError, match=re.escape('Invalid Configuration: Missing Region')):
        resolve(params)

def test_agent_case__standard_region__no_fips__no():
    """AGENT case: standard region, no FIPS, no DualStack -> amazonaws.com"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, SubServiceType='AGENT')
    result = resolve(params)
    assert result.url == 'https://wellarchitected-agent.us-east-1.amazonaws.com'

def test_agent_case__fips_enabled____amazonaws_co():
    """AGENT case: FIPS enabled -> amazonaws.com with -fips"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=False, SubServiceType='AGENT')
    result = resolve(params)
    assert result.url == 'https://wellarchitected-agent-fips.us-east-1.amazonaws.com'

def test_agent_case__dualstack_enabled____api_aws():
    """AGENT case: DualStack enabled -> api.aws"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=True, SubServiceType='AGENT')
    result = resolve(params)
    assert result.url == 'https://wellarchitected-agent.us-west-2.api.aws'

def test_agent_case__fips___dualstack____api_aws_():
    """AGENT case: FIPS + DualStack -> api.aws with -fips"""
    params = EndpointParams(Region='us-east-1', UseFIPS=True, UseDualStack=True, SubServiceType='AGENT')
    result = resolve(params)
    assert result.url == 'https://wellarchitected-agent-fips.us-east-1.api.aws'

def test_agent_case__us_west_2_standard____amazon():
    """AGENT case: us-west-2 standard -> amazonaws.com"""
    params = EndpointParams(Region='us-west-2', UseFIPS=False, UseDualStack=False, SubServiceType='AGENT')
    result = resolve(params)
    assert result.url == 'https://wellarchitected-agent.us-west-2.amazonaws.com'

def test_agent_case__custom_endpoint_override_sti():
    """AGENT case: custom endpoint override still works"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, SubServiceType='AGENT', Endpoint='https://custom.endpoint.example.com')
    result = resolve(params)
    assert result.url == 'https://custom.endpoint.example.com'

def test_non_agent_subservicetype_falls_through_t():
    """Non-AGENT SubServiceType falls through to the base WA endpoint"""
    params = EndpointParams(Region='us-east-1', UseFIPS=False, UseDualStack=False, SubServiceType='SOMETHING-ELSE')
    result = resolve(params)
    assert result.url == 'https://wellarchitected.us-east-1.amazonaws.com'