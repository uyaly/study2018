# coding:utf-8
# 导入日志模块
import logging

# 创建要记录的日志级别的记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# 创建日志处理程序
handler_info = logging.FileHandler('info_log.txt')
handler_info.setLevel(logging.INFO)
# 日志的格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler_info.setFormatter(formatter)
# 将日志处理程序记录到记录器
logger.addHandler(handler_info)

def age():
    logger.info('Inside funtion age()')

    try:
        logger.info('In the try Block')
        age = int(input("请输入你当前年龄"))
        logger.debug('Value of age is %s'%age)

    except ValueError as e:
        logger.critical('Invalid Input',exc_info=True)

if __name__=="__main__":
    age()
