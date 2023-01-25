#Pas plus de 31 caracteres affichés visibles par ligne de print (print inclu)
from math import *

def Calcul(a = 0, b = 0, c = 0):

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

    Choix = int(input("""Faites un choix:
		-Alpha: 			      1
		-Beta: 				     2
		-Delta: 			      3
		-forme canonique:	 4
		-Racine x0: 		    5
		-Racine x1 et x2: 	6
		-forme factorisée:	7
		-Tableau de signe:	8
		-Leçon:         	  9
		-Equation mx² + (): 10
									"""))

    print("f(x): {}x²{}{}x{}{} = 0".format(a, Signe1, b, Signe2, c))
    print("""on a donc:
    a = {}
    b = {}
    c = {}""".format(a, b, c))

    print("-------------------------------")

    SigneAlpha = ""
    SigneBeta = ""

    Alpha = round(-b/(2*a), 2)
    Delta = round(b**2 - ((4*a)*c), 2)
    Beta = round(a*Alpha**2+b*Alpha + c, 2)

    if Delta  > 0:
        x1 = -b - round(sqrt(Delta), 2) / 2*a
        x2 = -b + round(sqrt(Delta), 2) / 2*a

    x0 = Alpha
    
    if -Alpha > 0:
        SigneAlpha = "+"
    if Beta > 0:
        SigneBeta = "+"
    if -Alpha == 0 or -0:
        SigneAlpha = "+"
    if Beta == 0 or -0:
        SigneBeta = "+"
    if -Alpha < 0:
        SigneAlpha = ""
    if Beta < 0:
        SigneBeta = ""

    if -4*a*c > 0:
    	Signe4ac = "+"
    if -4*a*c == 0 or -0:
    	Signe4ac = "+"
    if -4*a*c < 0:
    	Signe4ac = ""

    if Choix == 1:
	    print("""Alpha = -b/2a
    	= {}/{}
Alpha = {}""".format(-b, 2*a, round(-b/(2*a), 2)))
	
    if Choix == 2:
	    print("""Beta  = f(Alpha)
	    = {}*{}²{}{}*{}{}{}
 Beta = {}""".format(a, Alpha, Signe1, b, Alpha, Signe2, c, Beta))
	
    if Choix == 3:
	    print("""Delta = b² - 4ac
	    = {} {} {}
Delta = {}""".format(b**2, Signe4ac, -4*a*c, Delta))
	
    if Choix == 4:
	    print("""On a:
    Alpha = {}
    Beta = {}""".format(Alpha, Beta))

	    print("""f a donc pour forme canonique:
    a(x - Alpha) + Beta
    {}(x{}{}){}{}""".format(a, SigneAlpha, -Alpha, SigneBeta, Beta))

    if Choix == 5:
        print("""Delta = 0: f a une racine :
    x0 = Alpha = -b/2a
    x0 = {}/2*{}
     S = ({})""".format(-b, a, round(Alpha, 2)))

    if Choix == 6:
        print("""Delta > 0: f a deux racines :
		x1 = (-b - sqrt(Delta))/2a   et x2 = (-b + sqrt(Delta))/2a
		x1 = ({} - sqrt({}))/2 * {}
	 et x2 = ({} + sqrt({}))/2 * {}
		x1 = {}/{}
 et x2 = {}/{}
    x1 = {}
 et x2 = {}""".format(-b, Delta, a, -b, Delta, a, round(-b - sqrt(Delta), 2), round(2*a, 2), round(-b + sqrt(Delta), 2), round(2*a, 2), round(-b - sqrt(Delta) / 2*a, 2), round(-b + sqrt(Delta) / 2*a, 2)))
        print("-------------------------------")
        x1 = -b - round(sqrt(Delta), 2) / 2*a
        x2 = -b + round(sqrt(Delta), 2) / 2*a
        if x1 < x2:
            print("""S = ({}, {})""".format(round(x1, 2), round(x2, 2)))
        if x2 < x1:
            print("""S = ({}, {})""".format(round(x2, 2), round(x1, 2)))

    if Choix == 8:

        if a > 0:
        	Symba = ">"
        	Signe3 = "+"
        if a < 0:
        	Symba = "<"
        	Signe3 = "-"
        if Signe3 == "+":
        	Signe4 = "-"
        if Signe3 == "-":
        	Signe4 = "+"
        	
        if Delta > 0:
            print("""Le tableau de signe de la
    		fonction f est:
    		pour a={}{}0:
   x 		   {}   {}
------|-inf--|------|--+inf|
 f(x) |      |	    |	    |
   	 |   {}  0	 {}  0  {}   |
   	 |      |	    |	    |""".format(a, Symba, round(x1, 2), round(x2, 2), Signe3, Signe4, Signe3))
        if Delta == 0:
            print("""Le tableau de signe de la
    		fonction f est:
    		pour a={}{}0:
   x		    {}
  ----|-inf---|+inf---|
 f(x) |	     |	     |
	    |	 {}   0   {}   |
	    |	     |	     |""".format(a, Symba, round(x0, 2), Signe3, Signe3))

        if Delta < 0:
            print("""Le tableau de signe de la
    		fonction f est:
    		pour a={}{}0:
   x
------|-inf-----+inf|
 f(x) |	     	    |
	    |	    {} 	   |
	    |	     	    |""".format(a, Symba, Signe3))
	
    if Alpha > 0:
	    Signex0 = "+"
    if Alpha == 0 or -0:
    	Signex0 = "+"
    if Alpha < 0:
    	Signex0 = ""

    if Delta > 0:
    	if x1 > 0:
    		Signex1 = "+"
    	if x2 > 0:
    		Signex2 = "+"
    	if x1 == 0 or -0:
    		Signex1 = "+"
    	if x2 == 0 or -0:
    		Signex2 = "+"
    	if x1 < 0:
    		Signex1 = ""
    	if x2 < 0:
    		Signex2 = ""
    if Choix == 7:
    	if Delta == 0:
    		print("""pour Delta = 0:, f(x) admet une forme factorisée:
    		a(x - x0)²
    		{}(x {} {})²""".format(a, Signex0, x0))
    	if Delta > 0:
    		print("""pour Delta > 0, f(x) admet une forme factorisée:
    		a(x - x1)(x - x2)
    		{}(x {} {})(x {} {})""".format(a, Signex1, round(x1, 2), Signex2, round(x2, 2)))

    if Choix == 9:
    	print("""Pour résoudre n'importe quelle équation,
    	on fait:
    	-passer tout a gauche
    	-factoriser
    	-Calculer Delta et les Solutions

    	on a 3 méthodes pour calculer f(x) = y:
		trouver la plus appropriée:
		ax² + bx + c
		a(x - Alpha)² + Beta (on a (Alpha ; Beta)Sommet dans le graphique)
		a(x - x1)(x - x2)    (on a x1, x2 sur le graphique(y = 0)

	Pour tracer une droite affine (ax + b):
	on part de l'ordonné b
	si a>0: on avance de 1 et on monte de a
	si a<0: on avance de 1 et on descend de a

	pour trouver a (sauf pr parabole):
	y/x
	c a d: si on avance de 1 vers haut, et 2 vers droite:
	a = 1/2

	autre méthode:
	utiliser la forme dvp/fact:
	si on a le sommet, on a la forme
	canonique et on passe tout à droite sauf a:
	ex: on a f(1) = -2 et sommet = (-3;2):
	a(1+3)²+2=-2 a(1+3)²=-4 16a=-4 a=-1/4

	On peut faire pareil avec la forme fact x1 et x2.
	Il faut donc juste un point et une de ces 2 formes.
	on peut aussi calculer b et c vu qu'on a a:
	Alpha = -b/a <--
	Beta = f(Alpha)

	Si on a (x+2)(ax²+bx+c):
	on dvp
	on calcule a puis b puis c grace
	à l'énoncé""")
    
    if Choix == 10:
        print("""Si mx² + (3 - m)x + 1 = 0:
	on calcul Delta b² - 4ac
	(3 - m)² - 4m
	on identifie une identité remarquable
	9 - 6m + m² - 4m
	m² - 10m + 9
	On voit une nouvelle equation
	On recalcule Delta
	100 - 36
	64""")

    print("-------------------------------")

    print("""Utilisez 2nd + touches
	fléchées pour naviguer""")

Calcul()

print("-------------------------------")

while True:
	VarRecommencer = input("Recommencer? o/n: ")
	if VarRecommencer == 'o':
		Calcul()
	if VarRecommencer == 'n':
		break
	else:
		print("ecris 'o' pour recommencer ou 'n' pour arreter")
		continue
