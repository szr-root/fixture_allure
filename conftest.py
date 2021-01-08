import os

import pytest
import yaml

from calculate import Calculator


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


path = os.path.dirname(__file__) + './datas.yml'

with open(path, encoding='utf-8') as f:
    datas = yaml.safe_load(f)
    adddata = datas['datas']['adddatas']
    addids = datas['ids']['addids']

    subdata = datas['datas']['subdatas']
    subids = datas['ids']['subids']

    muldata = datas['datas']['muldatas']
    mulids = datas['ids']['mulids']

    divdata = datas['datas']['divdatas']
    divids = datas['ids']['divids']


@pytest.fixture(scope='module', params=adddata, ids=addids)
def get_adddatas(request):
    print("【开始计算】")
    data = request.param
    print(f"接收的数据是{data}")
    yield data
    print("【结束计算】")

@pytest.fixture(scope='module', params=subdata, ids=subids)
def get_subdatas(request):
    print("【开始计算】")
    data = request.param
    print(f"接收的数据是{data}")
    yield data
    print("【结束计算】")

@pytest.fixture(scope='module', params=muldata, ids=mulids)
def get_muldatas(request):
    print("【开始计算】")
    data = request.param
    print(f"接收的数据是{data}")
    yield data
    print("【结束计算】")

@pytest.fixture(scope='module', params=divdata, ids=divids)
def get_divdatas(request):
    print("【开始计算】")
    data = request.param
    print(f"接收的数据是{data}")
    yield data
    print("【结束计算】")

# 生成一个计算器实例
@pytest.fixture(scope='class')
def create_cal():
    calc = Calculator()
    return calc
