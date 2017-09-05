# coding:utf-8
#  导入日志模块
import logging

# 创建要记录的日志级别的记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.info())

# 创建日志处理程序
handler_warn = logging.FileHandler('warning_log.text')
handler_warn.setLevel(logging.WARNING)

# 日志处理程序创建事物
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
