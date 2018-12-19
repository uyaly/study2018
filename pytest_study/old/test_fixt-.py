# coding:utf-8
import pytest
def setup_modle():
    print("setup_modle: 整个.py模块只执行一次")
def teardown_model():
    print("teardown_model: 整个.py模块只执行一次")
def setup_function():
    print("setup_function: 每个用例开始都会执行")
def teardown_function():
    print("teardown_function: 每个用例结束后都会执行")
def test_one():
    print("正在执行------test_one")
    x = "this"
    assert 'h' in x
def test_two():
    print("正在执行------test_tow")
    x = "hello"
    assert hasattr(x, 'check')
def test_three():
    print("正在执行------test_three")
    a = "hello"
    b = "hello world"
    assert a in b
if __name__ == "__main__":
    pytest.main(["-s", "test_fixt-.py"])