# -*- coding: utf-8 -*-
"""
Dec: 检索server中的所有的数据库和数据库中包含的集合以及各个集合包含的内容
Created on : 2017.09.08
Author : Iflier
"""
print(__doc__)

from pymongo import MongoClient

client = MongoClient(host="localhost", port=27017)

# 获取连接到的server的信息
# serverInfo = client.server_info()
# print("Server Info: {0}".format(serverInfo))
print('\n')

print("*******"*10)
# 以列表的形式返回server端存在的所有的数据库名称
allDatabasesName = client.database_names()
print("当前server共存在 {0:>+2,d} 个数据库：{1}".format(len(allDatabasesName), allDatabasesName))

for database in allDatabasesName:
    if database == "local":
        pass
    else:
        db = client.get_database(database)
        # 返回该db中包含的所有集合的名称
        collectionsName = db.collection_names(include_system_collections=False)
        print("-------"*10)
        print("数据库 {0} ，包含 {1:>+2,d} 个集合：{2}".format(db.name, len(collectionsName), collectionsName))
        for collection in collectionsName:
            print("集合 {0} ，包含的文档：".format(collection))
            docs = client[database][collection].find({}, projection={"_id": False})
            for doc in docs:
                print(doc)
