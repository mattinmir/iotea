import pymysql


class database:

	def __init__:
		self.conn = pymysql.connect(host='129.31.226.212', port=3306, user='root', passwd='', db='TEA', cursorclass=pymysql.cursors.DictCursor)
		self.cursor = conn.cursor()
		

	def insert(self, tea_id, name_of_tea, devide_id, broad_lux, ir_lux, temperature)

	def next_tea_id(self):
		return cursor.execute('SELECT MAX(tea_id) FROM teaTable')
	
	def query(q):
		
		cursor.execute(q)
		return cur


