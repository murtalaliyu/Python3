appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt', 'a')
appendFile.write(appendMe)

# don't forget to close
appendFile.close()
