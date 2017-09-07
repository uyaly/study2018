# coding:utf-8
import test_hpk.utils.log1
from test_hpk.utils.log1.handlers import TimedRotatingFileHandler
from test_hpk.utils.config import LOG_PATH


class Logger(object):
    def __init__(self, logger_name='framework'):
        self.logger = test_hpk.utils.log1.getLogger(logger_name)
        test_hpk.utils.log1.root.setLevel(test_hpk.utils.log1.NOTSET)
        self.log_file_name = 'test.log'
        self.backup_count = 5
        # 日志输出级别
        self.console_output_level = 'WARNING'
        self.file_output_level = 'DEBUG'
        # 日志输出格式
        self.formatter = test_hpk.utils.log1.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        """在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回"""
        if not self.logger.handlers:  # 避免重复日志
            console_handler = test_hpk.utils.log1.StreamHandler()
            console_handler.setFormatter(self.formatter)
            console_handler.setLevel(self.console_output_level)
            self.logger.addHandler(console_handler)

            # 每天重新创建一个日志文件，最多保留backup_count份
            file_handler = TimedRotatingFileHandler(filename=LOG_PATH + self.log_file_name,
                                                    when='D',
                                                    interval=1,
                                                    backupCount=self.backup_count,
                                                    delay=True,
                                                    encoding='utf-8'
                                                    )
            file_handler.setFormatter(self.formatter)
            file_handler.setLevel(self.file_output_level)
            self.logger.addHandler(file_handler)
        return self.logger

logger = Logger().get_logger()