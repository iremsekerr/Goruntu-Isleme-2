from PIL import Image
import numpy as np

# kullanacağımız görüntüyü yükledik
image = Image.open("D:\Balon.png")

# Görüntünün boyutlarını aldık
width, height = image.size

# Convolution için kerneli tanımladık
kernel = np.array([[0, 0, -1, 0, 0],
    [0, -1, -2, -1, 0],
    [-1, -2, 16, -2, -1],
    [0, -1, -2, -1, 0],
    [0, 0, -1, 0, 0]
])

# Matrisi tanımladık ve pikselleri matrise ekledik
matrix = np.zeros((height, width, 4))
for y in range(height):
    for x in range(width):
        pixel = image.getpixel((x, y))
        matrix[y][x] = pixel

# Convolution işlemini for döngüleriyle gerçekleştirdik
new_matrix = np.zeros((height, width))
for y in range(2, height - 2):
    for x in range(2, width - 2):
        value = 0
        for i in range(-2, 3):
            for j in range(-2, 3):
                pixel = matrix[y + i][x + j]
                kernel_value = kernel[i + 2][j + 2]
                value += sum(pixel) * kernel_value
        new_matrix[y][x] = value

# Normalizasyon islemini gerceklestirdik.daha net bir görüntü elde etmek icin bunu yaptık.
min_val = np.min(new_matrix)
max_val = np.max(new_matrix)
new_matrix = (new_matrix - min_val) / (max_val - min_val) * 255

# Olusturulan yeni resmi kaydettik.
im = Image.fromarray(new_matrix.astype(np.uint8))
im.save("filtered_image.png")