import re

# Links:
# - http://g1.globo.com/politica/noticia/2015/09/10-aprovam-e-69-reprovam-governo-dilma-diz-ibope.html
# - https://pt.wikipedia.org/wiki/Ataques_de_11_de_setembro_de_2001
# - http://extra.globo.com/casos-de-policia/disque-denuncia-oferece-recompensa-por-informacoes-sobre-homem-com-31-mandados-de-prisao-21126192.html
# - http://www.diariodaregiao.com.br/cultura/casa-das-janelas-ganha-novo-endere%C3%A7o-1.685275

def main():

	filename = input('Filename: ')

	filenameOut = '.'.join( [ t + '_tokenized' if i == 0 else t for i, t in enumerate(filename.split('.')) ] )

	file = open(filename, 'r')
	text = file.read()
	file.close()

	regexList = []

	# Date Regex
	regexList.append( (r"\d{1,2}(\sde\s(\w+|\d{1,2})(\sde\s(\d{4}|\d{2}))?|\/\d{1,2}(\/(\d{4}|\d{2}))?)", "_DATA_") )

	# Fone Regex
	regexList.append( (r"((\(\d{2}\))|(\d{2}))\ ?\d{4,5}[-\ ]?\d{4}", "_TELEFONE_") )

	# Address Regex
	regexList.append( (r"[Rr]ua(\ \w+)+(,?\ ?\d+)?", "_ENDERECO_") )

	# Number Regex
	regexList.append( (r"\d+[\w%]*", "_NUMERO_") )
	
	newText = text

	for i in regexList:
		newText = re.sub(i[0], i[1], newText)

	fileOut = open(filenameOut, 'w')
	fileOut.write(newText)
	fileOut.close()

	print('Tokenized text saved to: %s\n\n' % (filenameOut,))

	print("Original text: \n\n\"%s\"\n" % (text,))
	print("Tokenized text: \n\n\"%s\"" % (newText,))

if __name__ == '__main__':
	main()