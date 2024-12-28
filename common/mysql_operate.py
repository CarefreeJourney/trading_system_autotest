# @Version：
# @Time：2024/12/27 22:30
# @Author：ChuliLin
# @Description：

import pymysql
from common.yaml_config import GetConf

class MysqlOperate:
    def __init__(self):
        mysql_config = GetConf().get_mysql_config()
        # 连接 mysql
        self.host = mysql_config['host']
        self.port = mysql_config['port']
        self.user = mysql_config['user']
        self.password = mysql_config['password']
        self.db = mysql_config['db']
        self.conn = None
        self.cur = None

    def __conn_db(self):
        try:
            self.conn = pymysql.connect(host=self.host, user=self.user
                                        , password=self.password,
                                        db=self.db, port=self.port,
                                        charset='utf8')
        except Exception as e:
            print(e)
            return False

        self.cur = self.conn.cursor()
        return True

    def __close_conn(self):
        self.cur.close()
        self.conn.close()
        return True

    def __commit(self):
        self.conn.commit()
        return True

    def query(self, sql):
        """
        根据 sql 语句进行查询并返回结果
        :param sql:
        :return:
        """
        self.__conn_db()
        self.cur.execute(sql)
        query_data = self.cur.fetchall()
        # 通过 pymysql 执行后返回的结果都是元组的形式
        if query_data == ():
            query_data = None
            print("没有获取到数据，表为空")
        else:
            pass
        self.__close_conn()
        return query_data

    def insert_update_table(self, sql):
        self.__conn_db()
        self.cur.execute(sql)
        self.__commit()  # 有修改记得 commit
        self.__close_conn()


if __name__ == '__main__':
    # 查询校园二手交易系统的用户表,结果是元组
    result = MysqlOperate().query("select * from user;")
    print(result[0][1])
    sql = ("INSERT INTO `product`"
    "(`product_id`, `product_title`, `product_stock`, "
    "`product_price`, `product_desc`, `product_cover_img`, "
    "`product_detail_img`, `product_status`, `create_time`, "
    "`update_time`, `publish_user_id`) VALUES "
    "(33, '自用篮球，没打过几次，便宜出', 1, 99.00, '自用篮球，没打过几次，便宜出', "
    "'http://47.101.216.239:9090/product/product_img/16891321223286eb32b0c-09bd-4353-a047-0751ec2309dd',"
    "'http://47.101.216.239:9090/product/product_img/168913213426804dce806-e86f-4062-8916-131387092c00',"
    " 1, '2023-07-12 11:22:30', '2023-07-12 11:22:30', 12);")
    MysqlOperate().insert_update_table(sql)
