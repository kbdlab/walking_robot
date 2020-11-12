from PIL import Image
import glob

pospath = glob.glob('./positive_images/*.jpg')
negpath = glob.glob('./negative_images/*.jpg')

ptxt = open("positives.txt",'w')
ntxt = open("negatives.txt",'w')

def resize_n_txt(path, pn):
    if pn == 'p':
        for index in range(len(path)):
            print(path[index])
            im = Image.open(path[index])
            print(im.size)
            width = im.size[0]
            height = im.size[1]
            size = (40, 100)
            im=im.resize(size)
            im.save(path[index])
            string = "{0} 1 0 0 {1} {2}\n".format(path[index], size[0], size[1])
            ptxt.write(string)
        ptxt.close
    elif pn == 'n':
        for index in range(len(path)):
            string = "{}\n".format(path[index])
            ntxt.write(string)
        ntxt.close
        
if __name__ == "__main__":
    resize_n_txt(pospath, 'p')
    resize_n_txt(negpath, 'n')

    