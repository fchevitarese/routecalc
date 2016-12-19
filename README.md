## **RouteCalc** ##
O projeto foi feito utilizando [Django 1.10](https://www.djangoproject.com/).

Apaixonado por Django, fiz utilizando o mesmo pois é minha ferramenta de trabalho há anos!

Por simplicidade, estou utilizando o SQLite para armazenar os dados com os pontos.

O initial.json é um dump das coordenadas que foram passadas no exemplo no email.

Como nome no mapa, utilizei a sigla do meu estado natal, Minas Gerais, portanto MG.


**Instalação**:

>     git clone https://bitbucket.org/frederico_chevitarese/routecalc/admin
>     pip install -r requirements.txt
>     python manage.py migrate
>     python manage.py loaddata initial.json
>     python manage.py runserver

**Docker**

O projeto tem disponível 2 Dockerfiles diferentes, para python3 e python2.

Dockerfile-python2
Dockerfile-python3

No arquivo docker-compose.yaml, estou utilizando a versão com python2.

Para utilizar python3, é necessário configurar a diretiva "dockerfile" apontando para o dockerfile desejado:


 1. Python2: "dockerfile: Dockerfile-python2"
 2. Python3: "dockerfile: Dockerfile-python3"


**Build**:

>  docker-compose build
>  docker-compose up


 **Acesso**:
    A api está na raiz do projeto, portanto:
    http://localhost:8000/


 **Calculando frete:**
    Faça um **GET** passando os parâmetros necessários para o cálculo na url.


* nome: Nome do mapa;
* origem: Ponto de origem;
* destino: Ponto de destino;
* autonomia: Autonomia do veículo;
* preco: Preço do combustível;


**URL de exemplo:**

    http://localhost:8000/api/rotas/menor_frete/?nome=mg&origem=a&destino=d&autonomia=10&preco=2.50


**Padrão de retorno:**
    O get na url acima deverá devolver o seguinte json:

```
#!json

{
        "nome": "MG",
        "origem": "A",
        "destino": "D",
        "autonomia": 10,
        "preco": 2.5,
        "valor_frete": 6.25,
        "caminho": "['A', 'B', 'D']",
        "distancia": 25
    }

```


* **Ponto ou mapa inexistente:**
    Caso passe um mapa ou coordenada inexistente, receberá a mensagem de erro:

```
#!json

 {
        "result": "Rota não encontrada."
 }
```