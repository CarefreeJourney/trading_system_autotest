# @Version：
# @Time：2024/12/21 10:25
# @Author：ChuliLin
# @Description：
import pytest
from pytest_assume.plugin import assume
class TestAssert:
    def test_assert(self):
        with assume: assert "william" in "UI autotest"
        pytest.assume(1+1==3)
        assert 1+1==2
        print("over?")