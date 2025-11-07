import logging
import os
from datetime import datetime


def get_logger(name: str = __name__):
    """
    创建并返回一个配置好的logger实例
    """
    # 创建logger对象
    logger = logging.getLogger(name)
    
    # 设置日志级别
    logger.setLevel(logging.INFO)
    
    # 避免重复添加处理器
    if not logger.handlers:
        # 创建控制台处理器
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # 创建文件处理器
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'log')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        log_file = os.path.join(log_dir, 'test.log')
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        
        # 创建格式器
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s [函数:%(funcName)s] [line:%(lineno)d] %(levelname)s --%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        # 为处理器添加格式器
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        # 将处理器添加到logger对象
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
    
    return logger