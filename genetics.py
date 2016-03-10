import random 

class maxRobot:

	genome = [None]*243
	currentPosition = [1,1]
	iteration = 0
	
	grid = [[0 for x in range(12)] for x in range(12)]
	locale = [0 for x in range(5)]
	averageFitness = 0

	def __init__(self, rubbishIterations, genomeOne):
		# self.createGenome(genomeOne, genomeTwo)
		self.genome = genomeOne
		self.fitnessScore = [0 for x in range(rubbishIterations)]

	def mutateGenome(self, p):
		i = random.randint(1,243)
		for i in range(numGenomes):
			rand = random.random()
			if rand <= p:
				# using 6 as argument as we are creating a random int between 1-6 for our decision			
				self.genome[i] = self.randomDecision(6)

	def findLocale(self):
		self.locale[0] = self.grid[self.currentPosition[0]-1][self.currentPosition[1]]
		self.locale[1] = self.grid[self.currentPosition[0]+1][self.currentPosition[1]]
		self.locale[2] = self.grid[self.currentPosition[0]][self.currentPosition[1]+1]
		self.locale[3] = self.grid[self.currentPosition[0]][self.currentPosition[1]-1]
		self.locale[4] = self.grid[self.currentPosition[0]][self.currentPosition[1]]

	def move(self):
		self.findLocale()
		index = 81*(self.locale[0])+27*(self.locale[1])+9*(self.locale[2])+3*(self.locale[3])+(self.locale[4])
		self.moveMax(self.genome[index])


	def randomDecision(self, limit):
		return random.randint(1,limit)

	def moveMax(self, move):
		if move == 1:
			if self.grid[self.currentPosition[0]-1][self.currentPosition[1]] != 2:
				self.currentPosition[0] -= 1
			else:
				self.fitnessScore[self.iteration] -=5
		elif move == 2:
			if self.grid[self.currentPosition[0]+1][self.currentPosition[1]] != 2:
				self.currentPosition[0] += 1
			else:
				self.fitnessScore[self.iteration] -=5
		elif move == 3:
			if self.grid[self.currentPosition[0]][self.currentPosition[1]+1] != 2:
				self.currentPosition[1] += 1
			else:
				self.fitnessScore[self.iteration] -=5
		elif move == 4:
			if self.grid[self.currentPosition[0]][self.currentPosition[1]-1] != 2:
				self.currentPosition[1] -= 1
			else:
				self.fitnessScore[self.iteration] -=5
		elif move == 5:
			self.pickUpRubbish()
		elif move == 6:
			rand = self.randomDecision(5)
			self.moveMax(rand)

	def pickUpRubbish(self):
		if self.grid[self.currentPosition[0]][self.currentPosition[1]] == 1:
			self.fitnessScore[self.iteration] += 10
			self.grid[self.currentPosition[0]][self.currentPosition[1]] = 0
		elif self.grid[self.currentPosition[0]][self.currentPosition[1]] == 0:
			self.fitnessScore[self.iteration] -= 1

	def meanFitness(self):
		total = 0
		for x in self.fitnessScore:
			total += x
		self.averageFitness = total / len(self.fitnessScore)
# end of maxRobot Class


def quickSort(alist, bots):
   quickSortHelper(alist, bots, 0,len(alist)-1)

def quickSortHelper(alist, bots, first,last):
   if first<last:

       splitpoint = partition(alist, bots, first,last)

       quickSortHelper(alist, bots, first,splitpoint-1)
       quickSortHelper(alist, bots, splitpoint+1,last)


def partition(alist, bots, first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           temp2 = bots[leftmark]
           alist[leftmark] = alist[rightmark]
           bots[leftmark] = bots[rightmark]
           alist[rightmark] = temp
           bots[rightmark] = temp2

   temp = alist[first]
   temp2 = bots[first]
   alist[first] = alist[rightmark]
   bots[first] = bots[rightmark]
   alist[rightmark] = temp
   bots[rightmark] = temp2


   return rightmark

def createGenome(genomeOne = [], genomeTwo = [], p = 0.5):

	rand = random.random()

	# if two genomes have been passed as arguments, cross them. Else create random genome
	if len(genomeOne) != 0 and len(genomeTwo) != 0 and rand < p:
		
		genome = [[None for x in range(243)] for x in range(2)]
		changeIndex = round(p * 243)
		# merge two genomes together
		for i in range(0,243):
			if i < changeIndex:
				genome[0][i] = genomeOne[i]
				genome[1][i] = genomeTwo[i]
			else:
				genome[0][i] = genomeTwo[i]
				genome[1][i] = genomeOne[i]
	elif(len(genomeOne) == 0 and len(genomeTwo) == 0):
		genome = [None]*243
		for i in range(0,243): 
			# using 6 as argument as we are creating a random int between 1-6 for our decision
			genome[i] = random.randint(1,6)
	else:
		genome = [genomeOne, genomeTwo]
	return genome
		
def generateGrid(obj, p):
	for i in range(0, 12):
		for y in range(0, 12):
			if i == 0 or i == 11 or y == 0 or y == 11:
				obj.grid[i][y] = 2
			else:
				rand = random.random()
				if rand < p:
					obj.grid[i][y] = 1
				else:
					obj.grid[i][y] = 0

numGenomes = 200
rubbishIterations = 100
simSteps = 200
rubbishProbability = 0.5
crossProbability = 0.65
mutateProbability = 0.001
totalGens = 1000

numMutate =  round(numGenomes * 0.65)

maxBot = [0 for x in range(numGenomes)]
maxBotFitnesses = [0 for x in range(numGenomes)]

f = open('fitnesses.txt', 'w')

for i in range(0, numGenomes):
	newGenome = createGenome()
	maxBot[i] = maxRobot(rubbishIterations, newGenome)

for loop in range(totalGens):
	f.write(str(maxBotFitnesses)+"\n\n")
	print(maxBotFitnesses)

	# loop through each genome
	for i in range(0, numGenomes):
		# number of rubbish configurations
		for y in range(0, rubbishIterations):
			generateGrid(maxBot[i], rubbishProbability)
			# number of steps per strategy
			for z in range(0, simSteps):
				maxBot[i].move()
			maxBot[i].iteration += 1
			maxBot[i].currentPosition = [1,1];
			
		maxBot[i].meanFitness()

		maxBotFitnesses[i] = maxBot[i].averageFitness

	quickSort(maxBotFitnesses, maxBot)

	fitnessSum = 0
	overallProbability = 0
	botBreadProbability = [0 for x in range(numGenomes)]

	for i in range(0, len(maxBotFitnesses)):
		maxBotFitnesses[i] += 1000
		fitnessSum += maxBotFitnesses[i]

	for i in range(0, len(maxBotFitnesses)):
		botBreadProbability[i] = overallProbability + (maxBotFitnesses[i] / fitnessSum)
		overallProbability = botBreadProbability[i]

	tempMaxBot = []
	# create all the children
	for x in range(int(numMutate/2)):
		parent = [None, None] 

		for u in range(2):
			rand = random.random()

			for q in range(numGenomes):
				if rand <= botBreadProbability[q]:
					parent[u] = maxBot[q].genome
					break

		newGenome = createGenome(parent[0], parent[1], crossProbability)

		tempMaxBot.append(newGenome[0])
		tempMaxBot.append(newGenome[1])

	count = numGenomes-1
	while len(tempMaxBot) != numGenomes:
		tempMaxBot.append(maxBot[count].genome)
		count -= 1

	for x in range(0, numGenomes):
		maxBot[x] = maxRobot(rubbishIterations, tempMaxBot[x])
		maxBot[x].mutateGenome(mutateProbability)

fileEnd = open('finalGenes.txt', 'w')	
for x in range(0, numGenomes):
	fileEnd.write(str(maxBot[x].averageFitness) + "\n")
	fileEnd.write(str(maxBot[x].genome) + "\n\n") 




