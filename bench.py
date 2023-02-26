import uuid

import pytest
import timeflake
from cuid2 import CUID
from cyksuid.v2 import ksuid as cy_ksuid
from cyksuid.v2 import parse as cy_parse
from ksuid import Ksuid as SvixKsuid
from snowflake import Snowflake, SnowflakeGenerator
from ulid import ULID as python_ulid

snowflake_gen = SnowflakeGenerator(42)

@pytest.mark.parametrize(
    "gen",
    [
        pytest.param(uuid.uuid4, id="uuid4"),
        pytest.param(SvixKsuid, id="svix"),
        pytest.param(cy_ksuid, id="cyksuid"),
        pytest.param(python_ulid, id="python-ulid"),
        pytest.param(snowflake_gen.__next__, id="snowflake"),
        pytest.param(CUID().generate, id="cuid2"),
        pytest.param(timeflake.random, id="timeflake"),
    ],
)
def test_generate(benchmark, gen):
    benchmark(gen)

@pytest.mark.parametrize(
    "parse,val",
    [
        pytest.param(SvixKsuid.from_base62, "Afwp2wWXH1RpvLDMXQkmZtUlWzr", id="svix"),
        pytest.param(cy_parse, "Afwp2wWXH1RpvLDMXQkmZtUlWzr", id="cyksuid"),
        pytest.param(uuid.UUID, "03e36797-f3c1-47ac-ba34-9daccece7e30", id='uuid4'),
        pytest.param(Snowflake.parse, 7035582051483033600, id="snowflake"),
        pytest.param(lambda x: timeflake.parse(from_base62=x), "0002HCZffkHWhKPVdXxs0YH", id="timeflake")
    ],
)
def test_parse(benchmark, parse, val):
    benchmark(parse, val)