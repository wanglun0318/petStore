# coding=utf-8
import pymysql
from com.petstore.dao.base_dao import BaseDao
"""订单明细管理DAO"""


class OrderDetailDao(BaseDao):
    def __init__(self):
        super().__init__()

    def create(self, orderdetail):
        """创建订单明细，插入到数据库"""
        try:
            with self.conn.cursor() as cursor:
                sql = 'insert into orderdetails (orderid, productid,quantity,unitcost) ' \
                      'values (%s,%s,%s,%s)'
                affectedcount = cursor.execute(sql, orderdetail)
                print('成功插入{0}条数据'.format(affectedcount))
                # 提交数据库事务
                self.conn.commit()
        except pymysql.DatabaseError as e:
            # 回滚数据库事务
            self.conn.rollback()
            print(e)
        finally:
            self.close()

