# Andrea Rahmadanisya 1301184146
# Vijay Cheza Pangestu 1301180351

import random as rd
import numpy as np
import matplotlib.pyplot as plts

# variabel Scalar
jumlah_individu = 200  # 200 individu
rasio_terinfeksi = 0.05  # 5% : 0.05
PMove = 0.8  # 80% : 0.8
WPemulihan = 10
jumlah_terinfeksi = int(jumlah_individu * rasio_terinfeksi)

# space
x_max = 20
y_max = 20
x_min = 0
y_min = 0

range_x = x_max - x_min
range_y = y_max - y_min
x_position = []
y_position = []

# variabel list
for i in range(jumlah_individu):
    x_position.append(rd.randint(x_min, x_max))
    y_position.append(rd.randint(y_min, y_max))

WInfeksi = []
imun = []


# Inisial waktu infeksi
WInfeksi.append(0)
