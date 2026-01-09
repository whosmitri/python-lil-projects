import smtplib
import email.message

def enviar_email():  
    corpo_email = """
    <p>parágrafo 1</p>
    <p>parágrafo <strong>2</strong> !!</p>
    """

    msg = email.message.Message()
    msg['Subject'] = 'Título do Email (assunto)'
    msg['From'] = 'gmail do remetente'
    msg['To'] = 'gmail do destinatário'
    password = 'senha' 
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email )

    # security settings required by Google
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()

    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('email enviado !!')

enviar_email()
