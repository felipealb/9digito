#coding:utf-8
#Created by flowp on 28/06/15 - 12:34.
__author__ = 'flowp'

import os

class Contato:
	def __init__(self,caminho):
		arq=open(caminho)
		self.conteudo=arq.readlines()
		self.nome="NONE"
		arq.close()
		self.arq=open(caminho,'w')

	def organiza(self):
		for i in self.conteudo:
			if "CHARSET" in i:
				self.nome=i.split(":")[1].strip().replace(";",'')
				# print(self.nome)
			if "CELL" in i:
				self.numero=i.split(":")[1].strip()

	def analisa(self):
		if len(self.numero)>=9:
			if self.numero[-9]=='9':
				print('=',self.nome,self.numero)
				print()
			else:
				print(self.nome,self.numero,'+=>',end=' ')
				print(self.numero[:-8]+'9'+self.numero[-8:])
				self.numero=self.numero[:-8]+'9'+self.numero[-8:]
		else:
			self.numero="9"+self.numero
			# print('+>',self.nome,self.numero)


	def setNumero(self):
		# print('ANT',self.conteudo[3])
		tag,num=self.conteudo[3].split(':')
		num=self.numero
		self.conteudo[3]=tag+':'+num+'\n'
		# print('DEP',self.conteudo[3])

	def salva(self):
		self.arq.writelines(self.conteudo)
		self.arq.close()

if __name__ == '__main__':
	local='/media/flowp/FELIPE ALB/Pai/'
	files=os.listdir(local)
	lisContatos=[]
	for c in files:
		nome=local+c
		lisContatos.append(Contato(nome))

	for i in lisContatos:
		i.organiza()
		i.analisa()
		i.setNumero()
		i.salva()
