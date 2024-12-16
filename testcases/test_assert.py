# @Version：
# @Time：2024/12/16 23:51
# @Author：ChuliLin
# @Description：

class TestAssert:
    def test_assert(self):
        # == != < > >= <=
        assert "lcl"=="lcl"
        assert "lclA"!="lclB"
        assert 0<1
        assert 2>1
        assert 0<=1
        assert 2>=1
        # 包含 in，不包含 not in
        assert "william" in "william UI"
        assert "william" not in "UI"
        # 使用 True 或 False
        assert 1
        assert (9>8) is True
        assert not False
