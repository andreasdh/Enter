#!/usr/bin/env python
# coding: utf-8

# # Vilkår (if-tester)
# 
# ```{admonition} Læringsutbytte
# Etter å ha arbeidet med dette temaet, skal du kunne:
# 1. bruke vilkår til å systematisere valg i programkode
# 2. illustrere og løse matematiske og naturvitenskapelige problemstillinger med sammensatt kode der vilkår inngår
# ```
# ````{admonition} Innledende oppgave
# :class: tip
# Før du går i gang med å programmere, prøv å forklare hva følgende kodesnutter gjør:
# 
# ```{code-block} Python
# tall = 10
# 
# if tall > 8:
#     print("Tallet er større enn 8.")
# ```
# 
# ```{code-block} Python
# tall = 10
# 
# if tall < 8:
#     print("Tallet er mindre enn 8.")
# ```
# 
# ```{code-block} Python
# tall = 10
# if tall < 8:
#     print("Tallet er mindre enn 8.")
# else:
#     print("Tallet er ikke mindre enn 8.")
# ```
# 
# ```{code-block} Python
# tall = 10
# if tall < 8:
#     print("Tallet er mindre enn 8.")
# elif tall >= 8:
#     print("Tallet er ikke mindre enn 8.")
# ```
# ````
# 
# ## Definisjon
# 
# ```{admonition} Vilkår
# Et vilkår, eller en betingelse, er en logisk test for å sjekke om et kriterium er oppfylt. Dersom kriteriet er oppfylt, utføres det en handling. Dersom kriteriet ikke er oppfylt, blir ikke handlingen utført. Vilkår beskrives ofte i programmering som en «hvis-setning» («if» i Python).
# ```
# Vilkår er sentrale i programmering, men også sentrale i hverdagen. Vi kan lage et enkelt eksempel ut fra billettpriser på bussen. Hvis du er under 18 år, blir prisen 31 kroner. Hvis ikke, regnes du som voksen, og må betale 62 kroner. Vi kan beskrive dette med følgende pseudokode:
# 
# ```{code-block} text
# hvis alder er mindre enn 18:
#     pris = 31
# hvis ikke:
#     pris = 62
# ```
# 
# Dersom vi oversetter denne pseudokoden til Python-kode, ser vi at logikken og strukturen er ganske lik:
# 
# ```{code-block} Python
# if alder < 18:
#     pris = 31
# else: 
#     pris = 62
# ```
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Vi kan illustrere hvordan vilkår fungerer med et puslespill. Puslespillet nedenfor er basert på billettpriseksempelet. Løs puslespillet nedenfor uten å se på Python-koden ovenfor. Pass på at innrykkene er riktig! Hva tror du innrykk betyr?
# ```

# In[9]:


from IPython.display import IFrame
IFrame('https://parsons.herokuapp.com/puzzle/1a01c8b7115240199d88a732d06317b1', width=1000, height=450)


# ## Vilkår i Python
# La oss se på et eksempel i Python:
# 
# ```{code-block} Python
# tall = float(input("Tast inn et tall: "))
# if tall > 1:
#     print("Hurra, tallet er større enn 1!")
# ```
# 
# Programmet ber brukeren om å taste inn et vilkårlig tall som deretter konverteres til flyttall. Vilkåret starter med _if_, etterfulgt av variabelnavnet. Deretter gir vi et kriterium som skal sjekkes. Her tester vi om tallet er større enn 1. Dersom det er større enn 1, skrives det ut en beskjed. Vi må ha et kolon etter første linje, og innrykk på alt som hører til det spesifikke kriteriet. Dersom kriteriet ikke er oppfylt, skjer det ingen ting. Dersom vi vil at det skal skje noe selv om kriteriet ikke er oppfylt, kan vi legge til _else_-kommandoen:
# 
# ```{code-block} Python
# tall = float(input("Tast inn et tall: "))
# if tall > 1:
#     print("Hurra, tallet er større enn 1!")
# else:
#     print("Tallet er ikke større enn 1.")
# ```
# Dersom kriteriet (tall > 1) ikke er sant, blir beskjeden etter _else_ skrevet ut. Vi kan legge til enda flere kriterier ved å bruke _elif_ (forkortelse for _else if_):
# 
# ```{code-block} Python
# tall = float(input("Tast inn et tall: "))
# if tall > 1:
#     print("Hurra, tallet er større enn 1!")
# elif tall < 1:
#     print("Tallet er mindre enn 1!")
# else:
#     print("Tallet er 1!")
# ```
# 
# Det er en logisk konklusjon at tallet _er_ 1 dersom det verken er større eller mindre enn 1. For å være helt sikre, kan vi erstatte else-kommandoen med nok en elif-kommando:
# 
# ```{code-block} Python
# tall = float(input("Tast inn et tall: "))
# if tall > 1:
#     print("Hurra, tallet er større enn 1!")
# elif tall < 1:
#     print("Tallet er mindre enn 1!")
# elif tall == 1:
#     print("Tallet er 1!")
# ```
# 
# Legg merke til at symbolet _==_ brukes for å teste om tallet er lik 1. Dersom vi bruker enkel likhetstegn (=) tror Python at vi prøver å tilordne en variabel. Da får vi en feilmelding. De ulike symbolene som brukes i vilkår, er oppsummert i tabellen nedenfor.
# 
# | Symbol | Betydning |
# | ------ | --------- |
# | > | Større enn |
# | < | Mindre enn |
# | == | Er lik |
# | <= | Mindre enn eller lik |
# | >= | Større enn eller lik |
# | != | Ikke lik |
# 
# Det er noen ting å passe spesielt på når vi programmerer med vilkår:
# - Alt som er rykket inn utføres kun hvis if-testen ovenfor er sann. Innrykk er derfor viktig for strukturen.
# - "elif" står for "else if", og sjekker noe nytt, mens "else" brukes for å gjøre noe dersom ingen av kriteriene under "if" og "elif" er sanne.
# - Det er den første if-testen som er sann i en serie av if-elif-else som utføres. Alle andre overses. Dersom vi skriver "if" en gang til, begynner vi på en ny serie med if-elif-else.
# - Vi _må_ begynne med "if", mens "elif" og "else" er valgfritt.
# - De logiske operatorene vi kan velge mellom, er:
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Lag et program der du sjekker om et tall er positivt, negativt eller null, og skriver ut relevante setninger når de ulike kriteriene er nådd. Du kan ta utgangspunkt i programkoden i kodeboksen her:
# ```
# <iframe src="https://trinket.io/embed/python3/12af96f83e?font=1.5em" width="100%" height="500" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# tall = 2
# 
# if tall > 0:
#     print("Tallet er positivt")
# elif tall < 0:
#     print("Tallet er negativt")
# else:    # Eventuelt elif tall == 0:
#     print("Tallet er 0")
# ```
# ````

# ## Nøstede vilkår
# Vi kan også ha vilkår inni vilkår. Dette er spesielt nyttig hvis vi skal sjekke flere ting som er avhengige av hverandre. Nedenfor ser du en svært forenklet bestemmelsesnøkkel for grunnstoffer som illustrerer prinsippet. Kanskje du kan legge inn et kriterium til som gjør bestemmelsen mer presis?

# In[2]:


elektronegativitet = float(input("Hvilken elektronegativitet har grunnstoffet? "))
if elektronegativitet > 2:
    print("Grunnstoffet er mest sannsynlig et ikke-metall.")
else:
    reaktivt = input("Er grunnstoffet svært reaktivt (ja/nei)? ")
    if reaktivt == "ja":
        print("Grunnstoffet er mest sannsynlig et alkalimetall.")
    elif reaktivt == "nei":
        print("Grunnstoffet kan for eksempel være et innskuddsmetall eller et jordalkalimetall.")


# ```{admonition} Underveisoppgave
# :class: tip
# Bruk flytskjemaet nedenfor som utgangspunkt for et program som finner ut hva slags bergart du har oppdaget.
# 
# <img src="https://github.com/andreasdh/programmering-i-kjemi/blob/master/docs/bilder/bergarter.png?raw=true" width="500"/>
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# print("Velkommen til bestemmelsesnøkkel for bergarter!")
# prikker = input("Er mønsteret i steinen prikkete (ja/nei)? ")
# if prikker == "ja":
#     print("Du har funnet en magmatisk bergart.")
# elif prikker == "nei":
#     striper = input("Er mønsteret i steinen stripete  (ja/nei)? ")
#     if striper == "ja":
#         print("Du har funnet en metamorf bergart.")
#     elif striper == "nei":
#         print("Du har funnet en sedimentær bergart.")
#     else:
#         print("Vennligst svar 'ja' eller 'nei'")
# else:
#     print("Vennligst svar 'ja' eller 'nei'")
# ```
# ````

# ## Oppgaver
# ```{admonition} Oppgave 3.1
# :class: tip
# Forklar hvorfor de to ulike programmene nedenfor gir ulike output.
# ```

# In[ ]:


a = 10
if a > 5:
    a = a + 5
a = a + 2
print(a)


# In[ ]:


a = 10
if a > 5:
    a = a + 5
else:
    a = a + 2
print(a)


# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Verdien til _a_ er større enn 5. Dette gjør at programmet vil gjøre det som står under _if_ i begge programmene.
# 
# Første program vil utføre _a = a + 2_ etter if -testen uansett om _a > 5_ stemmer eller ikke. Dette er fordi _a = a + 2_ ikke er en del av if-testen.
# 
# Siden andre kodesnutt bruker en else-kommando, vil _a = a + 2_ utføres kun når _a_ ikke er større enn 5. Siden verdien til _a_ er større enn 5, vil programmet utføre det som står under _if_.
# ````
# 
# ```{admonition} Oppgave 3.2
# :class: tip
# Lag et program som spør brukeren om alderen til brukeren. Skriv ut en kommentar som avhenger av om alderen er under eller over 17. Utvid programmet til å skille mellom flere aldre.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# alder = int(input("Hvor gammel er du? "))
# if alder < 17:
#     print("Dra tilbake til barnehagen!")
# elif alder == 17:
#     print("Du er i din beste alder")
# elif alder < 25:
#     print("Voksenlivet nærmer seg!")
# else:
#     print("Dra tilbake til gamlehjemmet!")
# ```
# ````
# 
# ```{admonition} Oppgave 3.3
# :class: tip
# Lag et program som tar en poengsum som input. Programmet skal finne ut hvilken karakter du får dersom maks poengsum er 60 poeng. Finn på karaktergrenser selv.
# 
# Utvid programmet med en maks poengsum. Programmet skal benytte prosenter av denne makssummen til å regne ut sluttkarakteren. Lag prosentgrensene selv.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# maks_poeng = int(input("Hva er maks poengsum? "))
# poengsum = int(input("Hvor mange poeng fikk du? "))
# 
# prosent1 = 20
# prosent2 = 40
# prosent3 = 60
# prosent4 = 80
# prosent5 = 95
# 
# grense1 = maks_poeng /100*prosent1
# grense2 = maks_poeng /100*prosent2
# grense3 = maks_poeng /100*prosent3
# grense4 = maks_poeng /100*prosent4
# grense5 = maks_poeng /100*prosent5
# 
# if poengsum < grense1 :
#     karakter = 1
# elif poengsum < grense2 :
#     karakter = 2
# elif poengsum < grense3 :
#     karakter = 3
# elif poengsum < grense4 :
#     karakter = 4
# elif poengsum < grense5 :
#     karakter = 5
# else: # poengsum må være større enn grense5
#     karakter = 6
# 
# print("Du fikk karakteren", karakter)
# ```
# ````
# 
# ```{admonition} Oppgave 3.4
# :class: tip
# Lag et program som tar to tall som input. Programmet skal skrive ut hvilket av de to tallene som er størst.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# tall1 = int(input("Skriv et tall: "))
# tall2 = int(input("Skriv et til tall: "))
# 
# if tall1 > tall2:
#     største = tall1
# else:
#     største = tall2
# print("Det største tallet av", tall1 ,"og", tall2,"er:", største)
# ```
# ````
# 
# ```{admonition} Oppgave 3.5
# :class: tip
# Puslespillet nedenfor skal bli et program som skal regne ut hvor mange løsninger en andregradslikning på formen $ax^2 + bx + c = 0$ har. Prøv å sette sammen puslespillet. Hvis du blir fort ferdig eller trenger en ekstra utfordring, kan du prøve [denne varianten](http://parsons.problemsolving.io/puzzle/a56e0f5a917a4079aadffb571c3d411e).
# ```

# In[1]:


from IPython.display import IFrame
IFrame('https://parsons.herokuapp.com/puzzle/6e30d3320c8e4ba69b61a0e302754a3c', width=1000, height=600)


# ```{admonition} Oppgave 3.6
# :class: tip
# Lag et program som tar utgangspunkt i puslespillet ovenfor. Programmet skal også regne ut hva løsningene er.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# a = 1
# b = -3
# c = 2
# 
# rotuttrykk = b**2 - 4*a*c
# 
# if rotuttrykk > 0:
#     x1 = (-b + rotuttrykk**0.5)/(2*a)
#     x2 = (-b - rotuttrykk**0.5)/(2*a)
#     print("Likningen har løsningene x1 =", x1, "og x2 =", x2)
# elif rotuttrykk == 0:
#     x = -b/(2*a)
#     print("Likningen har løsningen x = ", x)
# else:
#     print("Likningen har ingen reelle løsninger.")
# ```
# ````
# 
# ```{admonition} Oppgave 3.7
# :class: tip
# Lag en kalkulator der brukeren må taste inn to tall og en regneoperasjon. Du bestemmer selv hvor mange regneoperasjoner programmet skal håndtere.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# tall1 = float(input("Første tall: "))
# op = input("Velg operasjon ( + , - , / , * ): ")
# tall2 = float(input(" Andre tall: "))
# 
# if op == "+":
#     resultat = tall1 + tall2
# elif op == "-":
#     resultat = tall1 - tall2
# elif op == "/":
#     resultat = tall1 / tall2
# elif op == "*":
#     resultat = tall1 * tall2
# else:
#     resultat = "udefinert "
# print(tall1, op, tall2, "=", resultat)
# ```
# ````
# 
# ```{admonition} Fysikkoppgave
# :class: tip
# Lag et program der du kan taste inn bølgelengden til synlig lys i nm og få ut hvilken farge lyset har. Utvid eventuelt programmet med andre deler av det elektromagnetiske spekteret.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# bl = float(input("Skriv inn lysets bølgelengde i nm: "))
# 
# if 380 <= bl < 420:
#     farge = "fiolett"
# elif 420 <= bl < 490:
#     farge = "blå"
# elif 490 <= bl < 575:
#     farge = "grønn"
# elif 575 <= bl < 585:
#     farge = "gul"
# elif 585 <= bl < 650:
#     farge = "oransje "
# elif 650 <= bl <= 750:
#     farge = "rød"
# else:
#     farge = "udefinert "
# print("Fargen til lyset er:", farge )
# ```
# ````
# 
# ```{admonition} Kjemioppgave
# :class: tip
# Lag et program med en variabel kalt pH. Programmet skal skrive ut om løsningen med denne pH-en er sur, basisk eller nøytral.
# 
# $$pH = -log([H_3O^+])$$
# 
# Her står $[H_3O^+]$ for konsentrasjonen av $H_3O^+$-ioner. Test programmet med $[H_3O^+] = 1\cdot 10^{-7}$. Dette bør gi nøytral løsning.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# from numpy import log10
# 
# oksonium = float(input("[H3O+]: "))
# pH = -log10(oksonium)
# 
# if pH < 7:
#     print("Løsningen er sur.")
# elif pH > 7:
#     print("Løsningen er basisk.")
# elif pH == 7: # Eventuelt else:
#     print("Løsning er nøytral.")
# ```
# ````
# 
# ```{admonition} Biologioppgave
# :class: tip
# Vi skal se på en populasjon av mennesker og ser på et gen som finnes i to varianter: $a$ og $A$. Andelen av populasjonen som har variant $a$ kan vi kalle for $p$ og andelen av populasjonen som har variant $A$ kan vi kalle for $q$. Verdiene til $p$ og $q$ må være mellom 0 og 1. 
# Siden alle i populasjonen vil ha enten $a$ eller $A$ (eller begge), må $p + q = 1$.
# 
# Populasjonen sies å være i _Hardy-Weinberg-likevekt_ dersom verdiene til $p$ og $q$ ikke forandrer seg under forutsetningen at det foregår tilfeldig paring, ingen mutasjoner, ingen naturlig seleksjon og ingen evolusjon i populasjonen.
# 
# Dersom populasjonen er i Hardy-Weinberg-likevekt kan en finne andelen til de tre mulige genotypene til menneskene i populasjonen:
# - $AA$ : $p^2$ 
# - $Aa$ : $2pq$
# - $aa$ : $q^2$
# 
# Lag et program som ber brukeren om verdien til $p$ og $q$.
# Programmet skal så teste om $ p + q = 1$. Hvis summen er 1, skal programmet regne ut andelene til de tre mulige genotypene, og skrive dem ut. Hvis summen ikke er 1, skal programmet skrive en feilmelding.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# p = float(input(" Hvor stor andel har genvariant a?: "))
# q = float(input(" Hvor stor andel har genvariant A?: "))
# if p + q == 1:
#     AA = p**2
#     Aa = 2*p*q
#     aa = q**2
#     print(" Andel som har genotype AA:", round(AA,2))
#     print(" Andel som har genotype Aa:", round(Aa,2))
#     print(" Andel som har genotype aa:", round(aa,2))
# else:
#     print("Summen av p og q er ikke lik 1!")
# ```
# ````
# 
# ```{admonition} Sammensatt oppgave
# :class:tip
# Lag et lite eventyrspill der spilleren får ulike valg underveis, og historien formes av valgene spilleren tar. Du kan gjerne bruke input-funksjonen for å gi spilleren ulike valg. Det blir gjerne mange if-tester inni if-tester, så hold styr på innrykkene dine.
# ```

# ## Video
# Se videoen nedenfor for å få en gjennomgang av det viktigste når vi skal programmere if-tester i Python:
# 
# <iframe width="900" height="600" src="https://www.youtube.com/embed/XkDoYa7aGwc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# In[ ]:




