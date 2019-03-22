import os
from time import sleep

def ulang():
	p = raw_input("tekan enter untuk mengulang")
		
def menu():
	print '''
    __ __      ____                     
   / //_/_____/ __ \____  __  __________
  / ,<  / ___/ / / / __ \/ / / /_  /_  /
 / /| |/ /  / /_/ / / / / /_/ / / /_/ /_
/_/ |_/_/   \____/_/ /_/\__,_/ /___/___/
                                        
'''
	sleep(0.7)

	print " Tools		: Perbandingan suhu"
	sleep(0.7)
	print " Author		: Kr0nuzz "
	sleep(0.7)
	print " Github		: https://github.com/Kr0nuzz\n\n"
	sleep(0.7)
	print "pilih perbandingan"
	print "[1] Celcius"
	print "[2] Fahrenheit"
	print "[3] Reamur"
	print "[4] Kelvin"
	pilih = input("masukkan pilihan: ")
	
	if pilih is 1:
		c1 = input("masukkan nilai>>")
		c = c1
		f = c1*1.8 + 32
		k = c1 + 273,5
		r = c1 * 0.8
		print """
 ========================================
 [ Celcius	=	{}		]
 [ Fahrenheit	=	{}		]
 [ Kelvin	=	{}	]
 [ Reamur	=	{}		]
 ========================================
 """.format(c, f, k, r)
	if pilih is 2:
		f1 = input("masukkan nilai")
		f = f1
		c = (((f1-32)*5)/9)
		k = (((f1+459.67)*5)/9)
		r = (((f1-32)*4)/9)
		print """
 ========================================
 [ Celcius	=	{}		]
 [ Fahrenheit	=	{}		]
 [ Kelvin	=	{}		]
 [ Reamur	=	{}		]
 ========================================
 """.format(c, f, k, r)
	if pilih is 3:
		r1 = input("masukkan nilai")
		c = ((r1*5)/4)
		f = (((r1*9)/4)+32)
		k = (((r1*5)/4)+273)
		r = r1
		print """
 ========================================
 [ Celcius	=	{}		]
 [ Fahrenheit	=	{}		]
 [ Kelvin	=	{}		]
 [ Reamur	=	{}		]
 ========================================
 """.format(c, f, k, r)
 	if pilih is 4:
		k1 = input("masukkan nilai")
		c = (((k1-273.15)*5)/5)
		f = (((k1*9)/5)-459.67)
		k = k1
		r = (((k1-273.15)*4)/5)
		print """
 ========================================
 [ Celcius	=	{}		]
 [ Fahrenheit	=	{}		]
 [ Kelvin	=	{}		]
 [ Reamur	=	{}		]
 ========================================
 """.format(c, f, k, r)
 

menu()
ulang()
while True:
	os.system('clear')
	menu()
	ulang()
		
