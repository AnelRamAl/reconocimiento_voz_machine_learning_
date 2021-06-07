import numpy as np
import math
import scipy.io.wavfile as waves
import matplotlib.pyplot as plt
import scipy.fftpack as fourier
from scipy.io import wavfile
import librosa
import librosa.display
from mpl_toolkits.mplot3d import Axes3D
from sklearn import tree

####################################   BART   ###########################################
#var
CadenaEnergytBart = []
CadenaRMSxBart = []
CadenamfccBart = []

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


	samplingFrequency, signalData = wavfile.read(archivo)
	y, sr = librosa.load(archivo)
	n_fft = 2048								
	n_mels = 128

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

	n= len(normalizado)
	norm = np.array([]);
	norm = normalizado;

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))

	CadenaRMSxBart.append(RMSx)	
	CadenaEnergytBart.append(energyt)

	#CARACTERISTICAS EN LA FRECUENCIA
	n = len(norm)
	frec = np.fft.fftfreq(n)
	mascara = frec > 0 

	#señal 
	fft_valores = np.fft.fft(norm)
	ab1 = (1/n)*np.abs(fft_valores)

	mel = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)

	abi = ab1[mascara]

	def functionHl(frecuencia):
		Hl = 0
		frecuencia = frecuencia
		f = []
		idxs_to_plot = [0, 9, 49, 99, 127]
		for i in idxs_to_plot:
			f = mel[i]
			for x in range(0,len(f)):
				if x+1 == frecuencia:
					Hl = f[x]
					break
			if Hl != 0:
				break
		return(Hl)

	N = len(frec[mascara])
	freci = frec[mascara]

	AnchoBanda = 1030
	FrstSuma = 0
	for x in range(0,AnchoBanda):	 
		Hl = functionHl(x)
		plus = abi[x]*Hl
		FrstSuma = FrstSuma + plus

	FrstSuma = math.log10(FrstSuma)

	N = len(freci)
	DCT = 0
	for x in range(0,N):
		plus = (freci[x] *math.cos(3.1416/(N*(x+0.5))))*FrstSuma
		DCT = DCT + plus	

	mfcc = abs(DCT)

	CadenamfccBart.append(mfcc)
	

####################################   HOMERO   ###########################################
#var
CadenaEnergytHomero = []
CadenaRMSxHomero = []
CadenamfccHomero = []


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

	samplingFrequency, signalData = wavfile.read(archivo)
	y, sr = librosa.load(archivo)
	n_fft = 2048								
	n_mels = 128

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

	n= len(normalizado)
	norm = np.array([]);
	norm = normalizado;

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))
	
	CadenaRMSxHomero.append(RMSx)
	CadenaEnergytHomero.append(energyt)

	#CARACTERISTICAS EN LA FRECUENCIA
	n = len(norm)
	frec = np.fft.fftfreq(n)
	mascara = frec > 0 

	#señal 
	fft_valores = np.fft.fft(norm)
	ab1 = (1/n)*np.abs(fft_valores)

	mel = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)

	abi = ab1[mascara]

	def functionHl(frecuencia):
		Hl = 0
		frecuencia = frecuencia
		f = []
		idxs_to_plot = [0, 9, 49, 99, 127]
		for i in idxs_to_plot:
			f = mel[i]
			for x in range(0,len(f)):
				if x+1 == frecuencia:
					Hl = f[x]
					break
			if Hl != 0:
				break
		return(Hl)

	N = len(frec[mascara])
	freci = frec[mascara]

	AnchoBanda = 1030
	FrstSuma = 0
	for x in range(0,AnchoBanda):	 
		Hl = functionHl(x)
		plus = abi[x]*Hl
		FrstSuma = FrstSuma + plus

	FrstSuma = math.log10(FrstSuma)

	N = len(freci)
	DCT = 0
	for x in range(0,N):
		plus = (freci[x] *math.cos(3.1416/(N*(x+0.5))))*FrstSuma
		DCT = DCT + plus	

	mfcc = abs(DCT)

	CadenamfccHomero.append(mfcc)

####################################   LISA   ###########################################
#var
CadenaEnergytLisa = []
CadenaRMSxLisa = []
CadenamfccLisa = []


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

	samplingFrequency, signalData = wavfile.read(archivo)
	y, sr = librosa.load(archivo)
	n_fft = 2048								
	n_mels = 128

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

	n= len(normalizado)
	norm = np.array([]);
	norm = normalizado;

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))

	CadenaRMSxLisa.append(RMSx)
	CadenaEnergytLisa.append(energyt)


	#CARACTERISTICAS EN LA FRECUENCIA
	n = len(norm)
	frec = np.fft.fftfreq(n)
	mascara = frec > 0 

	#señal 
	fft_valores = np.fft.fft(norm)
	ab1 = (1/n)*np.abs(fft_valores)

	mel = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)

	abi = ab1[mascara]

	def functionHl(frecuencia):
		Hl = 0
		frecuencia = frecuencia
		f = []
		idxs_to_plot = [0, 9, 49, 99, 127]
		for i in idxs_to_plot:
			f = mel[i]
			for x in range(0,len(f)):
				if x+1 == frecuencia:
					Hl = f[x]
					break
			if Hl != 0:
				break
		return(Hl)

	N = len(frec[mascara])
	freci = frec[mascara]

	AnchoBanda = 1030
	FrstSuma = 0
	for x in range(0,AnchoBanda):	 
		Hl = functionHl(x)
		plus = abi[x]*Hl
		FrstSuma = FrstSuma + plus

	FrstSuma = math.log10(FrstSuma)

	N = len(freci)
	DCT = 0
	for x in range(0,N):
		plus = (freci[x] *math.cos(3.1416/(N*(x+0.5))))*FrstSuma
		DCT = DCT + plus	

	mfcc = abs(DCT)

	CadenamfccLisa.append(mfcc)

####################################   MARCH   ###########################################
#var
CadenaEnergytMarch = []
CadenaRMSxMarch = []
CadenamfccMarch = []

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

	samplingFrequency, signalData = wavfile.read(archivo)
	y, sr = librosa.load(archivo)
	n_fft = 2048								
	n_mels = 128

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

	n= len(normalizado)
	norm = np.array([]);
	norm = normalizado;

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))

	CadenaRMSxMarch.append(RMSx)
	CadenaEnergytMarch.append(energyt)

	#CARACTERISTICAS EN LA FRECUENCIA
	n = len(norm)
	frec = np.fft.fftfreq(n)
	mascara = frec > 0 

	#señal 
	fft_valores = np.fft.fft(norm)
	ab1 = (1/n)*np.abs(fft_valores)


	mel = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)

	abi = ab1[mascara]

	def functionHl(frecuencia):
		Hl = 0
		frecuencia = frecuencia
		f = []
		idxs_to_plot = [0, 9, 49, 99, 127]
		for i in idxs_to_plot:
			f = mel[i]
			for x in range(0,len(f)):
				if x+1 == frecuencia:
					Hl = f[x]
					break
			if Hl != 0:
				break
		return(Hl)

	N = len(frec[mascara])
	freci = frec[mascara]

	AnchoBanda = 1030
	FrstSuma = 0
	for x in range(0,AnchoBanda):	 
		Hl = functionHl(x)
		plus = abi[x]*Hl
		FrstSuma = FrstSuma + plus

	FrstSuma = math.log10(FrstSuma)

	N = len(freci)
	DCT = 0
	for x in range(0,N):
		plus = (freci[x] *math.cos(3.1416/(N*(x+0.5))))*FrstSuma
		DCT = DCT + plus	

	mfcc = abs(DCT)

	CadenamfccMarch.append(mfcc)


####################################   Sr BURNS   ###########################################
#var
CadenaEnergytSrBurns = []
CadenaRMSxSrBurns = []
CadenamfccSrBurns = []

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

	samplingFrequency, signalData = wavfile.read(archivo)
	y, sr = librosa.load(archivo)
	n_fft = 2048								
	n_mels = 128

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

	n= len(normalizado)
	norm = np.array([]);
	norm = normalizado;

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))

	CadenaRMSxSrBurns.append(RMSx)
	CadenaEnergytSrBurns.append(energyt)

	#CARACTERISTICAS EN LA FRECUENCIA
	n = len(norm)
	frec = np.fft.fftfreq(n)
	mascara = frec > 0 

	#señal 
	fft_valores = np.fft.fft(norm)
	ab1 = (1/n)*np.abs(fft_valores)

	mel = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)

	abi = ab1[mascara]

	def functionHl(frecuencia):
		Hl = 0
		frecuencia = frecuencia
		f = []
		idxs_to_plot = [0, 9, 49, 99, 127]
		for i in idxs_to_plot:
			f = mel[i]
			for x in range(0,len(f)):
				if x+1 == frecuencia:
					Hl = f[x]
					break
			if Hl != 0:
				break
		return(Hl)

	N = len(frec[mascara])
	freci = frec[mascara]

	AnchoBanda = 1030
	FrstSuma = 0
	for x in range(0,AnchoBanda):	 
		Hl = functionHl(x)
		plus = abi[x]*Hl
		FrstSuma = FrstSuma + plus

	FrstSuma = math.log10(FrstSuma)

	N = len(freci)
	DCT = 0
	for x in range(0,N):
		plus = (freci[x] *math.cos(3.1416/(N*(x+0.5))))*FrstSuma
		DCT = DCT + plus	

	mfcc = abs(DCT)

	CadenamfccSrBurns.append(mfcc)

####################################  AUDIO DE PRUEBA !!  ###########################################
#var
CadenaEnergytPrueba = []
CadenaRMSxPrueba = []
CadenamfccPrueba = []

for señalDSP in range(0,1):

	if señalDSP == 0:
		archivo='DiecisieteHomero.wav'
	if señalDSP == 1:
		archivo='DosSrBurns.wav'
	if señalDSP == 2:
		archivo='TresSrBurns.wav'
	if señalDSP == 3:
		archivo='CuatroSrBurns.wav'


	samplingFrequency, signalData = wavfile.read(archivo)
	y, sr = librosa.load(archivo)
	n_fft = 2048								
	n_mels = 128

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

	n= len(normalizado)
	norm = np.array([]);
	norm = normalizado;

	# CARACTERÍSTICAS EN TIEMPO  Energía y RMS

	N = len(Absoluto)
	energyt = 0
	for x in range(0,N):
		plus = (Absoluto[x])**2
		energyt = energyt + plus

	RMSx = math.sqrt(energyt/(N**2))

	CadenaRMSxPrueba.append(RMSx)
	CadenaEnergytPrueba.append(energyt)

	#CARACTERISTICAS EN LA FRECUENCIA
	n = len(norm)
	frec = np.fft.fftfreq(n)
	mascara = frec > 0 

	#señal 
	fft_valores = np.fft.fft(norm)
	ab1 = (1/n)*np.abs(fft_valores)

	mel = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)

	abi = ab1[mascara]

	def functionHl(frecuencia):
		Hl = 0
		frecuencia = frecuencia
		f = []
		idxs_to_plot = [0, 9, 49, 99, 127]
		for i in idxs_to_plot:
			f = mel[i]
			for x in range(0,len(f)):
				if x+1 == frecuencia:
					Hl = f[x]
					break
			if Hl != 0:
				break
		return(Hl)

	N = len(frec[mascara])
	freci = frec[mascara]

	AnchoBanda = 1030
	FrstSuma = 0
	for x in range(0,AnchoBanda):	 
		Hl = functionHl(x)
		plus = abi[x]*Hl
		FrstSuma = FrstSuma + plus

	FrstSuma = math.log10(FrstSuma)

	N = len(freci)
	DCT = 0
	for x in range(0,N):
		plus = (freci[x] *math.cos(3.1416/(N*(x+0.5))))*FrstSuma
		DCT = DCT + plus	

	mfcc = abs(DCT)

	CadenamfccPrueba.append(mfcc)

fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.set_title('x = RMS, y = Energía, z = MFCC')

ax.scatter([CadenaRMSxBart],[CadenaEnergytBart],[CadenamfccBart], color=['blue'], label= "BART")
ax.scatter([CadenaRMSxHomero],[CadenaEnergytHomero],[CadenamfccHomero], color=['green'], label= "HOMERO")
ax.scatter([CadenaRMSxLisa],[CadenaEnergytLisa],[CadenamfccLisa], color=['red'], label= "LISA")
ax.scatter([CadenaRMSxMarch],[CadenaEnergytMarch],[CadenamfccMarch], color=['yellow'], label= "MARCH")
ax.scatter([CadenaRMSxSrBurns],[CadenaEnergytSrBurns],[CadenamfccSrBurns], color=['magenta'], label= "SR BURNS")
ax.scatter([CadenaRMSxPrueba],[CadenaEnergytPrueba],[CadenamfccPrueba], color=['cyan'], marker = "*",label= "PRUEBA")


ax.set_xlabel('RMSx')
ax.set_ylabel('Energía')
ax.set_zlabel('MFCC')

plt.legend()
plt.show()


