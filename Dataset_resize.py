from PIL import Image
from glob import glob

files = glob("/home/pszry/usr/local/RSML/RSML/example/Datasert/*.jpg")
#print files
i= len(files)
print i

for x in range(0, 3):
    fn = files[x] 
    fd_img = open(fn, 'r')
    a = os.path.basename(fn)
    img = Image.open(fd_img)
    img = resizeimage.contain(img, [500, 500]) 
    img = img.convert('RGB')
    img.save('/home/pszry/usr/local/SegNet/Dataset/Roots/a[:-4]'+'.png', img.format)
    fd_img.close()      

 
