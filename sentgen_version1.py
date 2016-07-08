import nltk
import random

infile = open('corpus/int12.txt','r')
inlines = infile.readlines()
len1 = len(inlines)
ofile = open('results/resultx_20.txt','w')

def randomx(rangex):
	return random.randint(0,rangex)

def distribution(word):
	followed = []
	after = []
	for k in range(len1):
		thisline = inlines[k]
		herewords = thisline.split()
		lenh = len(herewords)
		for j in range(lenh):
			if(herewords[j]==word):
				followed.append(herewords[j+1])
				if j+2<lenh:
					after.append(herewords[j+2])			
	#return ' '.join(followed)
	return followed,after

def distribution2(word):
	followed = []
	for k in range(len1):
		thisline = inlines[k]
		herewords = thisline.split()
		lenh = len(herewords)
		for j in range(lenh):
			if(herewords[j]==word):
				if j+1<lenh:
					followed.append(herewords[j+1])
	return followed
'''
def randomx(rangex):
	return random.randint(1,rangex)
'''

def calc_next(text1,text2):
	fdist1 = nltk.FreqDist(text1)
	print fdist1
	lnf = len(fdist1)
	if lnf > 20:
		res1 = fdist1.most_common(20)
	else:
		res1 = fdist1.most_common(lnf)
	lenres = len(res1)
	additionaltext = []
	
	beforecommon = []
	for w in range(lenres):
		rx = res1[w]
		#sum1 = sum1 + rx[1]
		beforecommon.append(rx[0])
		got1 = distribution2(rx[0])
		additionaltext.extend(got1)
	#print 'additionaltext = ', additionaltext
	fdist2 = nltk.FreqDist(additionaltext)
	res2 = fdist2.most_common(30)
	#print 'res2 = ',res2 
	aftercommon = []
	for y in range(30):
		try:
			sx = res2[y]
			aftercommon.append(sx[0])
		except IndexError:
			break;

	bothcommon = []
	print 'beforecommon =',beforecommon
	print 'aftercommon =',aftercommon
	for p in range(lenres):
		if beforecommon[p] in aftercommon:
			bothcommon.append(beforecommon[p])
	lenbc = len(bothcommon)
	if lenbc==0:
		return 'again'
	inty = randomx(lenbc-1)
	print inty, bothcommon
	return bothcommon[inty]	

def generate(wordx,times):
	for x in range(times):
		this1 = wordx
		ofile.write(this1)
		ofile.write(" ")
		for k in range(20):
			text1,text2 = distribution(this1)
			next1 = calc_next(text1,text2)
			if(next1=='<stop>'): 
				ofile.write('.')
				ofile.write(" ")
				break;
			elif (next1 == 'again'):
				continue;	
			elif (next1 == '<comma>'):
				ofile.write(', ')
				#ofile.write(" ")
			else:
				ofile.write(next1)
				ofile.write(" ")
				this1 = next1
		ofile.write("\n")

def main():
	inputs = ['Emirates','Dubai','British','London','In','The']
	for h in range(6):
		generate(inputs[h],10)
		ofile.write("\n")

if __name__=='__main__':
	main()