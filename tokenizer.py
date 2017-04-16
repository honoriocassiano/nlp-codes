import re

def main():

	text = "Hoje é dia 15 de novembro de 2017. Hoje é dia 15 de novembro."

	dataRE = r"\d{1,2}(\sde\s(\w+|\d{1,2})(\sde\s(\d{4}|\d{2}))?|\/\d{1,2}(\/(\d{4}|\d{2}))?)"

	print(re.sub(dataRE, "_DATA_", text))

	pass


if __name__ == '__main__':
	main()