"""
processo de 3 partes:
- pegar a informação que você quer
- enviar um aviso (email, por exemplo)
"""

# bibliotecas
import requests
import smtplib
import email.message

# pegar a informação

requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
requisicao_dicionario = requisicao.json()
cotacao = float(requisicao_dicionario['USDBRL']['bid'])


# enviar um aviso (email)
# enviar apenas quando a ctação do dólar for menor que 5.20

def enviar_email(cotacao):
    corpo_email = f"""
    <p>Dólar está abaixo de R$5.20</p>
    <p>Cotação atual simpleficada: <strong>R${cotacao:.2f}</strong></p>
    <p>Cotação atual detalhada: <strong>R${cotacao}</strong></p>
    """

    msg = email.message.Message()
    msg['Subject'] = 'Queda do Dólar Hoje'
    msg['From'] = 'gmail do remetente'
    msg['To'] = 'gmail do destinatário'
    password = 'senha de app única' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    # security settings required by Google
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('email enviado !!')

if (cotacao < 5.20):
    enviar_email(cotacao=cotacao)
else:
    print(f'Cotação Atual: \n* Simplificada: R${cotacao:.2f} \n* Detalhada: R${cotacao}')
