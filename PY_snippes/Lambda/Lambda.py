list_fn = {"2012": {"01": 0.0, "02": 0.0, "03": 0.0, "04": 0.0, "05": 0.0, "06": 0.0, "07": 0.0, "08": 0.0, "09": 0.0, "10": 134.47799999999998, "11": 208.01399999999995, "12": 105.84400000000002}, "2013": {"01": 103.91399999999999, "02": 198.77499999999998, "03": 566.9929999999998, "04": 772.4599999999999, "05": 972.086, "06": 1117.6950000000002, "07": 1410.3979999999997, "08": 1153.4420000000002, "09": 660.8850000000001, "10": 435.38700000000017, "11": 186.82699999999997, "12": 191.74200000000002}, "2014": {"01": 206.759, "02": 399.04599999999994, "03": 792.1350000000001, "04": 838.556, "05": 1087.12, "06": 1375.8909999999998, "07": 993.8529999999998, "08": 910.6870000000001, "09": 709.9449999999999, "10": 482.658, "11": 191.462, "12": 116.793}, "2015": {"01": 147.99200000000002, "02": 236.47200000000004, "03": 754.8690000000001, "04": 387.4440000000001, "05": 983.84, "06": 1201.286, "07": 1322.0159999999998, "08": 1112.132, "09": 758.1, "10": 436.7139999999999, "11": 219.62800000000004, "12": 173.025}, "2020": {"01": 0.0, "02": 0.0, "03": 0.0, "04": 264.251, "05": 1059.7780000000002, "06": 890.3949999999999, "07": 1133.665, "08": 872.9139999999998, "09": 667.8420000000001, "10": 346.84800000000007, "11": 185.855, "12": 70.75200000000001}, "2021": {"01": 28.644999999999996, "02": 294.35599999999994, "03": 659.2309999999999, "04": 897.6740000000001, "05": 908.5470000000004, "06": 1101.683, "07": 921.1869999999999, "08": 763.331, "09": 746.712, "10": 415.58099999999996, "11": 153.73000000000005, "12": 110.481}, "2022": {"01": 209.879, "02": 368.44100000000003, "03": 748.688, "04": 871.638, "05": 957.0130000000001, "06": 0.0, "07": 0.0, "08": 0.0, "09": 0.0, "10": 0.0, "11": 0.0, "12": 0.0}}		
			
m_list = ['2012_05_01', '2022_02_25']

mul = lambda x: (lambda y: y * x)
times4 = mul(4)
print(times4(2))
		
		
def str_handling(x):
	#ml = list(map(lambda y: x[0:10] if x[4:8] == y else '', m_list))
		
	ml = list(map(lambda y: x[8:10] if x[4:8] == y else '', m_list))
	mx = list(filter(lambda x: x if x != '' else '', ml ))
			
	return mx

		
af = list(map(lambda x: str_handling(x), list_fn))
print(af)
		
		
def check_month():
	test = lambda x,y : y if y[4:8] == x else '-'
	if test != '-': 
		return test
		
check = check_month()
for item in m_list:
	for item_02 in list_fn:
		temp = check(item, item_02)
				
		if temp != '-': print(temp)
		
		#num = (lambda x: "one" if x == 1 else( "two" if x == 2 else ("three" if x == 3 else "ten")))(3)
		#print(num)
		
		#p1 = (lambda x: x[0:10] if x[4:8] == '_01_' else('twoooo'))('2022_01_07.CSV')
		#print(p1)
		
		
p2 = list(map(lambda x: x[0:10] if x[4:8] == '_01_' else '' , list_fn))
print(p2)
		
p3 = list(map(lambda x: x[0:10] if x[4:8] == '_01_' else '' , list_fn))
print(p3)
		
		
from functools import partial  
add = lambda x, y: x + y  
inc = partial (add, 1)  
map = lambda f, l: [f(x) for x in l]  

s = [0, 1, 2, 3]  
s_nested = [s for x in s]  
ss_nested = map(lambda s: map(inc, s), s_nested)  

print (f"s_nested = {s_nested}")  
print (f"ss_nested = {ss_nested}")  
		
		
#Y = (lambda g: lambda f: f(lambda x: g (g) (f) (x))) \  (lambda g: lambda f: f(lambda x: g (g) (f) (x)))  
Y = ((lambda g: lambda f: f(lambda x: g (g) (f) (x)))(lambda g: lambda f: f(lambda x: g (g) (f) (x))))  	
		
n = 6
fibn = Y(lambda f: lambda n: n if n <= 1 else f(n-1) + f(n-2))(n)
print (f"n = {n} Fibonacci({n}) = {fibn}")  
		
def square(w):
	return w**2


n = [4,3,2,1]
print(list(map(square, n)))
print(list(map(lambda x : x**2,n)))
print(list(map(lambda x : square(x),n)))
print('..')
		
		
def get_sub(x):
			
	return('888')
		
p1 = (lambda x: x[4:8])('2022_01_07.CSV')
print(p1)
			
		
p1 = (lambda x: x[0:10] if x[4:8] == '_01_' else('twoooo'))('2022_01_07.CSV')
print(p1)
		
def greetings():
	start ='Hallo'
	greet = lambda y: start + str(y)
	return greet 
		
result = greetings()
print(type(result))
print(result(' RKn'))
		
def greetings_01():
	start ='Hallo '
	greet = lambda x, y: start + 'Herr' + str(x) if y== 'H' else start + 'Frau'+ x
	return greet

result = greetings_01()
print(type(result))
print(result(' RKn', 'H'))
print(result(' BKn', 'a'))
		
		
		
		
p = lambda x: print(x)

p("Hello")
p("World")
		
		
def print_01(a):
	print(a)
		
f1 = lambda x: print_01(x)
f1('hgjhjh') 
		
		
f2 = list(map(lambda x: print_01(x), list_fn))
		
		
colors = ["Goldenrod", "Purple", "Salmon", "Turquoise", "Cyan"]
def normalize_case(string):
	return string.casefold()

normalized_colors = map(normalize_case, colors)
		
normalized_colors_01 = map(lambda s: s.casefold(), colors)
normalized_colors_02 = list(sorted(colors, key=lambda s: s.casefold()))
#print(normalized_colors_02)
		
#A REGULAR FUNCTION
def guru( funct, *args ):
	funct( *args )
	
def printer_one(arg ):
	return print (arg)
	
def printer_two(*arg ):
	print(arg)
	
#CALL A REGULAR FUNCTION 
guru( printer_one, 'printer 1 REGULAR CALL' )
guru( printer_two, 'printer 2 REGULAR CALL \n' )
	
#CALL A REGULAR FUNCTION THRU A LAMBDA
guru(lambda: printer_one('printer 1 LAMBDA CALL'))
guru(lambda: printer_two('printer 2 LAMBDA CALL', 'hhjhjhjhj'))
		
	
