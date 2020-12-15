## PYTHON AND DJANGO API REST

Desafio de um API REST de Produtos Favoritos, no qual é possível criar clientes e produtos, sendo que cada cliente pode adicionar produtos a sua lista de produtos favoritos sem repeti-los

-Banco de dados: Postgresql

-Pode utilizar o Postman Também

## Processo de Instalação 

1-Clonar o repositório

2-Ativar o venv (VsCode): venv/Scripts/activate.ps1 

4-Instalar os módulos: pip install -r requirements.txt

5-Migrações Models: python manage.py makemigrations

6-Migrações: python manage.py migrate

7-Cria um super usuário: python manage.py createsuperuser

9-Rodar a aplicação: python manage.py runserver

** Se der erro : python -m pip install --upgrade pip


## Processo Inicial 

---Get /AUTHENTICATION

Através do login e password do superuser, pode ser visualizado os clientes.

Os Produtos podem ser vistos pelos clientes, porém não podem ser alterados.

  login: <admin-name>,
  
  password: <password>

#### Rodar API

venv/Scripts/activate.ps1 

cd magalu

python manage.py runserver

http://127.0.0.1:8000/


## Como utilizar a API

#Endpoint lista os clientes e também cria cada cliente.
Post /client     

{

    "count": 5,
    "next": null,
    "previous": "http://127.0.0.1:8000/clients",
    "results": [
        {
            "id": 4,
            "name": "Gustavo",
            "email": "gustavo@exemplo.com",
            "favorite": []
        },
        {
            "id": 5,
            "name": "Manuela",
            "email": "manuela@exemplo.com",
            "favorite": []
        }
}

#Endpoint mostra as páginas e os clientes.
---Get /clients?page=2     

{

    "count": 5,
    "next": null,
    "previous": "http://127.0.0.1:8000/clients",
    "results": [
        {
            "id": 5,
            "name": "Manuela",
            "email": "manuela@exemplo.com",
            "favorite": []
        },
        {
            "id": 6,
            "name": "lopes",
            "email": "lopes@exemlo.com",
            "favorite": []
            
        }
    ]
}

#Endpoint atualiza o Cliente.
---Puth - Path /client/2 

{

    "id": 2,
    "name": "Regina",
    "email": "regina@exemplo.com",
    "favorite": []
    
}

 #Endpoint exclui cliente
---Delete /client/2    


  { 
  
    "detail": "Not found."
    
    }

#O endpoint informar o cliente e se tiver algum ou alguns favorite_product (sem repetição de produtos), ira retornar as informações no                                 favorite, senão o campo fica vazio. 
---Get /client/1         

    {
    "id": 1,
    "name": "Patricia",
    "email": "Patricia@exemplo.com",
    "favorite": []
 }
{

    "id": 1,    
    "name": "Patricia",    
    "email": "Patricia@exemplo.com",    
    "favorite": [
    
        {
            "id": 1,
            "title": "Nescau",
            "price": "5.00",
            "image": "http://127.0.0.1:8000/product/nescau.jfif",
            "brand": "Nestle",
            "reviewScore": "9.0"
        },
        {
            "id": 2,
            "title": "Caixa de Bombom",
            "price": "10.00",
            "image": "http://127.0.0.1:8000/product/1417116105_1GG.png",
            "brand": "Garoto",
            "reviewScore": "9.6"
        }
    ]
}

