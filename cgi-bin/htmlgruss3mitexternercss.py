#!C:/Python34/python.exe


import cgi
import MySQLdb

db = MySQLdb.connect("localhost","root","","userdaten" )

class Formular_einlesen:
     def __init__ (self):
          self.passwort=""
          self.mail=""
          self.Geburtsdatum=""    


     #MySQL
     def Post(self):
          cursor = db.cursor()
          data=cgi.FieldStorage()
          mail=self.mail
          passw=self.passwort
          datum=self.geburtsdatum

          query = f"INSERT INTO daten (email, password, geburtsdatum) VALUES ('{mail}', '{passw}', '{datum}')"
          cursor.execute(query)
          db.commit()

          import logging

          logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                              filename='app.log')




     def fehler(self):
          print ('Content-Type: text/html')
          print()
          print ('<?xml version="1.0" ?>\
             <!DOCTYPE html>\
               <html>\
               <link rel="stylesheet" type="text/css" href="../Stylesheet.css"/>\
               <body>\
                    <nav class="menu">\
                         <ul>\
                         <li><a href="../Main.html/">Main</a></li>\
                         <li><a href="TEST.html">MEME</a></li>\
                         <li><a href="login.html">Login</a></li>\
                         </ul>\
                    </nav>\
                    <h1 class="fehlermeldung">Etwas ist schiefgelaufen Versuche es erneut</h1>\
                         <button class="buttonlogin">Zurück</button value= "Zurück" onclick = "history.back()" />\
               </body>\
               </html>')
                  
     def anmeldung(self):
              print ('Content-Type: text/html')
              print()
              print('<?xml version="1.0" ?>\
               <!DOCTYPE html>\
               <link rel="stylesheet" type="text/css" href="../Stylesheet.css"/>\
               <head>\
                <title> Vielen Dank </title>\
                </head>\
                <body >\
                <h1>Vielen Dank</h1>\
                <h2> Herzlich willkommen, Ihre E-Mail-Adresse ist: '+self.mail+' und Sie haben am: '+self.geburtsdatum+' Geburtstag. </h2>\
                <h2>Lust auf ein Quiz?</h2>\
                <a href="../Quiz.html">Quiz</a>\
                <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                </body>\
                </html>')
              

     def haupt(self):
          form = cgi.FieldStorage()
          if "Mail" in form:
             self.mail=form["Mail"].value
          if "Geburtsdatum" in form:
               self.geburtsdatum=form["Geburtsdatum"].value
          if "Passwort" in form:
               self.passwort=form["Passwort"].value         
          if  (self.mail=="" or self.passwort==""):
               self.fehler()
          else:
              self.anmeldung()
              self.Post()
          


              
objekt=Formular_einlesen()
objekt.haupt()
