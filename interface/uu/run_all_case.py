# coding:utf-8
import os
import unittest

from study.interface.uu.utils import HTMLTestRunner


def all_case():
    # 待执行用例的目录

    # 用例路径
    case_path = os.path.join(os.getcwd(), "case")
    # 报告存放路径
    report_path = os.path.join(os.getcwd(), "report")
    # html报告文件
    report_abspath = os.path.join(report_path, "result.html")
    testcase = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="test*.py",
                                                    top_level_dir=None)
    testcase.addTests(discover) # 直接加载discover
    # print(testcase)
    # return testcase
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')

if __name__ == "__main__":
    # 返回实例
    runner = unittest.TextTestRunner()
    # run 所有用例
    runner.run(all_case())