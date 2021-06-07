import numpy as np
import math
import scipy.io.wavfile as waves
import matplotlib.pyplot as plt


####################################   BART   ###########################################
#var
CadenaEnergytBart = []
CadenaRMSxBart = []

for señalDSP in range(0,15):

	if señalDSP == 0:
		archivo='UnoBart.wav'
	if señalDSP == 1:
		archivo='DosBart.wav'
	if señalDSP == 2:
		archivo='TresBart.wav'
	if señalDSP == 3:
		archivo='CuatroBart.wav'
	if señalDSP == 4:
		archivo='CincoBart.wav'
	if señalDSP == 5:
		archivo='SeisBart.wav'
	if señalDSP == 6:
		archivo='SieteBart.wav'
	if señalDSP == 7:
		archivo='OchoBart.wav'
	if señalDSP == 8:
		archivo='NueveBart.wav'
	if señalDSP == 9:
		archivo='DiezBart.wav'
	if señalDSP == 10:
		archivo='OnceBart.wav'
	if señalDSP == 11:
		archivo='DoceBart.wav'
	if señalDSP == 12:
		archivo='TreceBart.wav'
	if señalDSP == 13:
		archivo='CatorceBart.wav'
	if señalDSP == 14:
		archivo='QuinceBart.wav'

	# Preparando la señal
	fsonido, sonido = waves.read(archivo)
	sonido = sonido[:,0].copy()

	n = len(sonido)
	normalizado = []

	for x in range(0,n):
		normalizado.append(sonido[x]/30000)

	# ABSULUTO
	Absoluto = []

	for x in range(0,n):
		Absoluto.append(abs(normalizado[x]))

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))

	CadenaRMSxBart.append(RMSx)	
	CadenaEnergytBart.append(energyt)

print(CadenaRMSxBart)
print("Espacio")
print(CadenaEnergytBart)

	

####################################   HOMERO   ###########################################
#var
CadenaEnergytHomero = []
CadenaRMSxHomero = []

for señalDSP in range(0,15):

	if señalDSP == 0:
		archivo='UnoHomero.wav'
	if señalDSP == 1:
		archivo='DosHomero.wav'
	if señalDSP == 2:
		archivo='TresHomero.wav'
	if señalDSP == 3:
		archivo='CuatroHomero.wav'
	if señalDSP == 4:
		archivo='CincoHomero.wav'
	if señalDSP == 5:
		archivo='SeisHomero.wav'
	if señalDSP == 6:
		archivo='SieteHomero.wav'
	if señalDSP == 7:
		archivo='OchoHomero.wav'
	if señalDSP == 8:
		archivo='NueveHomero.wav'
	if señalDSP == 9:
		archivo='DiezHomero.wav'
	if señalDSP == 10:
		archivo='OnceHomero.wav'
	if señalDSP == 11:
		archivo='DoceHomero.wav'
	if señalDSP == 12:
		archivo='TreceHomero.wav'
	if señalDSP == 13:
		archivo='CatorceHomero.wav'
	if señalDSP == 14:
		archivo='QuinceHomero.wav'

# Preparando la señal
	fsonido, sonido = waves.read(archivo)
	sonido = sonido[:,0].copy()

	n = len(sonido)
	normalizado = []

	for x in range(0,n):
		normalizado.append(sonido[x]/30000)

	# ABSULUTO
	Absoluto = []

	for x in range(0,n):
		Absoluto.append(abs(normalizado[x]))

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))
	
	CadenaRMSxHomero.append(RMSx)
	CadenaEnergytHomero.append(energyt)

print("Espacio homeros")
print(CadenaRMSxHomero)
print(CadenaEnergytHomero)
print("")

####################################   LISA   ###########################################
#var
CadenaEnergytLisa = []
CadenaRMSxLisa = []

for señalDSP in range(0,15):

	if señalDSP == 0:
		archivo='UnoLisa.wav'
	if señalDSP == 1:
		archivo='DosLisa.wav'
	if señalDSP == 2:
		archivo='TresLisa.wav'
	if señalDSP == 3:
		archivo='CuatroLisa.wav'
	if señalDSP == 4:
		archivo='CincoLisa.wav'
	if señalDSP == 5:
		archivo='SeisLisa.wav'
	if señalDSP == 6:
		archivo='SieteLisa.wav'
	if señalDSP == 7:
		archivo='OchoLisa.wav'
	if señalDSP == 8:
		archivo='NueveLisa.wav'
	if señalDSP == 9:
		archivo='DiezLisa.wav'
	if señalDSP == 10:
		archivo='OnceLisa.wav'
	if señalDSP == 11:
		archivo='DoceLisa.wav'
	if señalDSP == 12:
		archivo='TreceLisa.wav'
	if señalDSP == 13:
		archivo='CatorceLisa.wav'
	if señalDSP == 14:
		archivo='QuinceLisa.wav'


	# Preparando la señal
	fsonido, sonido = waves.read(archivo)
	sonido = sonido[:,0].copy()

	n = len(sonido)
	normalizado = []

	for x in range(0,n):
		normalizado.append(sonido[x]/30000)

	# ABSULUTO
	Absoluto = []

	for x in range(0,n):
		Absoluto.append(abs(normalizado[x]))

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))

	CadenaRMSxLisa.append(RMSx)
	CadenaEnergytLisa.append(energyt)

print("Espacio LISAS")
print(CadenaRMSxLisa)
print(CadenaEnergytLisa)
print("")

####################################   MARCH   ###########################################
#var
CadenaEnergytMarch = []
CadenaRMSxMarch = []

for señalDSP in range(0,15):

	if señalDSP == 0:
		archivo='UnoMarch.wav'
	if señalDSP == 1:
		archivo='DosMarch.wav'
	if señalDSP == 2:
		archivo='TresMarch.wav'
	if señalDSP == 3:
		archivo='CuatroMarch.wav'
	if señalDSP == 4:
		archivo='CincoMarch.wav'
	if señalDSP == 5:
		archivo='SeisMarch.wav'
	if señalDSP == 6:
		archivo='SieteMarch.wav'
	if señalDSP == 7:
		archivo='OchoMarch.wav'
	if señalDSP == 8:
		archivo='NueveMarch.wav'
	if señalDSP == 9:
		archivo='DiezMarch.wav'
	if señalDSP == 10:
		archivo='OnceMarch.wav'
	if señalDSP == 11:
		archivo='DoceMarch.wav'
	if señalDSP == 12:
		archivo='TreceMarch.wav'
	if señalDSP == 13:
		archivo='CatorceMarch.wav'
	if señalDSP == 14:
		archivo='QuinceMarch.wav'

	# Preparando la señal
	fsonido, sonido = waves.read(archivo)
	sonido = sonido[:,0].copy()

	n = len(sonido)
	normalizado = []

	for x in range(0,n):
		normalizado.append(sonido[x]/30000)

	# ABSULUTO
	Absoluto = []

	for x in range(0,n):
		Absoluto.append(abs(normalizado[x]))

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))

	CadenaRMSxMarch.append(RMSx)
	CadenaEnergytMarch.append(energyt)

print("Espacio MARCH")
print(CadenaRMSxMarch)
print(CadenaEnergytMarch)
print("")

####################################   SR. BURNS   ###########################################
#var
CadenaEnergytSrBurns = []
CadenaRMSxSrBurns = []

for señalDSP in range(0,15):

	if señalDSP == 0:
		archivo='UnoSrBurns.wav'
	if señalDSP == 1:
		archivo='DosSrBurns.wav'
	if señalDSP == 2:
		archivo='TresSrBurns.wav'
	if señalDSP == 3:
		archivo='CuatroSrBurns.wav'
	if señalDSP == 4:
		archivo='CincoSrBurns.wav'
	if señalDSP == 5:
		archivo='SeisSrBurns.wav'
	if señalDSP == 6:
		archivo='SieteSrBurns.wav'
	if señalDSP == 7:
		archivo='OchoSrBurns.wav'
	if señalDSP == 8:
		archivo='NueveSrBurns.wav'
	if señalDSP == 9:
		archivo='DiezSrBurns.wav'
	if señalDSP == 10:
		archivo='OnceSrBurns.wav'
	if señalDSP == 11:
		archivo='DoceSrBurns.wav'
	if señalDSP == 12:
		archivo='TreceSrBurns.wav'
	if señalDSP == 13:
		archivo='CatorceSrBurns.wav'
	if señalDSP == 14:
		archivo='QuinceSrBurns.wav'

	# Preparando la señal
	fsonido, sonido = waves.read(archivo)
	sonido = sonido[:,0].copy()

	n = len(sonido)
	normalizado = []

	for x in range(0,n):
		normalizado.append(sonido[x]/30000)

	# ABSULUTO
	Absoluto = []

	for x in range(0,n):
		Absoluto.append(abs(normalizado[x]))

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))

	CadenaRMSxSrBurns.append(RMSx)
	CadenaEnergytSrBurns.append(energyt)

print("Espacio SrBurns")
print(CadenaRMSxSrBurns)
print(CadenaEnergytSrBurns)
print("")

####################################   AUDIO DE PRUEBA !!  ###########################################
#var
CadenaEnergytPrueba = []
CadenaRMSxPrueba = []

for señalDSP in range(0,1):

	if señalDSP == 0:
		archivo='DieciseisHomero.wav'
	if señalDSP == 1:
		archivo='DiecisieteHomero.wav'
	if señalDSP == 2:
		archivo='DieciseisBart.wav'
	if señalDSP == 3:
		archivo='DiecisieteBart.wav'
	if señalDSP == 4:
		archivo='DieciseisLisa.wav'
	if señalDSP == 5:
		archivo='DiecisieteLisa.wav'
	if señalDSP == 6:
		archivo='DieciseisMarch.wav'
	if señalDSP == 7:
		archivo='DiecisieteMarch.wav'
	if señalDSP == 8:
		archivo='DieciseisSrBurns.wav'
	if señalDSP == 9:
		archivo='DiecisieteSrBurns.wav'
	if señalDSP == 10:
		archivo='UnoMilhouse.wav'
	if señalDSP == 11:
		archivo='prueba.wav' # mi voz nota: ya es mono audio comentar la linea 403

	# Preparando la señal
	fsonido, sonido = waves.read(archivo)
	sonido = sonido[:,0].copy()

	n = len(sonido)
	normalizado = []

	for x in range(0,n):
		normalizado.append(sonido[x]/30000)

	# ABSULUTO
	Absoluto = []

	for x in range(0,n):
		Absoluto.append(abs(normalizado[x]))

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))

	CadenaRMSxPrueba.append(RMSx)
	CadenaEnergytPrueba.append(energyt)

print("Espacio PRUEBA TIEMPO")
print(CadenaRMSxPrueba)
print(CadenaEnergytPrueba)
print("")


plt. figure(1)
plt.title('Energía vs RMS')
plt.scatter([CadenaRMSxBart],[CadenaEnergytBart], color=['blue'], label= "BART")
plt.scatter([CadenaRMSxHomero],[CadenaEnergytHomero], color=['green'], label= "HOMERO")
plt.scatter([CadenaRMSxLisa],[CadenaEnergytLisa], color=['red'], label= "LISA")
plt.scatter([CadenaRMSxMarch],[CadenaEnergytMarch], color=['yellow'], label= "MARCH")
plt.scatter([CadenaRMSxSrBurns],[CadenaEnergytSrBurns], color=['magenta'], label= "Sr BURNS")
plt.scatter([CadenaRMSxPrueba],[CadenaEnergytPrueba], color=['cyan'], marker = "*",label= "PRUEBA")

plt.xlabel('RMSx')
plt.ylabel('Energía')
plt.legend()
plt.show()


