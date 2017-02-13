import pymysql


class database:

	def __init__(self, _host, _port, _user, _passwd, _db):
		self.conn = pymysql.connect(host=_host, port=_port, user=_user, passwd=_passwd, db=_db)
		self.cursor = self.conn.cursor()
		

	def insert(self,  tea_id, name_of_tea, type_of_tea, device_id, broad_lux, ir_lux, temperature):
		values = "({}, {}, {}, {}, {}, {}, {});".format(tea_id, name_of_tea, type_of_tea, device_id, broad_lux, ir_lux, temperature)
		print(values)
		self.cursor.execute("INSERT INTO `TEA`. `teaTable` (`tea_id`,  `name_of_tea`, `type_of_tea`, `device_id`, `broad_lux`, `ir_lux`, `temperature`) VALUES " + values)

	def next_tea_id(self):
		self.cursor.execute("SELECT MAX(tea_id) FROM teaTable")
		return self.cursor.fetchone()[0] + 1
	
	def query(q):
		self.cursor.execute(q)
		return self.cursor.fetchall()


