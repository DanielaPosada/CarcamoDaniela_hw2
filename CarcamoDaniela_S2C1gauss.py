import numpy as np
#N=3
#Arreglo=(np.random.random((N,N))*10.0)-5.0
#print Arreglo
#B=(np.random.random((N,1))*10.0)-5.0
#print B
A = np.array([[4.0,3.0,-2.0],[1.0,2.0,1.0],[-3.0,3.0,2.0]])
B = np.array([[3.0],[2.0],[1.0]])

sol = np.linalg.solve(A,B)
print(A)
print(B)
print("sol",sol)
print(np.dot(A,sol))


#Escriba un codigo de eliminacion Gaussiana para resolver el sistema Ax=B.
temp=np.ones((4))
#print temp
Arreglo1=A
#Arreglo1[:,0:3]=A[:,0:3]
#Arreglo1[:,3]=B[:,0]
print Arreglo1
Arreglodos=Arreglo1
print Arreglodos
Arreglotres=Arreglo1
print Arreglotres


for i in [0]:
	for j in [1, 2]:
		temp=Arreglo1[i,:]*Arreglo1[j,i]/Arreglo1[i,i]
		Arreglodos[j,:]=temp-Arreglo1[j,:]
for i in [1]:
	for j in [2]:
		temp=Arreglo1[i,:]*Arreglo1[j,i]/Arreglo1[i,i]
		Arreglodos[j,:]=temp-Arreglo1[j,:]
print Arreglodos
temp0=Arreglo1[0,:]*Arreglo1[1,0]/Arreglo1[0,0]
Arreglotres[1,:]=temp0-Arreglo1[1,:]
temp1=Arreglo1[0,:]*Arreglo1[2,0]/Arreglo1[0,0]
Arreglotres[2,:]=temp1-Arreglo1[2,:]
print Arreglotres
#print Arreglo3
#for i in range (1,2):
 #   for j in range (0,1):
  #      Arreglo2[i,:]=Arreglo2[i,:]-Arreglo2[i-1,:]*Arreglo2[i,j]
#print Arreglo2

