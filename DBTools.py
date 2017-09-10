# -*- coding: utf-8 -*-
"""
Dec: Tools for DB
Created on : 2017.09.08
Author : Iflier
"""
print(__doc__)

from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)

# 获取连接到的server的信息
serverInfo = client.server_info()
print("连接到的server的信息：{0}".format(serverInfo))

# 该server允许的最大连接数
maxPoolSize = client.max_pool_size
print("该server允许的最大连接数为：{0:>+3,d}".format(maxPoolSize))

# 获取该server中的所有的数据库的名字
allTheDatabasesName = client.database_names()
print("该server一共存在 {0:>+2,d} 个Database(s)：{1}".format(len(allTheDatabasesName),
      allTheDatabasesName))

# 获取一个来自于该server的一个已经存在的集合
db = client.get_database("insertmany")
# 或者
# db = client.queryEmbededArr


# 查看使用的数据库中包含的集合（collection）
collectionsName = db.collection_names(include_system_collections=True)
print("数据库 {0} 中包含 {1:>+2,d} 个集合：{2}".format(db.name, len(collectionsName),
      collectionsName))

# 在使用的数据库中，创建一个新的集合：money
db.create_collection("money")

# 从数据库中删除一个集合（collection）
# dropCollectionResult = db.drop_collection("happy")
# 该操作返回一个字典，即使删除不存在的集合，也不会引发异常
# print("dropCollectionResult: {0}".format(dropCollectionResult))

# *************************************************************
# 删除掉一个数据库
# client.drop_database(db)
# 或者
# client.drop_database("queryEmbededArr")
# *************************************************************

# 断开与server的连接
client.close()
