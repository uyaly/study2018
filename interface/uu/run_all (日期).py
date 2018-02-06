# coding:utf-8
import unittest
import HTMLTestRunner
import os
import time

# python2加这三行
import sys
reload(sys)
sys.setdefaultencoding('utf8')
def all_case(case="case"):
    '''加载指定目录下的所有的用例'''

    case_dir = os.path.join(os.getcwd(), case)

    discover = unittest.defaultTestLoader.discover(case_dir,
                                                   pattern="test*.py",
                                                   top_level_dir=None)

    print(discover)
    return discover

if __name__ == "__main__":
    # 报告的路径
    nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
    print(nowtime)
    report_path = os.path.join(os.getcwd(), "report", nowtime+".html")
    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='测试模板',description='用例执行情况')
    runner.run(all_case())
    fp.close()
