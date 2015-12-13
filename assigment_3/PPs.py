def mapFileParse():
	f = open('paths.txt', 'r')
	for line in f:
		map = []
		for l in line[2:].replace('\r\n','').replace(' ',''):
			map.append(l)
		paths.update({line[0]:map})
	f.close()

def ThreeSome(path):
    dests = set()
    for key in paths[path]:
        dests.add(key)
        if key in paths:
            dests.update(ThreeSome(key))
    return list(dests)


if __name__ == '__main__':
	paths = {}
	results = {}
	mapFileParse()
	for key in paths:
		results.update({key : ThreeSome(key)})
	f = open('commandsP2.txt','r')
	for city in f.read().split(','):
		if city in paths:
			print city + ":" + str(results[city])
		else:
			print "City '%s' has no reachable neighbour" % (city)
