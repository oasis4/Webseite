#!C:/Python34/python.exe


import cgi
class Formular_einlesen:
     def __init__ (self):
          self.geschlecht=""
          self.passwort=""
          self.name=""
          self.mail=""
          
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
          if  (self.geschlecht=="" or self.vorname=="" or self.name=="" or self.mail=="" or self.mailw==""):
               self.fehler()
          elif self.mail != self.mailw:
               self.fehler1()
          else:
              print ('Content-Type: text/html')
              print()
              print( '<!DOCTYPE html>\
                 <link rel="stylesheet" type="text/css" href="../cssclasse.css"/>\
                 <head>\
                 <meta http-equiv="Content-type" content="text/html; CHARSET=iso-8859-1"/>\
                 <title> Anmeldung erfolgreich</title>\
                 </head>\
                 <body>\
                 <h1>Vielen Dank für Ihre Daten!</h1>\
                 <div class="white">Herzlich willkommen, '+self.anrede+' '+self.name+'! Ihre E-Mail-Adresse ist: '+self.mail+' </div>\
                  </body>\
                  </html>')

objekt=Formular_einlesen()
objekt.haupt()
