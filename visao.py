
import cv2
import numpy as np
#from skimage 
import io
import numpy as np
from numpy.lib.utils import source
import pytesseract
import shutil
import os
import random
try:
 from PIL import Image
except ImportError:
 import Image

img = io.imread("https://i.postimg.cc/gJ4BL7Hn/cards.jpg") # Carrega imagem a partir de uma URL
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Função responsável por converter do formato BGR para RGB

print("(altura, largura, canais)")
print(img.shape)
print("Imagem no padrão RGB")
cv2.imshow(img) # Função responsável por exibir a imagem na plataforma Google Colab (equivalente a função cv2.imshow())

# Apenas para vizualização #
# Marcação dos 4 vértices (AZUL)
cv2.circle(img,(450,127),2,(255,255,0),5) # Vértice 1
cv2.circle(img,(276,117),2,(255,255,0),5) # Vértice 2
#cv2.circle(img,(154,482),2,(255,255,0),5) # Vértice 3
cv2.circle(img,(455,372),2,(255,255,0),5) # Vértice 4
# Apenas para vizualização #

cv2.imshow(img)

# Tamanho da carta
width,height = 250,350

# Coordenadas desejadas da projeção
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# Retângulo representando a posição desejada (VERMELHO)
cv2.rectangle(img,(0,0),(width,height),(0,0,255),2)

cv2.imshow(img)

# Coordenadas atuais dos 4 vértices
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])

# Coordenadas desejadas da projeção
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# Apenas para vizualização #
# Marcação dos 4 vértices (AZUL)
cv2.circle(img,(276,117),2,(255,255,0),5) # Vértice 1
cv2.circle(img,(450,127),2,(255,255,0),5) # Vértice 2
cv2.circle(img,(270,360),2,(255,255,0),5) # Vértice 3
cv2.circle(img,(455,372),2,(255,255,0),5) # Vértice 4
# Apenas para vizualização #

# Marcação das 4 linhas (VERDE)
cv2.line(img,(0,0),(276,117),(0,255,0),3)
cv2.line(img,(width,0),(450,127),(0,255,0),3)
cv2.line(img,(0,height),(270,360),(0,255,0),3)
cv2.line(img,(width,height),(455,372),(0,255,0),3)

# Retângulo representando a posição desejada (VERMELHO)
cv2.rectangle(img,(0,0),(width,height),(0,0,255),3)
# Apenas para vizualização #

cv2.imshow(img)

img = io.imread("https://i.postimg.cc/gJ4BL7Hn/cards.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Tamanho da carta
width,height = 250,350

# Coordenadas atuais dos 4 vértices
pts1 = np.float32([[276,117],[450,127],[270,360],[455,372]])

# Coordenadas desejadas da projeção
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# Matriz de Transformação de Perspectiva
matrix = cv2.getPerspectiveTransform(pts1,pts2)

# Distorção de Perspectiva
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

print("Imagem com distorção de perspectiva")
cv2.imshow(imgOutput)

img_half = imgOutput[0:350,125:250]
cv2.imshow(img_half)

Img_flip = cv2.flip(img_half, 1)
Img_flip = cv2.flip(Img_flip, 0)
cv2.imshow(Img_flip)

new_img = np.concatenate((Img_flip, img_half), axis=1)
cv2.imshow(new_img)

img1 = io.imread("https://i.postimg.cc/gJ4BL7Hn/cards.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

# Tamanho da carta
width,height = 250,350

# Coordenadas atuais dos 4 vértices
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])

# Coordenadas desejadas da projeção
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

#-----
w1 = (190,10) #esquerda superior
w2 = (352,27) #direita superior
w3 = (160,230) #esquerda inferior
w4 = (310,240) #direita inferior
#-----

# Apenas para vizualização #
# Marcação dos 4 vértices (AZUL)
cv2.circle(img1,w1,2,(255,255,0),5) # Vértice 1
cv2.circle(img1,w2,2,(255,255,0),5) # Vértice 2
cv2.circle(img1,w3,2,(255,255,0),5) # Vértice 3
cv2.circle(img1,w4,2,(255,255,0),5) # Vértice 4
# Apenas para vizualização #

# Marcação das 4 linhas (VERDE)
cv2.line(img1,(0,0),w1,(0,255,0),3)
cv2.line(img1,(width,0),w2,(0,255,0),3)
cv2.line(img1,(0,height),w3,(0,255,0),3)
cv2.line(img1,(width,height),w4,(0,255,0),3)

# Retângulo representando a posição desejada (VERMELHO)
cv2.rectangle(img1,(0,0),(width,height),(0,0,255),3)
# Apenas para vizualização #

cv2.imshow(img1)

img1 = io.imread("https://i.postimg.cc/gJ4BL7Hn/cards.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

#-----
#w1 = (190,10) #esquerda superior
#w2 = (352,27) #direita superior
#w3 = (160,230) #esquerda inferior
#w4 = (300,250) #direita inferior
#-----

# Tamanho da carta
width,height = 250,350

# Coordenadas atuais dos 4 vértices
pts1 = np.float32([w1,w2,w3,w4])

# Coordenadas desejadas da projeção
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# Matriz de Transformação de Perspectiva
matrix = cv2.getPerspectiveTransform(pts1,pts2)

# Distorção de Perspectiva
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

print("Imagem com distorção de perspectiva")
cv2.imshow(imgOutput)

img_half = imgOutput[0:175,0:250]
cv2.imshow(img_half)
print()
Img_flip = cv2.flip(img_half, 0)
Img_flip = cv2.flip(img_half, -1)
cv2.imshow(Img_flip)

print()
new_img = np.concatenate((img_half,Img_flip), axis=0)
cv2.imshow(new_img)

img2 = io.imread("https://i.postimg.cc/gJ4BL7Hn/cards.jpg")
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Tamanho da carta
width,height = 250,350

# Coordenadas atuais dos 4 vértices
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])

# Coordenadas desejadas da projeção
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

#-----
w1 = (7,125) #esquerda superior
w2 = (150,37) #direita superior
w3 = (130,280) #esquerda inferior
w4 = (255,175) #direita inferior
#-----

# Apenas para vizualização #
# Marcação dos 4 vértices (AZUL)
cv2.circle(img2,w1,2,(255,255,0),5) # Vértice 1
cv2.circle(img2,w2,2,(255,255,0),5) # Vértice 2
cv2.circle(img2,w3,2,(255,255,0),5) # Vértice 3
cv2.circle(img2,w4,2,(255,255,0),5) # Vértice 4
# Apenas para vizualização #

# Marcação das 4 linhas (VERDE)
cv2.line(img2,(0,0),w1,(0,255,0),3)
cv2.line(img2,(width,0),w2,(0,255,0),3)
cv2.line(img2,(0,height),w3,(0,255,0),3)
cv2.line(img2,(width,height),w4,(0,255,0),3)

# Retângulo representando a posição desejada (VERMELHO)
cv2.rectangle(img2,(0,0),(width,height),(0,0,255),3)
# Apenas para vizualização #

plt.imshow(img2)

img = io.imread("https://i.postimg.cc/gJ4BL7Hn/cards.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#-----
#w1 = (190,10) #esquerda superior
#w2 = (352,27) #direita superior
#w3 = (160,230) #esquerda inferior
#w4 = (300,250) #direita inferior
#-----

# Tamanho da carta
width,height = 250,350

# Coordenadas atuais dos 4 vértices
pts1 = np.float32([w1,w2,w3,w4])

# Coordenadas desejadas da projeção
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

# Matriz de Transformação de Perspectiva
matrix = cv2.getPerspectiveTransform(pts1,pts2)

# Distorção de Perspectiva
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

print("Imagem com distorção de perspectiva")
cv2.imshow(imgOutput)

img_half = imgOutput[0:175,0:250]
cv2.imshow(img_half)
print()
Img_flip = cv2.flip(img_half, 0)
Img_flip = cv2.flip(img_half, -1)
cv2.imshow(Img_flip)

print()
new_img = np.concatenate((img_half,Img_flip), axis=0)
cv2.imshow(new_img)