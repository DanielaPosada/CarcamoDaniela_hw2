import numpy as np
N=3
Arreglo=(np.random.random((N,N))*10.0)-5.0
print Arreglo
B=(np.random.random((N,1))*10.0)-5.0
print B

#Escriba un codigo de eliminacion Gaussiana para resolver el sistema Ax=B.

sol = np.linalg.solve(Arreglo,B)
print np.dot(Arreglo,sol)
print("sol",sol)

Arreglo1=np.ones((N,N+1),dtype=np.float)
Arreglo1[:,0:N]=Arreglo
Arreglo1[:,N]=B[:,0]
print Arreglo1

numero=1
for k in range(N-1):
	for i in range(numero,N):
		if (Arreglo1[k,k]!=0):
			Arreglo1[i,:]=Arreglo1[i,:]-(Arreglo1[i,k]/Arreglo1[k,k])*Arreglo1[k,:]
		else:
			if(Arreglo[k+1,k]!=0):
				guarda=Arreglo1[k,:]
				Arreglo1[k,:]=Arreglo1[k+1,:]
				Arreglo1[k+1,:]=guarda
	numero=numero+1
print Arreglo1

numero2=N-1
for i in xrange(N-1,-1,-1):
	if(Arreglo1[i,i]!=1):
		Arreglo1[i,:]=Arreglo1[i,:]/Arreglo1[i,i]
	numero2=numero2-1
	for k in xrange(numero2,-1,-1): 
		Arreglo1[k,:]=Arreglo1[k,:]-Arreglo1[k,i]*Arreglo1[i,:]		
print Arreglo1


		
