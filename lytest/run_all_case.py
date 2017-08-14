# coding:utf-8
import unittest
import os
# 用例路径
case_path = os.path.join(os.getcwd(), "case")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
def all_case():
    # 三个参数：-case_dir:这个是待执行用例的目录。
    # -pattern：这个是匹配脚本名称的规则，test*.py意思是匹配test开头的所有脚本。
    # -top_level_dir：这个是顶层目录的名称，一般默认等于None就行了。
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="test*.py",
                                                   top_level_dir=None)
    print(discover)
    return discover
if __name__ == "__main__":
    # discover加载到的用例是一个list集合，需要重新写入到一个list对象testcase里
    # 这样就可以用unittest里面的TextTestRunner这里类的run方法去执行
    runner = unittest.TextTestRunner()
    runner.run(all_case())