设计数据库总结：
考点：entity, relationship
relationship是一行一行的，而不是a->[b,c,d]这样的，单独一行scalable,容易SQL操作
每一个table里面至少有的col: create_time, update_time, modify_by
有可能需要的表： loggin table(日志table)，有的公司放在mySQL table. 有点放在kafka
例子： 一个user upload photo，有很多friend

User
id(mySQL自动生成，自增的) name country(来自enum表) created_time updated_time


Photos
id(同上)  owner URL(因为图片太大，会有硬盘存，fileHostingService)

Relationship
id user_a user_b created_time

Sharing

id p_id user_id

尽量不要有冗余信息

具体的SQL复习请看这里：
http://www.runoob.com/sql/sql-groupby.html




