# coding:utf-8
import unittest
import os
import HTMLTestRunner
# 解决UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 1: ordinal not in range(128)
import sys
reload(sys)
sys.setdefaultencoding('utf8')
# 用例路径
case_path = os.path.join(os.getcwd(), "case")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "report")
def all_case():
    # 三个参数：-case_dir:这个是待执行用例的目录。
    # -pattern：这个是匹配脚本名称的规则，3*.py意思是匹配test开头的所有脚本。
    # -top_level_dir：这个是顶层目录的名称，一般默认等于None就行了。
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern="3*.py",
                                                   top_level_dir=None)
    print(discover)
    return discover
if __name__ == "__main__":
    # discover加载到的用例是一个list集合，需要重新写入到一个list对象testcase里
    # 这样就可以用unittest里面的TextTestRunner这里类的run方法去执行
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())
    # html报告文件路径
    report_abspath = os.path.join(report_path, "result.html")
    fp = open(report_abspath, "wb")
    # 三个参数:--stream:测试报告写入文件的存储区域
    # --title:测试报告的主题
    # --description：测试报告的描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()
