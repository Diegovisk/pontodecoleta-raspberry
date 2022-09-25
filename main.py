import time
import paho.mqtt.client as paho
from paho import mqtt

# CADA PONTO DE COLETA VAI TER SEU TOPICO. O DESSE SE CHAMA "pontopiloto"
# O SERVER (COMPUTADOR EXTERNO) VAI SE SUBSCREVER EM TODOS OS PONTOS.

# NO MOMENTO, ESTAMOS SEM BROKER, ENTAO ESTAMOS USANDO A VERSAO FREE\
# DO HIVEMQTT, COM AS SEGUINTES VARIAVEIS:
nome_do_broker = "pontodecoleta"
senha_do_broker = "pontodecoleta"
url_da_conexao = "cd65bcd7e6c144ed804c228b2f6cfe7c.s1.eu.hivemq.cloud"
porta = 8883 

# ESSA FUNCAO SERA EXECUTADA TODA VEZ QUE SE CONECTAR NO BROKER
def on_connect(client, userdata, flags, rc, properties=None):
    print("ACK da conexao no topico recebido: %s." % rc)

# ESSA FUNCAO SERA EXECUTADA TODA VEZ QUE ENVIAR ALGO PELO TOPICO
def on_publish(client, userdata, mid, properties=None):
    print("ID da mensagem: " + str(mid))

client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)

client.on_connect = on_connect

# PARA O HIVEMQTT, PRECISA HABILITAR CONEXAO SEGURA PELO PROTOCOLO TLS
# SE CONSEGUIRMOS UM BROKER, ENTAO PODE APAGAR A LINHA DEBAIXO
client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)
# NOME DO BROKER SETADO NO HIVEMQ + PASSWORD
client.username_pw_set(nome_do_broker, senha_do_broker)
# CONEXAO COM O HASH DADO PELO HIVEMQ + PORTA
client.connect(url_da_conexao, porta)

# SETANDO AS FUNCOES QUE CRIAMOS LA NO INICIO 
client.on_publish = on_publish
client.publish("pontos/pontopiloto", payload="arroz", qos=1)

# loop_forever for simplicity, here you need to stop the loop manually
# you can also use loop_start and loop_stop
client.loop_forever()
