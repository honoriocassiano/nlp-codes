import re

def main():

	text = "Hoje é dia 15 de novembro de 2017. Hoje é dia 15 de novembro. Meu telefone é (21) 90999 9999. Tenho 21 anos."

	dataRE = r"\d{1,2}(\ de\s(\w+|\d{1,2})(\ de\ (\d{4}|\d{2}))?|\/\d{1,2}(\/(\d{4}|\d{2}))?)"
	foneRE = r"\(?(\d{2})?\)?\ ?\d{4,5}[-\ ]?\d{4}"

	regexDict = {}
	# Date Regex
	regexDict[r"\d{1,2}(\sde\s(\w+|\d{1,2})(\sde\s(\d{4}|\d{2}))?|\/\d{1,2}(\/(\d{4}|\d{2}))?)"] = "_DATA_"
	# Fone Regex
	regexDict[r"\(?(\d{2})?\)?\ ?\d{4,5}[-\ ]?\d{4}"] = "_TELEFONE_"

	# Number Regex
	regexDict[r"\d+\w*"] = "_NUMERO_"

	newText = text

	for k in regexDict:
		newText = re.sub(k, regexDict[k], newText)

	print("Original text: \"%s\"" % (text,))
	print("Tokenized text: \"%s\"" % (newText,))

	pass


if __name__ == '__main__':
	main()