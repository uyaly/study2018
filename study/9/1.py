# coding:utf-8
#  导入日志模块
import log1

# 创建要记录的日志级别的记录器
logger = log1.getLogger(__name__)
logger.setLevel(log1.info())

# 创建日志处理程序
handler_warn = log1.FileHandler('warning_log.text')
handler_warn.setLevel(log1.WARNING)

# 日志处理程序创建事物
formatter = log1.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
