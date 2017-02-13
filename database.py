import pymysql


class database:

	def __init__(self, _host, _port, _user, _passwd, _db):
		self.conn = pymysql.connect(host=_host, port=_port, user=_user, passwd=_passwd, db=_db)
		self.cursor = conn.cursor()
		

	def insert(self, time, tea_id, name_of_tea, type_of_tea, device_id, broad_lux, ir_lux, temperature):
		values = "({}, {}, {}, {}, {}, {}, {}, {});".format(time, tea_id, name_of_tea, type_of_tea, device_id, broad_lux, ir_lux, temperature)
		cursor.execute("INSERT INTO `TEA`. `teaTable` (`time`, `tea_id`, `name_of_tea`, `type_of_tea`, `device_id`, `broad_lux`, `ir_lux`, `temperature`) VALUES" + values)

	def next_tea_id(self):
		cursor.execute("SELECT MAX(tea_id) FROM teaTable")
		return cursor.fetchone()[0] + 1
	
	def query(q):
		cursor.execute(q)
		return cursor.fetchall()


