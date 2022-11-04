import pytest
from myconfig import the_config
from SibylSystem import PsychoPass

@pytest.mark.asyncio
async def test_sibyl_client01():
    sibyl_client = PsychoPass(
        the_config.sibyl_token,
        host=the_config.sibyl_url,
    )
    
    info = sibyl_client.get_info(1341091260)
    if not info:
        pytest.fail('get_info returned an invalid object.')
        return
