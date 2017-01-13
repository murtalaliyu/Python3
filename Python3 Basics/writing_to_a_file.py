# write will replace with new things
# append will add to the existing file

text = 'Sample Text to Save \nNew line!'

# exampleFile will be created if it doesn't already exist
# you can also specify file path
saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)

# always remember to close when done making changes to file
saveFile.close()
