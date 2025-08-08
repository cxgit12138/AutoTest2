#实现日志记录功能，
# 创建全局日志对象，支持控制台和文件双重日志输出
import logging
import os
from datetime import datetime

class Logger:
    def __init__(self, log_level='INFO'):
        # 创建logger对象
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(log_level)

        # 避免日志重复输出
        if not self.logger.handlers:
            # 创建控制台处理器
            console_handler = logging.StreamHandler()
            console_handler.setLevel(log_level)

            # 创建文件处理器
            # 修改: 使用相对路径而不是绝对路径
            log_dir = './logs'
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            log_file = os.path.join(log_dir, f'{datetime.now().strftime("%Y-%m-%d")}.log')
            file_handler = logging.FileHandler(log_file, encoding='utf-8')
            file_handler.setLevel(log_level)

            # 定义日志格式
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            file_handler.setFormatter(formatter)

            # 添加处理器到logger
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def get_logger(self):
        return self.logger

# 创建全局日志对象
logger = Logger().get_logger()