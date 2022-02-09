#!/usr/bin/env python
# coding: utf-8

# # Funksjoner
# 
# ```{admonition} Læringsutbytte
# Etter å ha arbeidet med dette temaet, skal du kunne:
# 1. bruke funksjoner til å strukturere og gjenbruke kode.
# 2. forklare hva som menes med globale og lokale variabler.
# ```
# 
# ## Definisjon
# I tillegg til  innebygde funksjoner i Python som _print_ og _input_ kan vi lage funksjoner selv. Dette kan være svært nyttig fordi det kan gjøre programmet mer oversiktlig og håndterbart. I tillegg er det nyttig med funksjoner når vi skal gjøre samme ting flere ganger. Si at vi for eksempel har en vilkårlig matematisk funksjon $f(x) = x^2 + x - 5$. Dersom vi vil regne ut $f(x)$ for alle heltallsverdier av $x$ mellom 1 og 50, kan vi gjøre dette med funksjoner. Først definerer vi funksjonen:

# In[6]:


def f(x):
    return x**2 + x - 5


# Vi definerer her en funksjon med kodeordet _def_ og gir den et funksjonsnavn, her _f_. Deretter spesifiserer vi hva inn-verdien/variabelen til funksjonen skal hete i parentes. Her kaller vi den _x_. I programmering kaller vi en slik størrelse for en _parameter_. Gitt én verdi av _x_, skal funksjonen _returnere_ (spesifisert ved _return_-kommandoen) en funksjonsverdi. Legg merke til at syntaksen er ganske lik vilkår (if-tester), while- og for-løkker, med et kolon etter funksjonsnavnet og innrykk på alt som tilhører funksjonen. 
# 
# Vi får derimot ikke noe output av å definere en funksjon. For å få et output, må vi bruke (vi sier også "kalle på") funksjonen:

# In[7]:


funksjonsverdi = f(2) # Kaller på funksjonen
print(funksjonsverdi)

# Eller
print(f(2))           # Kaller på funksjonen inni en print-funksjon


# 
# ```{admonition} Underveisoppgave
# :class: tip
# Lag en Python-funksjon som representerer den matematiske funksjonen $f(x) = \frac{-x}{2} + \sqrt{x}$. Lag ei løkke som skriver ut 100 ulike funksjonsverdier.
# ```
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# import numpy as np
# 
# def f(x):
#     return  -x/2 + np.sqrt(x)
#     
# for x in range(100):
#     print(f(x))
# ```
# ````
# 
# Vi kan også lage funksjoner uten returverdi, for eksempel funksjoner som skriver ut noe:

# In[8]:


# Definerer to funksjoner
def f(x):
    print(x**2 + x - 5)
    
def gratulerer(navn):
    print("Gratulerer med dagen,", navn)

# Kaller på funksjonene
f(2)
gratulerer("Silje")


# Her ser vi at vi ikke trenger å skrive _print_ når vi kaller på funksjonene. Dette ser da enda enklere ut enn å bruke retur-verdier, så hvorfor bruker vi _return_ i det hele tatt?
# 
# Det er faktisk bedre å bruke return enn print, der det er mulig. Hvis vi for eksempel er interessert i å gjøre noe annet med funksjonsverdiene enn å printe dem, må vi ha konkrete verdier å jobbe med. La oss si at vi ønsker å finne differansen mellom to funksjonsverdier. Hvis vi skal regne med funksjonsverdier, må vi ha en returverdi. Det fungerer nemlig ikke å trekke fra hverandre to print-funksjoner. Eksempelet nedenfor illustrerer dette.

# ````{panels}
# :column: col-6
# :card: border-2
# :header: bg-success
#         
# Riktig
# ^^^
# ```{code-block} Python
# def f(x):
#     return x**3 - 1/x
#     
# print(f(3) - f(1))
# ```
# ---
# :header: bg-danger
# Feil
# ^^^
# Følgende kode vil gi feilmelding:
# 
# ```{code-block} Python
# def f(x):
#     print(x**3 - 1/x)
#     
# f(3) - f(1)
# ```
# ````
# 
# Vi kan også representere matematiske formler som Python-funksjoner, for eksempel slik:

# In[13]:


import numpy as np

def areal_sirkel(r):
    A = np.pi*r**2
    return A

def volum_sylinder(r, h):
    V = np.pi*r**2*h
    return V


# Vi kan også skrive _np.pi\*r\*\*2_ og _np.pi\*r\*\*2\*h_ direkte etter return i funksjonene ovenfor, istedenfor å gjøre det på to linjer. Dette er litt smak og behag, men ofte kan det være mer oversiktlig å gjøre ting på flere linjer enn på én. Dessuten kan man skrive formelen direkte slik den forekommer i matematikken.
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Volumet til ei kule er gitt ved $\frac{4}{3}\pi r^3$. Lag en funksjon som beregner dette volumet og finner differansen mellom volumet til ei kule med radius 10 og ei kule med radius 5.
# ```
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# import numpy as np
# 
# def volum_kule(r):
#     V = (4/3)*np.pi*r**3
#     return V
#     
# volumforskjell = volum_kule(10) - volum_kule(5)
# ```
# ````
# 
# Her ser vi også at den siste funksjonen tar to parametre. Det er mulig å bruke så mange parametre i en funksjon som du ønsker. Det går også an å lage funksjoner uten parametre, for eksempel slik:

# In[20]:


def hei():
    print("Hei på deg!")
    
hei()


# ## Parameternavn
# La oss se på et eksempel der vi kaller på en funksjon på tre måter.

# In[18]:


def fart(s, t):
    v = s/t
    return v

# Funksjonskall 1
s = 10 # Strekning i meter
t = 2  # Tid i s
print("Farten er", fart(s, t), "m/s.")

# Funksjonskall 2
strekning = 10
tid = 2
print("Farten er", fart(strekning, tid), "m/s.")

# Funksjonskall 3
print("Farten er", fart(10, 2), "m/s.")


# Vi ser at vi får samme output for alle funksjonskallene. Vi trenger ikke å definere variabler før vi setter dem inn i funksjonen, så funksjonskall 3 er kanskje det enkleste. Men hvis vi for eksempel skal bruke verdien for tid flere steder, kan det være lurt å ha det som en egen variabel. Denne variabelen kan vi kalle hva vi vil, for den blir uansett overført til variabelen _t_ inni funksjonen. Så om vi kaller variablene for strekning og tid eller s og t, har ingenting å si. Inni funksjonen blir likevel verdien til _strekning_ overført til variabelen _s_ og variabelen _t_ får verdien til _tid_.

# ## Funksjoner med flere returverdier
# I motsetning til funksjoner i matematikk kan en funksjon i programmering ha flere retur-verdier. Disse kan vi tilordne til variabler adskilt med komma, som vist nedenfor.
# 
# <iframe src="https://trinket.io/embed/python3/847ba92c1d" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# ```{admonition} Underveisoppgave
# :class: tip
# Forklar hvordan programmet ovenfor fungerer. Modifiser programmet slik at det også returnerer renta, og skriv ut "Det tar {tid} år før du har {penger} kroner i banken med en rente på {renter*100} prosent."
# ```

# ## Lokale og globale variabler
# 
# Hva skjer hvis vi ikke returnerer verdier i funksjonen ovenfor? Vil vi uansett kunne printe renta og antallet år? La oss undersøke dette.

# In[1]:


def penger_i_banken(startkapital, sluttkapital, renter):
    kapital = startkapital
    år = 0
    while kapital <= sluttkapital:
        kapital = kapital + kapital*renter
        år = år + 1
    return kapital

penger = penger_i_banken(1000, 3000, 0.01)
print("Det tar", år, "år før du har", round(penger,2), "kroner med en rente på", renter*100, "prosent")


# Her får vi visst en feilmelding, selv om vi klart kan se at "år" er definert som en variabel inni funksjonen. Dette handler om at alle variabler som defineres i en funksjon, kun er tilgjengelig inni denne funksjonen. De kalles derfor _lokale_ variabler. Variabler som er definert utenfor funksjoner, kaller vi da for _globale_ variabler. Disse er tilgjengelig både inni og utenfor en funksjon. Her er to eksempler som viser dette:

# In[25]:


def funksjon():
    print(a)

a = "Her er jeg!"

funksjon()
print(a)  # Skriver ut den globale variabelen a


# In[36]:


def funksjon():
    b = "Her er jeg!" # b defineres lokalt inni funksjonen
    print(b)

funksjon()
print(b) # Prøver å skrive ut den lokale variabelen. Vi får dermed en feilmelding


# Vi kan gjøre en lokal variabel til en global variabel, dersom vi trenger det. Dette er ikke vanlig så vanlig å gjøre, men vi kan gjøre det slik:

# In[37]:


def masseenergi(m):
    global c
    c = 3E8 # lyshastigheten i m/s
    E = m*c**2
    return E

print("Energien til legemet er:", masseenergi(1), "joule.")
print("Lysets hastighet i vakuum:", c, "m/s.")


# ## Oppgaver
# 
# ````{admonition} Oppgave 5.1
# :class: tip
# Forklar hvordan programmet nedenfor fungerer.
# ```{code-block} Python
# def f(x):
#     return x + 1
# 
# addisjon = f(1) + f(3)
# subtraksjon = f(1) - f(3)
# 
# print(addisjon, subtraksjon)
# ```
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Vi definerer først en funksjon _f_ som skal returnere funksjonsverdien _x + 1_. Deretter kaller vi på (bruker) funksjonen ved å beregne summen av _f(1)_ og _f(3)_ og differansen mellom de samme funksjonsverdiene. Da henter programmet informasjon fra funksjonen ovenfor, og beregner slik: _addisjon = (1 + 1) + (3 + 1) = 6_ og _subtraksjon = (1 + 1) - (3 + 1) = -1_. Resultatene fra dette skrives så ut.
# ````
# 
# ```{admonition} Oppgave 5.2
# :class: tip
# I programmet nedenfor definerer vi en funksjon som regner ut volumet til en sylinder. Lag en annen funksjon i samme program som regner ut volumet til ei kule.
# 
# ($V_{kule} = \frac{4}{3}\pi r^3$)
# 
# <iframe src="https://trinket.io/embed/python3/030617648f" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# from numpy import pi
# 
# def volum_kule(r):
#     V = 4/3*pi*r**3
#     return V
# 
# # Tester funksjonen
# print(volum_kule(2))
# ```
# ````
# 
# ````{admonition} Oppgave 5.3
# :class: tip
# Hvert program i denne oppgava inneholder noen feil. Finn feilene og rett på dem slik at programmene kan kjøres korrekt.
# 
# 1. Funksjonen skal regne ut $f(x) = \frac{1}{2x} + 1$ og returnere svaret. I programmet skal funksjonen kalles på for $x = 4$:
# 
# ```{code-block} Python
# def f(x):
#     1/2*x + 1
# 
# print("f(x) = ",f(x))
# ```
# 2. Programmet ber brukeren om å skrive en verdi for _x_ og regner ut $f(x) = 3x + \cos(x)$:
# 
# ```{code-block} Python
# def f(x):
# return 3x + cos(x)
# 
# y = input("Skriv inn verdi for x i radianer: ")
# print("f(x) =",f(y))
# ```
# 
# 3. Programmet skal skrive ut funksjonsverdien  _G(1)_.
# 
# ```{code-block} Python
# def G(t):
#     a = t**2 - 2
#     return a
# 
# t = 1
# print(a)
# ```
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# 1. Uttrykket $1/2*x + 1$ regner ut $f(x) = x + 1$, og ikke den ønskede funksjonen. For at programmet skal regne ut hva _x_ blir i den ønskede funksjonen, må parentes brukes i uttrykket for nevneren. Variabelen _x_ er heller ikke definert. Variabelen kan settes til å være lik 4. Vi kan også kalle funksjonen direkte med f(4).
# ```{code-block} Python
# def f(x):
#     return 1/(2* x) + 1
# print("f(x) = ",f(4))
# ```
# 
# 2. Her må cosinus importeres fra et passende bibliotek. Vi må også ha et innrykk på _return_ i $f(x)$, fordi _return_ tilhører funksjonen. Leddet $3x$ må omskrives til $3*x$. Til slutt må variabelen $y$ omgjøres til float for at programmet skal kunne gjøre flytallsoperasjoner på den gitte verdien fra brukeren.
# ```{code-block} Python
# from numpy import cos
# def f(x):
#     return 3*x + cos (x)
# y = float(input(" Skriv inn verdi for x i radianer: "))
# print("f(x) =",f(y))
# ```
# 
# 3. For å finne hva funksjonsverdien til _G_, må vi huske å _kalle på_ funksjonen:
# ```{code-block} Python
# def G(t):
#     a = t**2 - 1
#     return a
# t = 1
# print(G(t))
# ```
# ````
# 
# ````{admonition} Oppgave 5.4
# :class: tip
# Lag et program eller flere programmer som bruker funksjoner til å regne ut:
# 1. Arealet til en sirkel.
# 2. Radius til en sirkel gitt arealet.
# 3. Omkretsen til en sirkel.
# 4. Volumet til ei kule.
# 5. Overflatearealet til ei kule.
# 
# Du kan lage en enkel versjon først uten funksjoner. Lag så en versjon som inneholder funksjoner av hver av formlene. Ikke ta input fra brukeren, men sett verdiene direkte inn i funksjonskallene.
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# from numpy import pi
# 
# # 1
# def sirkel_areal(r):
#     return pi*r**2
# # 2
# def sirkel_radius(A):
#     return (A/r)**0.5    # Opphøyer i 0.5 eller kan bruke sqrt fra numpy
# # 3
# def sirkel_omkrets(r):
#     return 2*pi*r
# # 4
# def kule_volum (r):
#     return 4/3*pi*r**3
# # 5
# def kule_overflate (r):
#     return 4*pi*r**2
# ```
# ````
# 
# ````{admonition} Oppgave 5.5
# :class: tip
# Forklar hvorfor programmet under gir _None_ som output.
# ```{code-block} Python
# def f(x):
#     x = 2*x
# x = 12
# x = x + 12
# x = f(x)
# print(x)
# ```
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Verdien til _x_ blir _None_ fordi funksjonen _f_ ikke returner en verdi. For å sørge for at _x_ får en tallverdi etter å ha kalt på _f_, må _f_ returnere noe – i dette tilfellet et tall.
# ```{code-block} Python
# def f(x):
#     return 2*x
# x = 12
# x = x + 12
# x = f(x)
# print(x)
# ```
# ````
# 
# ````{admonition} Oppgave 5.6
# :class: tip
# _Karvonens formel_ kan brukes til å finne pulsen til en person gitt hvilepuls $H_{hvile}$ og treningsintensitet $p$ (i prosent):
# 
# $hjerteslag \ per \ minutt = \left(H_{maks} - H_{hvile}\right)\cdot\frac{p}{100} + H_{hvile}$
# 
# der $H_{maks}$ er maks antall hjerteslag personen kan ha. Den maksimale pulsen kan en finne ved $H_{maks} = 220 - \textit{alder til person}$. Lag et program som regner ut pulsen til en 20 år gammel person som trener med 60 \% intensitet og hvilepuls på $70$ slag per minutt. Lag Karvonens formel som en funksjon.
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# def karvonen(hvilepuls, intensitet, alder):
#     p = intensitet
#     maks = 220 - alder
#     puls = (maks - hvilepuls)*p/100 + hvilepuls
#     return puls
# 
# puls = karvonen(70, 60, 20)
# print(" Personen vil ha en puls på",puls )
# ```
# ````
# 
# ````{admonition} Oppgave 5.7 (kjemi)
# :class: tip
# I kjemi har vi ofte bruk for molregning. Lag et enkelt program som regner ut antall mol dersom brukeren taster inn molmasse og masse av et bestemt stoff. Du kan også be brukeren taste inn stoffet det gjelder, slik at du får dette som output også. Lag formelen som en funksjon.
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# def antall_mol (masse , molmasse ):
#     return masse/molmasse
# stoff = input(" Hvilket stoff vil du finne antall mol til ?: ")
# masse = float(input(" Skriv inn massen ( gram ): "))
# molmasse = float(input(" Skriv inn molmassen ( gram /mol): "))
# mol = antall_mol (masse , molmasse )
# print("Stoffet", stoff, "består av", mol ,"mol.")
# ```
# ````
# 
# ````{admonition} Oppgave 5.8 (kjemi)
# :class: tip
# Lag et program som regner ut pH fra $[H_3O^+]$ ved hjelp av en funksjon.
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# from numpy import log10
# def ph_H3O(konsentrasjon):
#     return -log10 (konsentrasjon)
# 
# ph = ph_H3O(1E-5)
# print("pH av den gitte konsentrasjonen er:", ph)
# ```
# ````
# 
# ````{admonition} Oppgave 5.9 (fysikk)
# :class: tip
# Programmer én av bevegelsesformlene (kinematikklikningene) som en funksjon. Du kan selv velge hva programmet skal regne ut.
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# def posisjon(v0 , a, t):
#     return v0 + a*t
# 
# v = posisjon(2, 10, 5) # Tester funksjonen med v0 = 2, a = 10 og t = 5.
# print("Farten til legemet er:", v, "m/s.")
# ```
# ````
# 
# ````{admonition} Oppgave 5.10 (fysikk)
# :class: tip
# Bruk Bohrs formel for spektrene til hydrogenatomet:
# $f =\frac{B}{h}\cdot \left( \frac{1}{m^2} - \frac{1}{n^2} \right)$
# 
# Lag et program som regner ut bølgelengden til fotonet som emitteres når et elektron deeksiterer fra skall _m_ til _n_. Bruk en funksjon.
# 
# Husk at vi har følgende sammenheng mellom frekvens og bølgelengde ($\lambda$):
# 
# $\lambda = \frac{c}{f}$
# 
# $B = 2.18\cdot10^{-18}$, $c = 3.00\cdot10^8$ m/s og $h = 6.63\cdot10^{-34}$.
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# # Konstanter
# B = 2.18E-18
# h = 6.636E-34
# c = 3e8
# 
# #Bohrs formel
# def Bohr(n,m):
#     f = B/h *(1/ m**2 - 1/n **2)
#     bl = c/f            # bølgelengde i meter
#     bl_nm = bl*1E9      # bølgelengde i nanometer
#     return bl_nm
# 
# #Energinivåer
# n = int(input("Skriv inn en verdi for n:")) #skallet det eksiteres fra
# m = int(input("Skriv inn en verdi for m:")) #skallet det eksiteres til
# 
# print("Bølgelengden til lyset fra n =",n ,"til m =", m, 
#       "er:", round(Bohr(n,m)),"nm")
# ```
# ````
# 
# ````{admonition} Oppgave 5.11 (matematikk)
# :class: tip
# Lag en funksjon som tar tre variabler _a_, _b_ og _c_, tilsvarende koeffisientene i andregradsfunksjoner av typen $f(x) = ax^2 + bx + c$. La funksjonen løse andregradslikninger av typen $f(x) = 0$ ved hjelp av andregradsformelen.
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# def andregradsformelen(a, b, c):
#     rotuttrykk = b**2 - 4*a*c
#     if rotuttrykk > 0:
#         x1 = (-b + rotuttrykk**0.5)/(2*a)
#         x2 = (-b - rotuttrykk**0.5)/(2*a)
#         return x1, x2
#     elif rotuttrykk < 0:
#         return "Likningen har ingen reelle løsninger."
#     elif rotuttrykk == 0:
#         x = -b/(2*a)
#         return x
# 
# print(andregradsformelen(1, 2, 3))
# print(andregradsformelen(1, -2, 1))
# print(andregradsformelen(1, -4, 3))
# ```
# ````
# 
# ````{admonition} Oppgave 5.12
# :class: tip
# Hvorfor har _x_ samme verdi før og etter funksjonen _f_ har blitt kalt på i programmet under?
# ```{code-block} Python
# def f(x):
#     x = x + 3
#     return 9*x
# x = 3
# print(x) # Skriver ut 3
# y = f(x)
# print(x) # Skriver ut 3
# ```
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# _x_ er en global variabel utenfor funksjonen. Den får verdien 3. I tillegg finnes det en lokal variabel med samme navn inni funksjonen. Denne variabelen får verdien _x = x + 3 = 3 + 3 = 6_, men denne variabelen er ikke tilgjengelig utenfor funksjonen. 
# ```
# ````
# 
# ````{admonition} Oppgave 5.13
# :class: tip
# De fleste gasser kan modelleres med _tilstandslikninga for idelle gasser_:
# 
# $PV = nRT$
# 
# der _P_ er trykket i pascal, _V_ er volumet i kubikkmeter, _n_ er stoffmengden i mol, $R = 8.3144598 J/(mol\cdot K)$ er  gasskonstanten og _T_ er temperaturen i Kelvin. 
# 
# Lag et program der du bruker denne likninga til å lage en funksjon for P og en annen for T. Test funksjonene.
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# def trykk(V, n, T):
#     R = 8.3144598 # J/(mol*K)
#     P = n*R*T/V
#     return P
# 
# def temperatur(P, V, n):
#     R = 8.3144598 # J/(mol*K)
#     T = P*V/(n*R)
#     return T
# 
# print(trykk(100, 1, 300))
# print(temperatur(100, 1, 1))
# ```
# ````
# 
# ````{admonition} Oppgave 5.14*
# :class: tip
# Studer programmet nedenfor. Hvilke variabler er lokale, og hvilke er globale? Hva skrives ut?
# 
# ```{code-block} Python
# def f(x,y):
#     global e
#     e = x + y + e
#     return e
# 
# c = 1
# d = 2
# e = 3
# 
# print(f(c, d) + e)
# ```
# ````
# 
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# Variablene c_, _d_ og _e_ er globale variabler, mens _x_ og _y_ er lokale variabler som kun eksisterer inni funksjonen. Når vi printer _f(c, d) + e_, overføres verdien av _c_ og _d_ til de lokale variablene _x_ og _y_ i funksjonen. Deretter beregnes _e_ ved hjelp av _x_, _y_ og den globale _e_, som har verdien 3. Variabelen _e_ fra funksjonen (nå med verdien 6) defineres som global, og overskriver dermed den tidligere _e_ (med verdien 3). Det er denne _e_-en som legges til _f(c, d)_ i print-kommandoen til slutt.
# ```

# ## Filmer
# I videoen nedenfor kan du få en innføring eller repetisjon i den grunnleggende teorien bak funksjoner.
# 
# <iframe width="800" height="600" src="https://www.youtube.com/embed/PTsF6AIKIjg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
