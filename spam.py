import smtplib
spam = input('Enter email to be spammed: ')
msg = input('Enter The Message to be spammed: ')
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("python.bot75@gmail.com","adyaesziprmhepwg")
server.sendmail("python.bot75@gmail.com",spam,msg)
server.close()
print()