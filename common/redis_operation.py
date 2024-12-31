# @Version：
# @Time：2024/12/31 8:14
# @Author：ChuliLin
# @Description：

import  redis
from common.yaml_config import GetConf
class RedisOperation:
    def __init__(self):
        redis_info=GetConf().get_redis()
        self.redis_client=redis.Redis(
            host=redis_info['host'],
            port=redis_info['port'],
            db=redis_info['db'],
            decode_responses=True,
            charset="utf-8",
            encoding="utf-8"
            # 若 redis 设置了用户名密码，则：
            # password=user:password
        )
if __name__ == '__main__':
    print(RedisOperation().redis_client.get("lcl"))