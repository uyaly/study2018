# coding:utf-8
import unittest
import os
import utils.HTMLTestRunner
# import HTMLTestRunner
# ascii编码报错问题加上以下三行
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 用例路径
case_path = os.path.join(os.getcwd(), "case")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
# html报告文件
report_abspath = os.path.join(report_path, "result.html")

discover = unittest.defaultTestLoader.discover(case_path,
                                                pattern="test*.py",
                                                top_level_dir=None)


fp = open(report_abspath, "wb")
runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                       title=u'接口自动化测试报告',
                                       description=u'用例执行情况：')

# 调用add_case函数返回值
runner.run(discover)
fp.close()
