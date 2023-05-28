#!C:/Python34/python.exe


import cgi
class Formular_einlesen:
     def __init__ (self):
          self.geschlecht=""
          self.passwort=""
          self.name=""
          self.mail=""
          self.geburtstag=""
          
     def fehler(self):
          print ('Content-Type: text/html')
          print()
          print ('<?xml version="1.0" ?>\
             <!DOCTYPE html>\
            <link rel="stylesheet" type="text/css" href="../Stylesheet.css"/>\
            <head>\
            <meta http-equiv="Content-type" content="text/html; CHARSET=iso-8859-1"/>\
             <title> Fehlermeldung </title>\
              </head>\
              <body>\
              <h1>Fehler!</h1>\
              <h2 class="white">Bitte die Felder Geschlecht, Vorname, Nachname und E-Mail ausfüllen!</h2>\
              <p>\
              <input type="submit" value="Zurück" onclick = "history.back()" />\
              </p>\
              </body>\
              </html>')
     
     def fehler1(self):
             print ("Content-Type: text/html")
             print()
             print ('<?xml version="1.0" ?>\
               <!DOCTYPE html>\
               <link rel="stylesheet" type="text/css" href="../Stylesheet.css"/>\
               <head>\
                <title> Fehlermeldung </title>\
                </head>\
                <body>\
                <h1>Fehler!</h1>\
                <h2 class="white">Die E-Mail-Adressen stimmen nicht überein!</h2>\
                <p>\
                <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                </p>\
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
                <body>\
                <h1>Vielen Dank</h1>\
                <h2 Herzlich willkommen, '+self.anrede+' '+self.name+'! Ihre E-Mail-Adresse ist: '+self.mail+' und Sie haben am:  Geburtstag </h2>\
                <p>\
                <input type="submit" value="Zur&uuml;ck" onclick = "history.back()" />\
                </p>\
                </body>\
                </html>')



     def haupt(self):
          form = cgi.FieldStorage()
          if "Geschlecht" in form:
               self.geschlecht = form["Geschlecht"].value
               if self.geschlecht == "weiblich":
                    self.anrede = "Frau"
               if self.geschlecht == "maennlich":
                    self.anrede = "Herr"
          if "Name" in form:
             self.name=form["Name"].value
          if "Mail" in form:
             self.mail=form["Mail"].value
          
          if  (self.geschlecht=="" or self.mail=="" or self.name==""):
               self.fehler()
              
          else:
              self.anmeldung()
              
objekt=Formular_einlesen()
objekt.haupt()
