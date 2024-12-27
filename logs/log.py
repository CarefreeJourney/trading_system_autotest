# @Version：
# @Time：2024/12/26 16:51
# @Author：ChuliLin
# @Description：

import logging
import os
import time
from common.tools import get_project_path,sep

def get_log(logger_name):
    # 创建一个 logger，名称
    logger = logging.getLogger(logger_name)
    # 设置级别
    logger.setLevel(logging.INFO)

    # 存日志：存放位置+文件名称
    # 获取本地时间
    rq = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
    # 设置日志存放路径
    all_log_path = get_project_path()+sep(["logs","all_logs"],add_sep_before=True,add_sep_after=True)
    # 如果日志目录不存在，就自动创建
    if not os.path.exists(all_log_path):
        os.makedirs(all_log_path)
    # 设置日志文件名
    all_log_name = all_log_path+rq+".log"

    # 创建 handler
    # 创建一个 handler 写入日志
    fh = logging.FileHandler(all_log_name)
    fh.setLevel(logging.INFO) # 写入日志文件的日志级别，从 ERROR 及以上开始

    # 定义日志输出格式
    all_log_formatter = logging.Formatter("%(asctime)s - "
                                          "%(filename)s - "
                                          "%(module)s - "
                                          "%(funcName)s - "
                                          "%(lineno)d - "
                                          "%(levelname)s -"
                                          "%(message)s",
                                          datefmt="%Y-%m-%d %H:%M:%S")
    # 将定义好 的 输出形式添加到 handler
    fh.setFormatter(all_log_formatter)
    # 给 logger 添加 handler
    logger.addHandler(fh)
    return logger

log = get_log("自动化测试")
