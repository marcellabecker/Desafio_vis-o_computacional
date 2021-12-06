# Desafio_visão_computacional

# Objetivo
Este repositório tem o objetivo de armazenar a solução do desafio de visão computacional proposto no Centro de Competência em Robótica do SENAI CIMATEC.

# Desafio
O desafio consiste em realizar transformações de modo a corrigir determinada imagem. Esta imagem consiste em um conjunto de cartas em perspectiva e sob oclusão. Deste modo, para resolver o desafio, as castas devem ser apresentadas na forma retangular e sem oclusão.

![cards](https://github.com/marcellabecker/visao_computacional/img/cards.jpg)

# Desenvolvimento

Após a importação da imagem, por meio do método imread, é colocado os pontos que definem a região em que será realizada a transformação. Estes pontos são pares ordenados com a localização dos pixels associados a imagem.

$cv2.circle(img,(276,117),2,(255,255,0),5) # Vértice 1
cv2.circle(img,(450,127),2,(255,255,0),5) # Vértice 2
cv2.circle(img,(270,360),2,(255,255,0),5) # Vértice 3
cv2.circle(img,(455,372),2,(255,255,0),5) # Vértice 4$

![ROI](https://github.com/marcellabecker/visao_computacional/img/ROI.png)

# Resultados

![ouros](https://github.com/marcellabecker/visao_computacional/img/ouros.png)

![paus](https://github.com/marcellabecker/visao_computacional/img/paus.png)

![vermelha](https://github.com/marcellabecker/visao_computacional/img/vermelha.png)