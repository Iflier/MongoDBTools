# MongoDBTools
用于查看MongoDB的内容工具
文件DBTools.py功能包括：
1.查看连接的server的信息，允许的最大连接数
2.该server目前存在的数据库个数及名称
3.查看集体的某一个数据库包含的集合个数以及集合的名字

文件retriceDB.py的功能：
1.检索出该server目前存在的所有的Databases，输出它们的名字和个数
2.检索每一个Database中存在的集合（collection）数目和集合的名字
3.输出每一个集合中保存的文档（projection = {"_id": False}）
