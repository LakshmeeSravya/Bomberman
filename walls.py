from termcolor import colored

class Walls:

	def __init__(self):
		self.__arr=[]

	def structure(self):
		for i in range(0,38):
			self.__arr.append([])
		for i in range(0,2):
			for j in range(0,76):
				self.__arr[i].append(colored('#','blue'))
		for i in range(2,36):
			for j in range(0,76):
				if(i%4==2 or i%4==3):
					if(j<=3 or j>=72):
						self.__arr[i].append(colored('#','blue'))
					else:
						self.__arr[i].append(' ')
				else:
					if(j%8==0 or j%8==1 or j%8==2 or j%8==3):
						self.__arr[i].append(colored('#','blue'))
					else:
						self.__arr[i].append(' ')
		for i in range(36,38):
			for j in range(0,76):
				self.__arr[i].append(colored('#','blue'))
		return self.__arr
