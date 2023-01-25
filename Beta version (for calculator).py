
#Créé pour TI-CE 83 edition python
#Par Théo Tchilinguirian

from math import *

print("""Bienvenue sur CalTrino
Version 1.0.2""")
def Trinôme(a=0, b=0, c=0):
    print("Calcul Trinôme Second Degré")
    print("Entrez les valeurs de a, b et c du polynome ax² + bx + c: ")
    a = round(float(input("Valeur de a: ")), 2)
    b = round(float(input("Valeur de b: ")), 2)
    c = round(float(input("Valeur de c: ")), 2)

    Signe1 = ""
    Signe2 = ""

    if b > 0:
        Signe1 = "+"
    if c > 0:
        Signe2 = "+"
    if b == 0 or -0:
        Signe1 = "+"
    if c == 0 or -0:
        Signe2 = "+"
    if b < 0:
        Signe1 = ""
    if c < 0:
        Signe2 = ""

    print("f(x): {}x²{}{}x{}{} = 0".format(a, Signe1, b, Signe2, c))
    print("""on a donc:
    a = {}
    b = {}
    c = {}""".format(a, b, c))

    SigneAlpha = ""
    SigneBeta = ""

    Alpha = round(-b/2*a, 2)
    Delta = round(b**2 - 4*a*c, 2)
    Beta = round(Delta / 4*a, 2)

    if -Alpha > 0:
        SigneAlpha = "+"
    if Beta > 0:
        SigneBeta = "+"
    if -Alpha == 0 or -0:
        SigneAlpha = "+"
    if Beta == 0 or -0:
        SigneBeta = "+"
    if Alpha < 0:
        SigneAlpha = ""
    if Beta < 0:
        SigneBeta = ""

    print("""On cherche la Forme Canonique:
        on a:
        a = {}
        b = {}
        c = {}

        Alpha = -b/2a
              = {}

        Delta = b² - 4ac
              = {}

        Beta = Delta/4a
              = {}

     ou Beta = f(Alpha)
                = {}""".format(a, b, c, Alpha, Delta, Beta, Beta))
    print("-------------------------------")
    print("""On a donc:
    Alpha = {}
    Delta = {}
    Beta = {}""".format(Alpha, Delta, Beta))

    print("-------------------------------")

    print("""   f a donc pour forme canonique:
    a(x - Alpha) + Beta
    {}(x{}{}){}{}""".format(a, SigneAlpha, -Alpha, SigneBeta, Beta))

    print("-------------------------------")

    print("On cherche à Résoudre l'équation {}x² {} {}x {} {} = 0 :".format(a, Signe1, b, Signe2, c))
    print("On cherche à calculer Delta: (ou alors on dispose déja de Delta)")
    print("")
    print("Delta = b² - 4ac")
    print("      = {}² - 4 x {} x {}".format(b, a, c))
    print("      =", Delta)
    print("")

    if Delta < 0:
        print("Delta < 0: f n'a pas de racine")
    if Delta == 0:
        print("-------------------------------")
        print("""Delta = 0: f a une racine :
        x0 = Alpha = -b/2a
        x0 = {}/2{}
        S = [{}]""".format(-b, a, round(Alpha, 2)))
    if Delta > 0:
        print("-------------------------------")
        print("""Delta > 0: f a deux racines :
		x1 = (-b - sqrt(Delta))/2a   et x2 = (-b + sqrt(Delta))/2a
		x1 = ({} - sqrt({}))/2 x {}     et x2 = ({} + sqrt({}))/2 x {}
		x1 = {}/{}
 et x2 = {}/{}
    x1 = {}
 et x2 = {}""".format(-b, Delta, a, -b, Delta, a, round(-b - sqrt(Delta), 2), round(2*a, 2), round(-b + sqrt(Delta), 2), round(2*a, 2), round(-b - sqrt(Delta) / 2*a, 2), round(-b + sqrt(Delta) / 2*a)))

        x1 = -b - round(sqrt(Delta), 2) / 2*a
        x2 = -b + round(sqrt(Delta), 2) / 2*a
        if x1 < x2:
            print("""
			S = [{}, {}]""".format(round(x1, 2), round(x2, 2)))
        if x2 < x1:
            print("""
			S = [{}, {}]""".format(round(x2, 2), round(x1, 2)))


Trinôme()

print("-------------------------------")

while True:
	VarRecommencer = input("Recommencer? o/n: ")
	if VarRecommencer == 'o':
		Trinôme()
	if VarRecommencer == 'n':
		break
	else:
		print("ecris 'o' pour recommencer ou 'n' pour arreter")
		continue
