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
			if "CELL" in i:
				self.numero=i.split(":")[1].strip()

	def analisa(self):
		if len(self.numero)>=9:
			print('----->',self.numero[-8])
			if self.numero[-9]=='9':
				print('OK\t',self.nome,self.numero)
			else:
				if self.numero[-8] not in ['3','4']:
					print('+9+\t',self.nome,self.numero,'+=>',end=' ')
					print(self.numero[:-8]+'9'+self.numero[-8:])
					self.numero=self.numero[:-8]+'9'+self.numero[-8:]
				else:
					print('FX\t',self.nome,self.numero)
		else:
			if self.numero[0] not in ['3','4']:
				self.numero="9"+self.numero
				print('9+\t',self.nome,self.numero)
			else:
				print('FX\t',self.nome,self.numero)


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
