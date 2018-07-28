class GuessANumber:

  def readFile():
    trainedList = list()
    with open('GuessStorage.txt') as sFile:
      for line in sFile:
        trainedList.append(int(line))
      return trainedList

  def writeFile(data):
    with open('GuessStorage.txt', 'w') as sFile:
      sFile.writelines(data)

  def train():
    print('training, enter a number between 0-9.')
    responseList = list()
    while len(responseList) < 20:
      userResponse = input('Your number: ')
      try:
        int(userResponse)
        if len(userResponse) == 1:
          print('Enter another number between 0-9.')
          responseList.append(userResponse)
          responseList.append('\n')
        else:
          print('Must be a number between 0-9. Please try again.')
          continue 
      except ValueError:
        print('Must be a number between 0-9. Please try again.') 
    GuessANumber.writeFile(responseList)

  def sortDict(dictionary):
    largestVal = 0
    largestKey = 0
    for key, val in dictionary.items():
      if val > largestVal:
        largestKey = key
        largestVal = val
    sortedKey = largestKey
    return sortedKey

  def guess():
    input('Now think of a number between 0-9. Then press Enter when ready.')
    trainedList = GuessANumber.readFile()
    guessDictionary = dict()
    sortedDictionary = dict()
    for tlVal in trainedList:
      if tlVal in guessDictionary:
        guessDictionary[tlVal] = guessDictionary[tlVal] + 1
      else:
        guessDictionary[tlVal] = 1
    while len(guessDictionary) != 0:
      sortedKey = GuessANumber.sortDict(guessDictionary)
      sortedDictionary[sortedKey] = guessDictionary[sortedKey]
      del guessDictionary[sortedKey]
    print('Probability Table')
    for gdKey, gdVal in sortedDictionary.items():
      probability = gdVal / 10
      print(gdKey, ' ', "{:.0%}".format(probability))
    print('My guess is: ', next(iter(sortedDictionary.keys())),)

GuessANumber.train()
GuessANumber.guess()
