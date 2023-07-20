
from mysql.connector import pooling

poolName='MysqlPool'
poolsize=10
dbconfig = {'host':'192.168.1.74',
            'database':'futsaldb',
            'user':'ashna',
            'password':'ashna',
  "port":3306
}

#connPool=pooling.MySQLConnectionPool(pool_name=poolName,pool_size=poolsize,pool_reset_session=True,**dbconfig)
# conn= connPool.get_connection()
myConnectionPool=False
def conn():
  global myConnectionPool
  try:
    if myConnectionPool==False:
      myConnectionPool=pooling.MySQLConnectionPool(pool_name=poolName,pool_size=poolsize,pool_reset_session=True,**dbconfig)
    return myConnectionPool.get_connection()
  except Exception as e:
      raise e