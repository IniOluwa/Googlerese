Googlerese = {
	"y" : "a",
	"n" : "b",
	"f" : "c", 
	"i" : "d",
	"o" : "k",
	"w" : "f",
	"l" : "g",
	"b" : "h",
	"k" : "i",
	"u" : "j",
	"c" : "e",
	"m" : "l",
	"x" : "m",
	"s" : "n",
	"e" : "o",
	"v" : "p",
	"z" : "q",
	"p" : "r",
	"d" : "s",
	"r" : "t",
	"j" : "u",
	"g" : "v",
	"t" : "w",
	"h" : "x",
	"a" : "y",
	"q" : "z",
	" " : " ",
	"\n" : "\n"
	}

def google_rese(rese):
	grese = " "

	for cha in rese:
		grese += Googlerese[cha]
	return grese

def main():
	with open(".input", "r") as input:
		line = input.readline()
		numTestcases = int(line)

		with open(".output", "w") as output:
		    

			for i in range(numTestcases):
				line = input.readline()
				line = google_rese(line)

				output.write(line)
main()


import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

