#!/usr/bin/env python
# coding: utf-8

# # Lister
# 
# ```{admonition} Læringsutbytte
# Etter å ha arbeidet med dette temaet, skal du kunne:
# 1. opprette lister
# 2. gjør ulike operasjoner på lister (NB: Du trenger ikke pugge operasjonene!)
# 3. trekke ut informasjon av lister ved hjelp av indekser
# ```
# 
# Når vi trenger å spare på flere verdier i samme variabel, kan vi benytte _lister_. Lister er samlinger med tall, strenger eller annet. Lister i Python markeres ved å sette objektene  i klammeparentes:
# 
# ```{code-block} Python
# dyr = ["gaupe", "torndjevel", "bjørnedyr", "blobfisk", "sjøkneler"]
# tall = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ```
# 
# Lister defineres altså gjennom klammeparentesen, og elementene i lista skilles med komma. Vi kan også gjøre ulike listeoperasjoner, som å legge til og slette elementer. La oss bruke lista med dyr som eksempel:
# 
# ```{code-block} Python
# dyr = []                   		                   # Lager ei tom liste
# aper = ["stumpneseape", "spøkelsesape", "neseape"] # Lager ei liste
# dyr.append("komodovaran")                          # Legger til et element til dyrelista
# dyr.append("glaucus atlanticus")	               # Legger til et dyr til
# dyr.extend(aper)                                   # Legger hele apelista inn i dyrelista
# dyr.remove("neseape")                              # Sletter elementet "neseape"
# dyr.pop(1)                        	               # Sletter element nr. 1 i lista
# dyr.reverse()                                      # Reverserer lista
# 
# print(dyr)
# ```
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Hva slags output gir programmet ovenfor? Prøv å forstå hva som skjer uten datamaskin, og test så programmet for å se om du hadde rett.
# ```
# 
# Plassnummeret til et element i lista kaller vi _indeks_. Indeksen angis ofte i klammeparentes. Vi kan også sortere lista, finne lengden av lista og finne de elementene vi ønsker. 
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Kjør programmet nedenfor og forklar hva som skjer.
# ```
# <iframe src="https://trinket.io/embed/python3/cc90f348cd?font=1.2em" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# Men vent nå litt! Vi ser at lista inneholder ni elementer -- hvorfor står det at nummer 94 står på plass nr. 7 når vi ser at det er nest sist i lista (altså på plass nr. 8)? Det er fordi indekser i Python, og mange andre språk, starter på 0. Det vil si at indeksen til det første totallet er 0, og til det siste elementet (102) er 8. Ei liste med $n$ elementer har elementer med indekser fra $0$ til $n - 1$.
# 
# Vi kan finne og bruke ulike elementer i ei liste ved å bruke indeksene til elementet. Vi trenger med andre ord ikke behandle hele lista hver gang vi trenger noen elementer derfra:
# 
# ```{code-block} Python
# liste = [1.3, 5.6, -2.0, 3.5, -3.5]
# A = liste[2]		# A får verdien til element 2 i lista 
# B = liste[1:3]		# B blir ei liste med element 1 til og med 2
# C = liste[2:]		# C blir ei liste med element 2 og sluttelementet
# D = liste[:2]		# D blir ei liste med element 0 til og med 1 (til 2)
# E = liste[-1]       # E får verdien til det siste elementet i lista
# F = liste[-2]       # F får verdien til det nest siste elementet i lista
# ```
# ```{admonition} Underveisoppgave
# :class: tip
# Hvilken verdi får variablene A, B, C, D, E og F ovenfor?
# ```
# 
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# Indekser angir plasseringen i lista. Dersom indeksen er negativ, teller vi baklengs, altså fra det siste elementet og bakover. Husk at Python teller fra 0, ikke fra 1. Kolon angir "til", så 1:3 betyr fra og med element 1 til, men ikke med, element 3 (det vil si element 1 og 2). Når det ikke står noe foran kolon, tolkes det som fra det første elementet (element nummer 0). Når det ikke står noe etter kolon, tolkes det som til og med det siste elementet (element nummer -1). Vi får derfor:
# 
# A: -2.0
# B: [5.6, -2.0]
# C: [-2.0, 3.5, -2.5]
# D: [1.3, 5.6]
# E: -3.5
# F: 3.5
# ```
# 
# Det er noen andre operasjoner som en kan gjøre med lister. I tillegg er det ofte flere måter å gjøre ting på. La oss lage et par tallister og gjøre noen operasjoner på disse.
# 
# <iframe src="https://trinket.io/embed/python3/984d71242d" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Prøv ut programmet ovenfor og forklar hva som skjer. Endre gjerne på noen av operasjonene og se hva utfallet blir. Utvid også programmet slik at det skriver ut det siste elementet i lista _c_. Skriv også ut alle elementer bortsett fra det første.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# print(c[-1])
# print(c[1:])
# ```
# ````
# 
# Siden vi sletter element nr. 2 (som er tallet 3), får vi beskjed om at 3 ikke er i c lenger ("False"). Legg også merke til at når vi legger sammen listene, er det omtrent det samme som å bruke kommandoen _extend_.
# 
# ## Oppgaver
# ````{admonition} Oppgave 2.1
# :class: tip
# Forklar for hvert program hvorfor det gir følgende output:
# ```{code-block} Python
# a = [1,2,3,4,5,6,7,8,9]
# b = a[1] + a[5]
# print(b)
# ```
# *Output:* 8
# 
# ```{code-block} Python
# liste = [1,2,3,4,5]
# liste1 = liste[:3]
# liste.pop(1)
# liste1.reverse()
# del liste1[2]
# liste += liste1
# print(liste)
# ```
# *Output:* [1, 3, 4, 5, 3, 2]
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# 1. Siden _a[1]_ henter ut andre element i lista _a_, vil _a[1] = 2_. Siden _a[5]_ henter ut sjette element i lista, vil _a[5] = 6_. Dette gir at _b = a[1] + a[5] = 2 + 6 = 8_.
# 
# 2. Vi kan beskrive programflyten steg for steg slik:
# - Lista _liste[:3]_ består av de tre første elementene fra _liste_. Dette gir at _liste1 = [1,2,3]_.
# - Ved å skrive _liste.pop(1)_, fjernes elementet med indeks 1 fra _liste_. Elementet med indeks 1 er 2. Nå er _liste = [1,3,4,5]_.
# - Kommandoen _liste1.reverse()_ reverserer liste1. Nå er _liste1 = [3,2,1]_.
# - Ved å skrive _del liste1[2]_ fjernes elementet med indeks 2 fra _liste1_, altså 1. Nå er _liste1 = [3,2]_.
# - Siden _liste += liste1_ er det samme som _liste + liste1_, vil _liste_ bli utvida med _liste1_. Da vil _liste = liste + liste1 = [1,3,4,5] + [3,2] = [1,3,4,5,3,2]_.
# ````
# 
# ````{admonition} Oppgave 2.2
# :class: tip
# Du får gitt ei liste som ser slik ut:
# 
# ```{code-block} Python
# ['dette','er','en','ganske','lang','liste','med','ikke', 'så','viktig','innhold']
# ```
# Lag ei ny liste der programmet henter relevante elementer fra den gitte lista. Når du skriver ut den nye lista, skal du få:
# ['dette','er','en','liste','med','viktig','innhold']
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# liste = ["dette", "er", "en", "ganske", "lang", "liste" ,"med" ,"ikke", "så", "viktig" ,"innhold"]
# ny_liste = liste [:3] + liste [5:7] + liste [9:]
# print(ny_liste)
# ```
# ````
# 
# ````{admonition} Oppgave 2.3
# :class: tip
# 
# Skriv om linja som endrer på lista _a_ slik at _i1_ og _i2_ har forskjellige verdier. 
# 
# ```{code-block} Python
# a = [1,5,2,5,2,4,4,2]
# i1 = a.index(2)
# print("i1 =",i1)
# del a[7]
# i2 = a.index(2)
# print("i2 =",i2)
# ```
# ````
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# a = [1,5,2,5,2,4,4,2]
# i1 = a.index(2)
# print("i1 =", i1)
# del a[2]
# i2 = a.index(2)
# print("i2 =", i2)
# ```
# ````
# 
# ## Video
# Se videoen nedenfor for en innføring eller repetisjon til lister.

# In[1]:


from IPython.display import IFrame
IFrame("https://www.youtube.com/embed/1ZeRsnlxU4A? autoplay=0&rel=0", width=800, height=600)

