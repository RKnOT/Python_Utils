import numpy as np
import json
from datetime import datetime
import sys
import os

fpath = '/private/var/mobile/Containers/Shared/AppGroup/FA16265D-A93E-42FB-9932-E3CC306D50A8/File Provider Storage/Repositories/Python_Utils/Date_Time_Utils'
sys.path.append(fpath)


fpath = '/private/var/mobile/Containers/Shared/AppGroup/FA16265D-A93E-42FB-9932-E3CC306D50A8/File Provider Storage/Repositories/PV_Auswertung_2021_10/CommonClasses'
sys.path.append(fpath)

import date_time_util as dtu
import UtilsClasses as ut
import DataModel as d_m


class helpers(dtu.helpers_date_handling):
	
	def __init__(self):
			super().__init__()
	'---------------'
	def gen_empty_year_month_yield(self): 
		year_month_empty_dic = {}
		for i in range(1, 13):
			m = f'{i:02d}'
			year_month_empty_dic[m] = 0.0
		return year_month_empty_dic
	'--------------'
	def gen_years_yield_empty(self, start_year = 2012):
		years_empty_dic = {}
		now = datetime.now()
		current_year = int(now.strftime("%Y"))
		current_year = current_year			
		year_count = current_year - start_year
		for i in range(2012, current_year):
			years_empty_dic[str(i)] = 0
		return years_empty_dic
	'----------------'	
	def years_yield_abgerechnet_dic(self):
		 year_yield_abgerechnet_dic = {'2012': 431.0, '2013': 7325.0, '2014': 7878.0, '2015': 7733.0, '2016': 7729.0, '2017': 7797.0, '2018': 7972.0, '2019': 7644.0, '2020': 7301.0, '2021': 6705.0, '2022': 0.0}
		 return year_yield_abgerechnet_dic
	'----------------'
	def years_month_yield(self, years_month_yield):
		years_yield_dic = self.gen_years_yield_empty()
		#print(years_month_yield)
		for k in list(years_month_yield.keys()):
			#print(k)
			#print(years_month_yield_dic[k])
			year_yield = 0.0
			for k1 in years_month_yield[k]:
				#print(k1)
				#print(type(years_month_yield_dic[k][k1]), type(years_month_yield_dic[k][k1]) is dict)
				month_yield_format = "{:8.3f}".format(years_month_yield[k][k1])
				#print("year {}: | month : {} | yield : {}".format(k, k1, month_yield_format))
				year_yield += years_month_yield[k][k1]
			years_yield_dic[k] = year_yield 
		#print('----')	
		#print(years_yield_dic)
		return years_yield_dic
	'---------------'
	def convert_to_bar_plot_lists(self, *args):
		plot_lists = {}
		x = list(args[0].keys())
		X = np.arange(len(x))
		y_n = []
		for item in args:
			y = list(item.values())
			y_n.append(y)
		plot_lists['x_bezeichnung'] = x
		plot_lists['x_werte'] = X
		plot_lists['y_werte_liste'] = y_n
		#print(plot_lists)
		#print('--')
		return plot_lists
	
	'------'
	def writeJsonFile(self, dest_file_name, file_content):
		with open(dest_file_name, 'w') as outfile:
			json.dump(file_content, outfile)
			pass
	
	def readJsonFile(self, dest_file_name):
		#print(dest_file_name)
		if os.path.exists(dest_file_name):
			with open(dest_file_name) as json_file:
				data = json.load(json_file)
		else: 
			data = {}	
		return data
		
#------------------------------------
class Aggregate_Years_CSV():
	def __init__(self):
		'''
dict_keys(['last_recorded_date', 'years_month_yield_data', 'years_yield_data_aufgezeichnet', 'years_yield_data_abgerechnet'])
		'''
		
		self.helpers = helpers()
		self.nwd = ut.NetworkData()
		self.nwd.iniData()
		
		self.last_entry_dic = {}
		dir_aggr = 'Aggregation/'
		self.dir_file_dic = {}
		
		#-------------- check year dir exists locally------
		dest = os.path.join(self.nwd.dir_local_CSV, dir_aggr)
		#print(dest)
		if os.path.isdir(dest) == False:
			os.mkdir(dest)
		#---------------------------------------------------
		
		self.dir_file_dic['last_recorded_date'] = dest + 'last_recorded_date.json'
		self.dir_file_dic['years_month_yield_data'] = dest + 'years_month_yield_data.json'
		self.dir_file_dic['years_yield_data_aufgezeichnet'] = dest + 'years_yield_data_aufgezeichnet.json'
		self.dir_file_dic['years_yield_data_abgerechnet'] = dest + 'years_yield_data_abgerechnet.json'
		'---------------'
	def check_dirs_exists(self):
		year_file_names = {}
		year_month_names = {}
		list_temp = []
		key_years = list(self.dic_y_m_d.keys())
		for key_year in key_years[0:-1]: # without aggregation dir
			list_temp.append(key_year + '.json')
			month = list(self.dic_y_m_d[key_year].keys())
			list_month = []
			for key_month in month:
				list_month.append(key_year +'_'+ key_month+ '.json""')
			year_month_names[key_year] = list_month
		year_file_names['Years'] = list_temp		
				
		print((year_file_names['Years']))
		print(year_month_names)		
		
		for item in year_file_names['Years']:
			dest = self.dest + item
			#print(dest)
			# Writing to sample.json
			#self.writeJsonFile(dest, dictionary)
			#break		
		pass
	
	def aggregate_yield(self, years_selected = ['']):  
		
		I_get_csv_file_names = ut.Get_CSV_File_Names_from_Dir(years_selected)
		self.dic_y_m_d = I_get_csv_file_names.years_month_days_dic
		
		'''
		print('----')
		print(self.dic_y_m_d)
		print('----')
		'''
		month_monthYield_dic = {}
		#TagRecord = d_m.TagUtil()
		dm = d_m.TagUtil()
		list_day_yield_pro_month = []
		years_month_yields = {}
		key_years = list(self.dic_y_m_d.keys())
		#print(key_years)
		
		year_month_yield_dic = {}
		month_1_12 = self.helpers.gen_empty_year_month_yield()
		#print(month_1_12)
		for key_year in key_years:
			# debug
			#if key_year == '2014': break
			#------------
			print(key_year)
			month = list(self.dic_y_m_d[key_year].keys())
			for key_month in month:
				
				month_yield = 0.0
				dic_month = {}
		
				list_days_in_month = []
					
				days_in_month = self.dic_y_m_d[key_year][key_month]
				for i3 in days_in_month:
					file_name = key_year +'_'+ key_month +'_'+ i3
					gcsvN = d_m.GetCSV_File_Names(self.nwd.dir_local_CSV, file_name)
					list_days_in_month.append(key_year +'_'+ key_month + '_'+ i3 + '.CSV')
				dic_month[gcsvN.path] = list_days_in_month
				#print(dic_month)
				dm = d_m.TagUtil()
				A, monthYield = dm.getAllLastTelegrams(dic_month)
				
				month_1_12[key_month] = monthYield 
			#print('---')
			year_month_yield_dic[key_year] = month_1_12
			month_1_12 = self.helpers.gen_empty_year_month_yield()
		#print(month_1_12)
		#print(year_month_yield_dic)
		return year_month_yield_dic
		
#------------------------------------	
class Get_years_month_average():
	def __init__(self):
		agr = Aggregate_Years_CSV()
		hp = helpers()	
		self.y_m_av_dic = {}
		self.ym = hp.readJsonFile(agr.dir_file_dic['years_month_yield_data'])
		self.calc_averages()
	
	def calc_averages(self):
		
		for y, v in self.ym.items():
			m_av_dic = {}
			#print(y)
			#print(v)
			for m, w in v.items():
				date_str = y + '_' + m + '_'+ '01'
				#print(y, m, w)
				d1 = dtu.helpers_date_handling(date_str)
				dpm = d1.datum_dic['days_in_month_int']
				av = w / dpm
				m_av_dic[m] = [w, av]
				#print(y, m, w, dpm, av)
			self.y_m_av_dic[y] = m_av_dic
		#print(self.y_m_av_dic)
#------------------------------------
# debug
#hp = helpers()
#print(hp.datum_dic)

