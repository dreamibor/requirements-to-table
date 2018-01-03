# Parser for Python requirements.txt to build a table (markdown / html)
# Example: python txt2md.py -i requirements.txt -o table.html -s html
# OR: python txt2md.py -i requirements.txt -o table.md -s md


import argparse


def parse(sentence):
	first_equal = 0
	for index, char in enumerate(sentence):
		if char == "=":
			first_equal = index
			break
	name = sentence[:first_equal] 
	version = sentence[first_equal+2:]
	return name, version[:len(version)-1]


def main(args):
	requirements = []
	with open(args.i, 'r') as f:
		for line in f:
			name, version = parse(line)
			requirements.append((name, version))
	if args.s == "md" and args.o[len(args.o)-2:] == "md":
		with open(args.o, 'w+') as f:
			f.write("| Package Name | Version |\n")
			f.write("| ------------ | ------- |\n")
			for package in requirements:
				f.write("| {} | {} |\n".format(package[0], package[1]))
			print("The table file {} was created successfully!".format(args.o))
	elif args.s == "html" and args.o[len(args.o)-4:] == "html":
		with open(args.o, 'w+') as f:
			f.write("<table>\n<tr><th>Package Name</th><th>Version</th></tr>\n")
			for package in requirements:
				f.write("<tr><td>{}</td><td>{}</td></tr>\n".format(package[0], package[1]))
			f.write("</table>\n")
			print("The table file {} was created successfully!".format(args.o))
	else:
		print("Wrong Format! You chose {} but the output name is not compatible".format(args.s))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Parse requirements txt to Markdown / HTMLtable.')
	parser.add_argument('-i', type=str, help='Input requirements.txt path')
	parser.add_argument('-o', type=str, help='Output markdown / HTML path')
	parser.add_argument('-s', type=str, help='Output style: Markdowen / HTML')
	args = parser.parse_args()
	main(args)
