from datetime import datetime

def log_datetime(func):
			'''Log the date and time of a function'''
			
			def wrapper():
				print(f'Function: {func.__name__}\nRun on: {datetime.today().strftime("%Y-%m-%d %H:%M:%S")}')
				print(f'{"-"*30}')
				func()
			return wrapper
		
@log_datetime
def daily_backup():
	print('Daily backup job has finished.')
	print()
		
@log_datetime
def monthly_backup():
	print('Monthly backup job has finished.')
	print()
		
		
daily_backup()
monthly_backup()
		
		
		
		
		
print(f'{"_"*30}')

def meta_decorator(power):
	def decorator_list(fnc):
		#print(type(fnc))
		def inner(list_of_tuples):
			return [(fnc(val[0], val[1])) ** power for val in list_of_tuples]
		return inner
	return decorator_list

@meta_decorator(2)
def add_together(a, b):
	return a + b
		

print(add_together([(1, 3), (3, 17), (5, 5), (6, 7)]))

print(f'{"_"*30}')
