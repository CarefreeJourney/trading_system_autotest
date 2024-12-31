# @Version：
# @Time：2024/12/21 0:48
# @Author：ChuliLin
# @Description：
import random
import pytest
class TestRerun:
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    def test_rerun(self):
        num=random.randint(1,3)
        print("num:",num)
        if num!=1:
            print("失败")
            raise Exception("出错了")
        else:
            print("成功")
        assert "william" not in "william UI"
