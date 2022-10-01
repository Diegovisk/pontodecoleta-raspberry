# PONTO DE COLETA - RASPBERRY 
O raspberry envia mensagens pelo broker até o servidor. 
O que o servidor retornar, ele exibe nas telas LCDs ou abre/fecha a tranca.

Caso alguma porta esteja em uso, mate-a com: 
```console
sudo fuser -k <PORT>/tcp
```

## Deploy
Para fazer o os saber quais são as variáveis do ambiente:
```console
export $(cat config/.env | xargs) 
```
Para rodar o servidor:
```console
virtualenv venv --python=python3.9 
```
```console
source ./venv/bin/activate
```
```console
pip3 install -r requirements.txt
```

