import pymysql


cnx = pymysql.connect(host='129.31.228.132', port=3306, user='root', passwd='', db='TEA')

insert_query = ("INSERT INTO `TEA`. `teaTable` (`tea_id`, `name_of_tea`, `device_id`, `broad_lux`, `ir_lux`, `temperature`) VALUES ('2', 'test', '1', '1', '1', '1');")

cursor = cnx.cursor()
cursor.execute(insert_query)

cnx.commit()
cursor.close()
cnx.close()
