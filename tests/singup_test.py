import re
import pytest

from api.signup import signup
from api.json_keys import JsonKeys as k
from patterns.patterns import Pattern


# @pytest.mark.parametrize()  # Сюда передавать body + набор значений для assert X раз.
def test_is_signup_test_working(successful_signup):
    r, d = signup(successful_signup)
    print(r)
    print(d)
    assert r.status_code == 201  # Использовать переменные при parametrize во всех assert.
    assert re.match(Pattern.redirect, d[k.redirect])
    assert re.match(Pattern.login_url, d[k.login_url])
    assert re.match(Pattern.token, d[k.token])
    assert r.elapsed.total_seconds() < 15  # За 10 сек не всегда успевает ¯\_(ツ)_/¯.

