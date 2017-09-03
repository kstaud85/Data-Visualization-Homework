
# coding: utf-8

# In[1]:

#datavisualization video 1, practice
print ("This is my in class example of how to display text")


# In[2]:

def something ():
    print ("we can write something")


# In[3]:

something ()


# In[14]:

def main():
    print ("Data Visualization if fun!")
if __name__ == '__main__':
    main()


# In[4]:

def main(randomname):
    print ('Hi, '+ randomname)
if __name__ == '__main__':
    main ('Kim')


# In[5]:

main ('Kimberly')


# In[6]:

def main (randomname, age):
    print ("Hi, " + randomname + " you are " + str(age) + " years old.")
if __name__ == '__main__':
    main ("Kim", 23)


# In[7]:

# rounding down practice example
def main (randomname, quantity):
    print ("Hi %s, you have completed %0.2f"% (randomname, quantity) + ' percent of your work')
if __name__ == '__main__':
    main ('Kim', 87.45693)


# In[22]:

import sys


# In[23]:

platform = sys.platform;
print ("%s" % platform)


# In[24]:

pyversion_major = sys.version_info[0];
pyversion_minor = sys.version_info[1];
pyversion_micro = sys.version_info [2];
print ("Python version: %s.%s.%s" % (pyversion_major, pyversion_minor, pyversion_micro))


# In[25]:

import os
openFile = os.open('classfile', os.O_RDONLY)
readmeText = os.read(openFile, 100)
print (readmeText)


# In[35]:

txtContent = "Hi Im an example of a text file"
openFile = open('example', 'w')
readmeText = openFile.write(txtContent)
openFile.close()


# In[36]:

import os
openFile = os.open('example', os.O_RDONLY)
readmeText = os.read(openFile, 100)
print (readmeText)


# In[8]:

# practice functions outside of class can be found below
# sets
kim_set = {4,5,6}
print (kim_set)


# In[20]:

#while loop
for i in range (0,25):
    while 5<i<15:
        print (i)
        break 


# In[39]:

import PIL


# In[40]:


from PIL import Image
from PIL import ImageDraw


# In[64]:

def readcontent():
    openFile = open('example', 'r')
    readmeText = openFile.read()
    openFile.close()
    return openFile, readmeText


# In[76]:

#generating image in color
def generateImage():
    img = Image.new("RGBA", (100, 80), "white")
    draw = ImageDraw.Draw(img)
    output = draw.text((10,10), readmeText, fill = (255,0,0,255))
    draw = ImageDraw.Draw(img)
    img.save("output.png")
    return draw, img, output


# In[77]:

openFile, readmeText = readcontent()


# In[78]:

draw, img, output = generateImage()



# In[ ]:



