# from PIL import Image
# import os, glob
#
# files = glob.glob('alcohol_pic - 복사본/*.jpg')
# print(files)
#
# for f in files:
#     img = Image.open(f)
#     img_resize = img.resize((300,300))
#     title, ext = os.path.splitext(f)
#     img_resize.save(title + '_resize' + ext)


# from PIL import Image
# import os
#
# files = os.listdir('alcohol_pic - 복사본/')
# print(files)
# basewidth = 300
#
# for f in files:
#     if f == '100.jpg':
#         pass
#     else:
#         img = Image.open(f'alcohol_pic - 복사본/{f}')
#         wpercent = basewidth/float(img.size[0])
#         hsize = int(float(img.size[1])*float(wpercent))
#         img = img.resize((basewidth, hsize), Image.ANTIALIAS)
#         try:
#             img = img.convert('RGB')
#             img.save(f'resized_{f}')
#         except:pass

# from PIL import Image
# import os, glob
#
#
# basewidth = 300
#
# for f in glob.glob('alcohol_pic - 복사본/*.jpg'):
#     print(f)
#     if f == 'alcohol_pic - 복사본/100.jpg':
#         pass
#     else:
#         wpercent = basewidth/float(f.size[0])
#         hsize = int(float(f.size[1])*float(wpercent))
#         file, ext = os.path.splitext(f)
#         im = Image.open(f)
#         im.thumbnail(wpercent, hsize)
#         im.save(file+'.thumbnail', 'JPEG')


# imag1_size = image1.size
#
# print(imag1_size)
#
# image1 = image1.resize((int(imag1_size[0]*(0.7)), int(imag1_size[1]*(0.7))))
#
# imag1_size = image1.size
#
# print(imag1_size)
