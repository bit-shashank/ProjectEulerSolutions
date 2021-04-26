myfile=open("data/p042_words.txt")
contents=myfile.read()
i=0
word_list=contents.split(",")
series_numbers=[]
res=0

def series(n):
	return ((n*(n+1))//2)

for i in range(1,28):
	series_numbers.append(series(i))
traingle_words=[]
t=0
for word in word_list:
	t=0
	word=word.replace("\"","")
	for letter in word:
		t=t+(ord(letter)-64)
	if t in series_numbers:
		traingle_words.append(word)
		res=res+1
		
print("total triangle words are",res)


