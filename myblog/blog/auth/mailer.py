from flask_mail import Mail, Message
mail =Mail()


def sendMsg(subject,sender_address,reciver,msgbody,htmlMsg):
	msg = Message(subject, sender=sender_address, recipients=[reciver])
	msg.body = msgbody
	msg.html = htmlMsg
	mail.send(msg)
