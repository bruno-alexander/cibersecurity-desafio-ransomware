## codigo descriptografia -- desafio ciberseguranca

## importacoes
import os
import pyaes
## definicao variaveis
lista_arquivos = os.listdir('.')
arquivos_txt = []
## chave descriptografia
chave = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(chave)
## busca arquivos
def busca_txt(lista_arquivos):
	for arquivo in lista_arquivos:
		if "txt.ransomwaretroll" in arquivo:
			arquivos_txt.append(arquivo)
	return arquivos_txt
## resolucao
def resolucao():
	for txt in arquivos_txt:
		## abrir arquivo criptografado
		file = open(txt, "rb")
		file_data = file.read()
		file.close()
		## remover criptografia
		decrypt_data = aes.decrypt(file_data)
		## remover arquivo criptografado
		os.remove(txt)
		## criar arquivo descriptografado
		new_file = txt.replace(".ransomwaretroll","")
		new_file = open(f'{new_file}', "wb")
		new_file.write(decrypt_data)
		new_file.close()
## ponto de entrada
if __name__ == "__main__":
	arquivos_txt = busca_txt(lista_arquivos)
	resolucao ()


