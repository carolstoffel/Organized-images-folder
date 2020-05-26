import os, shutil
from PIL import Image


dir = "D:\\Imagens\\snap" # CHANGE HERE TO THE FOLDER YOU WANT TO ORGANIZE
change_dir_to = os.chdir("{}".format(dir))

#print(os.listdir()) # prints the files in actual folder

files = os.listdir() # save all the filenames in files variable
formatImages = ['.jpeg', '.png', '.sgv', '.gif', '.bmp', '.jpg']

images = []
for file in files:
    name, extension = os.path.splitext(file)
    if extension in formatImages:
        images.append(file)


createdIn = str()
for image in images:
    try:
        if not os.path.isdir(image): # if the image is not a folder
            try:
                createdIn = Image.open(dir+'\\'+image)._getexif()[36867] # get the date information
            except Exception:
                print("It's no possible to read this image.")
            year = createdIn[0:4]
            month = createdIn[5:7]
            print(year)
            if not os.path.isdir('./'+year): # if the year is not a directory already
                os.mkdir('./{}'.format(year)) # creates the directory
                print('Created the {} directory'.format(year))
            shutil.move(image, './{}/{}'.format(year, image)) # move the image to the corresponding year
    except Exception as error:
        print('ERROR CODE: {}'.format(repr(error)))
