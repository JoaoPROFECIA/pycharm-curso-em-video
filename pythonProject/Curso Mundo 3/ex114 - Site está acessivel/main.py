import urllib
import urllib.request


try:
    dados = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print("Deu ruim")
else:
    print("Deu bom")
    print(dados.read())
    dados.close()
    print("Fechou")
