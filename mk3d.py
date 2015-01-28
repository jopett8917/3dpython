import PIL
import PIL.ImageDraw
import os.path

def make3D(image):
    return image

def createMask(size):
    
    3dmask = PIL.Image.new('RGBA', (size[0], size[1]), (255,255,255,255))
    mask = PIL.ImageDraw.Draw(3dmask)
    return mask

def addTransparency(image):
    return image
    
def getImages(directory=None):
    
    if directory == None:
        directory = os.getcwd() # Set the directory to the cwd if none is specified
    
    img_list = []
    file_list = []
    
    dir_list = os.listdir(directory)
    for entry in dir_list:
        abs_path = os.path.join(directory, entry)
        try:
            image = PIL.Image.opn(abs_path)
            file_list += [entry]
            img_list += [image]
        except IOError:
            pass
    return img_list, file_list

def main(directory):
    if directory == None:
        directory = os.getcwd()
    
     new_directory = os.path.join(directory, '3d')
     
      try:
          os.mkdir(new_directory)
      except OSError:
          pass
          
       img_list, file_list = get_images(directory) 
       
       for n in range(len(img_list)):
           filename, filetype = file_list[n].split('.')
           new_img = make3d(img_list[n])
           new_img_filename = os.path.join(new_directory, filename + '.png')
           new_img.save(new_img_filename)