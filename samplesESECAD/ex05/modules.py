from PIL import Image

test_type_module = type(Image)
print(test_type_module)

mon_image = Image.open('./test.png')
Image._show(mon_image)