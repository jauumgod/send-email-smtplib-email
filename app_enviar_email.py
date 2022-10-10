import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Sua conta foi criada com sucesso!</p>     #email em tag html
    """

    msg = email.message.Message()
    msg['Subject']="Criação de email" #assunto
    msg['From']='joaomkurujao@gmail.com'
    msg['To']='hiasmynstasiak@gmail.com'
    password ='wehngbdbjtiolxrs'
    msg.add_header('Content-Type','text/html')
    msg.set_payload(corpo_email)
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.starttls()
    #login e envio de msg
    s.login(msg['From'],password)
    s.sendmail(msg['From'],[msg['To']],msg.as_string().encode('utf-8'))
    print('Email enviado')
enviar_email()
