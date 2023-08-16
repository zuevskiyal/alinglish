from flask import Flask, render_template,request
import requests
import smtplib
app = Flask(__name__)
myemail = 'zuevskiyal@mail.ru'
password = 'gfZqPcGBQJ2eCM8yWUCv'

@app.route('/',methods = ["GET","POST"])
def home():
    if request.method == "POST":
        data = request.form
        send_message(data['name'], data["phone"], data["email"], data["message"])
        return render_template('index.html', msg_sent=True)
    return render_template('index.html', msg_sent=False)

def send_message(pname, pphone, pemail, pmessage):
    email_meassage = f"Subject:New message\n\nName:{pname}\n Email: {pemail}\n Phone : {pphone}\nMessage : {pmessage}"
    with smtplib.SMTP('smtp.mail.ru', port=587) as connection:
        connection.starttls()
        connection.login(user=myemail, password=password)
        connection.sendmail(myemail,myemail,email_meassage)


if __name__ == "__main__":
    app.run(debug=True)



