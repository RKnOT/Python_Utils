import numpy as np
from datetime import datetime
from calendar import monthrange


#import sys
#print(sys.path[0])


class helpers_date_utils():
	def __init__(self):
		self.monat_name_list = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember']
		self.month_name_list = []
		self.get_month_names()
		pass

#------------------------
	def get_month_list(self):
		def wrapper(arg):
			a1 = '_' + "{:02d}".format(arg) + '_'
			return(a1)
		
		month_list = np.arange(12)
		m_list = []
		for i in month_list:
			m_list.append(wrapper(i+1))
		#print(m_list)
		#m_list = ['_01_', '_02_', '_03_', '_04_','_05_', '_06_', '_07_', '_08_', '_09_', '_10_', '_11_', '_12_'] 	
		#print(m_list)
		return m_list
	#------------------------
	def get_month_names(self):
		list_month = np.arange(12)
		for i in list_month:
			month_num = str(i+1)
			#provide month number
			datetime_object = datetime.strptime(month_num, "%m")
			self.month_name_list.append(datetime_object.strftime("%B"))
					
	#------------------------
	def compare_date_now_and_recorted(self, dt_recorted, flag_debug = False):
		flag_same_date = False
		dt_rc = helpers_date_handling(dt_recorted)
		dt_now = helpers_date_handling()	
		time_dic = dt_rc.date_time_differenz(dt_rc, dt_now)
		if time_dic['same_year_month_day_flag']:
			flag_same_date = True 
		# Debug
		if flag_debug:
			print(dt_rc.datum_dic['date_date'])
			print(dt_now.datum_dic['date_date'])
			print(time_dic['same_date_flag']) #== False:
		#---
		return flag_same_date

#------------------------------------
class helpers_date_handling():
	def __init__(self, date_time_str = '', debug_flag = False):
		'''
-- helpers_date_handling class --		
Doc Aufruf: 
	print(helpers_date_handling.__init__.__doc__)
date_time_str format -> '2021_12_22 12:44:22' oder '2021_12_22'
Dictionary with the following current date keyes:
	dict_keys(['year_str', 'year_int', 'month_str', 'month_int', 'day_str', 'day_int', 'date_str', 'date_date', 'date_time_str', 'date_time'])
len(datum_dic.keys()) == 1 -> falsches datum -> !! keine datum info !! 

add days:
	t1 = self.datum_dic['current_date_datetime']
	t2 = t1 + datetime.timedelta(days=2)
	print(t2)
		
		'''
		self.datum_dic = {}
		date_time_format = '%Y_%m_%d %H:%M:%S'
		date_format = date_time_format[0:8]
		self.datum_dic['Status_Flag'] = True
		if date_time_str == '':
			now = datetime.now()
		else:
			indexes = [4,7,10,13,16]
			chars = ['_', '_', ' ', ':', ':']
			if len(date_time_str) == 10:
				indexes = indexes[:2]
				chars = chars[:2]
			elif len(date_time_str) != 19:
				self.datum_dic['Status_Flag'] = False
				return 
			for ind, char in zip(indexes, chars):
				date_time_str = date_time_str[:ind] + char + date_time_str[ind+1:]
			
			#print(date_time_str)
			
			try:
				now = datetime.strptime(date_time_str, date_time_format)
			except: 
				try:
					#print('----', date_time_str, date_format)
					now = datetime.strptime(date_time_str, date_format).date()
				except: 
					self.datum_dic['Status_Flag'] = False
					return 
		
		self.datum_dic['year_str'] = now.strftime('%Y')
		self.datum_dic['year_int'] = int(self.datum_dic['year_str'])
		self.datum_dic['month_str'] = now.strftime('%m')
		self.datum_dic['month_int'] = int(self.datum_dic['month_str'])
		self.datum_dic['day_str'] = (now.strftime('%d'))
		self.datum_dic['day_int'] = int(self.datum_dic['day_str'])
		self.datum_dic['days_in_month_int'] = monthrange(self.datum_dic['year_int'], self.datum_dic['month_int'])[1]
		self.datum_dic['days_in_month_str'] = str(self.datum_dic['days_in_month_int'])
		self.datum_dic['date_str'] = self.datum_dic['year_str'] + '_' + self.datum_dic['month_str'] + '_' + self.datum_dic['day_str']
		self.datum_dic['date_date'] = datetime.strptime(self.datum_dic['date_str'], date_format).date()
		self.datum_dic['date_time_str'] = now.strftime(date_time_format)
		self.datum_dic['date_time'] = datetime.strptime(self.datum_dic['date_time_str'], date_time_format)
		#if debug_flag: self.debug(self)
		
	def date_time_differenz(self, t1, t2):
		diff_dic = {}
		diff_dic['Status_Flag'] = True
		same_date_flag = False
		same_year_flag = False
		same_year_month_flag = False
		same_year_month_day_flag = False
		#print(len(t1.datum_dic), len(t2.datum_dic))
		
		if len(t1.datum_dic) == 1:
			diff_dic['Status_Flag'] = t1.datum_dic['Status_Flag']
			return diff_dic
		if len(t2.datum_dic) == 1:
			diff_dic['Status_Flag'] = t2.datum_dic['Status_Flag']
			return diff_dic
		
		if t1.datum_dic['date_time'] < t2.datum_dic['date_time']:
			#print('t1 kleiner')
			diff_dic['time_delta'] = t2.datum_dic['date_time'] - t1.datum_dic['date_time']
		if t1.datum_dic['date_time'] > t2.datum_dic['date_time']:
			diff_dic['time_delta'] = t1.datum_dic['date_time'] - t2.datum_dic['date_time']
			#print('t1 größer')
			
		if t1.datum_dic['date_date'] == t2.datum_dic['date_date']:
			same_date_flag = True
		#print(t1.datum_dic['date_date'].year, t2.datum_dic['date_date'].year)
		if t1.datum_dic['date_date'].year == t2.datum_dic['date_date'].year:
			same_year_flag = True
			if(t1.datum_dic['date_date'].month == t2.datum_dic['date_date'].month):
				same_year_month_flag = True
				if(t1.datum_dic['date_date'].day == t2.datum_dic['date_date'].day):
					same_year_month_day_flag = True
		diff_dic['t1'] = t1.datum_dic['date_time_str']
		diff_dic['t2'] = t2.datum_dic['date_time_str']
		#diff_dic['time_delta'] = t1.datum_dic['date_time'] - t2.datum_dic['date_time']
		diff_dic['same_date_flag'] = same_date_flag
		diff_dic['same_year_flag'] = same_year_flag
		diff_dic['same_year_month_flag'] = same_year_month_flag
		diff_dic['same_year_month_day_flag'] = same_year_month_day_flag
		return diff_dic
	
	def debug(self, hp):
		print(len(self.datum_dic.keys()))
		print()
		print(self.datum_dic.keys())
		print()
		print(self.datum_dic)
		print('end debug_date_handling')
		print()
		
	
		
#--- debug helpers_date_handling ----------
'''
test_date = '2021_12_22'
test_date = '2021_12_22 23:12:00'
hp1 = helpers_date_handling(test_date, debug_flag = True)
hp2 = helpers_date_handling(debug_flag = True)
diff = hp1.date_time_differenz(hp2 , hp1)
print(diff)


dbf = False
test_date1 = '2021 12,23 00:00:04'
test_date2 = '2021_02_23 00:00:03'
test1 = '2021_12_23'

print(f'{"-"*40}')

hp1 = helpers_date_handling(test1, debug_flag = dbf)
hp2 = helpers_date_handling(test_date2, debug_flag = dbf)
diff = hp1.date_time_differenz(hp1 , hp2)
print(diff)

'''

#___________________________________________
