import os

import pytest


class TestCal:
    # 测试加法
    @pytest.mark.run(order=1)
    def test_add(self, create_cal, get_adddatas):
        result = create_cal.add(get_adddatas[0], get_adddatas[1])
        assert result == get_adddatas[2]

    # 测试除法
    @pytest.mark.run(order=4)
    def test_div(self, create_cal, get_divdatas):
        try:
            result = create_cal.div(get_divdatas[0], get_divdatas[1])
            assert result == get_divdatas[2]
        except ZeroDivisionError:
            print("0不能作为被除数")

    # 测试减法
    @pytest.mark.run(order=2)
    def test_sub(self, create_cal, get_subdatas):
        result = create_cal.sub(get_subdatas[0], get_subdatas[1])
        assert result == get_subdatas[2]

    # 测试乘法法
    @pytest.mark.run(order=3)
    def test_mul(self, create_cal, get_muldatas):
        result = create_cal.mul(get_muldatas[0], get_muldatas[1])
        assert result == get_muldatas[2]


# if __name__ == '__main__':
#     pytest.main(['--alluredir', '../Report', 'test_calculator.py ', '-vs'])  # 生成报表数据
#     split = 'allure ' + 'generate ' + '../Report ' + '-o ' + '../Html ' + '--clean'  # 生成Html报告语句
#     os.system(split)
