def totalItems():	
	h = open('history.txt', 'r')
	line = h.readline()
	items = (line.split(' ')[1])

	return int(items)

def buildPurchaseHistory(itemID):
	array = np.zeros(totalItems(), dtype=np.int)
	h = open('history.txt', 'r')
	next(h)
	for i in h:
		if int(i.split(' ')[1]) == int(itemID):
			array[int(i.split(' ')[0]) - 1] = 1
	return array
