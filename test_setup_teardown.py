import pytest
#python中一个模块就是一个文件，setup_module可实现整个模块中只执行一次
def setup_module():
    print("\nsetup module:整个模块中始只执行一次￥￥￥￥")

def teardown_module():
    print("\n￥￥￥￥teardown setup module:整个模块结束只执行一次￥￥￥￥")
#类外测试用例
def setup_function():
    print("\nsetup function:每个不在类中的用例开始前会执行！")
def teardown_fuction():
    print("\nteardown function:每个类中的用例结束后执行！")
def test_one():
    print("\n正在执行测试模块：test one")
def test_two():
    print("\n正在执行测试模块：test two")

class TestCase():
    def setup_class(self):
        print("\n**setup class:class类里面所有用例执行前执行")
    def teardown_class(self):
        print("\n**setup class:class类里面所有用例执行后执行")
    def setup(self):
        print("\nsetup:每个用例开始前都会执行")
    def teardown(self):
        print("\nteardown:每个用例结束执行")
    def test_three(self):
        print("\n正在执行测试模块：test three")
    def test_four(self):
        print("\n正在执行测试模块：test four")