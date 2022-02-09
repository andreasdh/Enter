#!/usr/bin/env python
# coding: utf-8

# # Datasamlinger
# 
# ```{admonition} Læringsutbytte
# Etter å ha arbeidet med dette temaet, skal du kunne:
# 1. opprette ulike arrayer
# 2. gjøre vektoroperasjoner med arrayer
# 3. gjøre rede for hva tupler er
# 4. opprette og bruke dictionarier
# ```
# 
# Vi har flere måter å organisere data på i Python. Her er en kort oversikt over de viktigste datasamlingene:
# 1. Lister (fleksible samlinger av like eller ulike data)
# 2. Arrayer (samlinger av tall som kan opereres på som vektorer).
# 3. Tupler (statiske lister som ikke kan endres)
# 4. Dictionarier (lister med strenger, ikke tall, som nøkler)
# 
# Vi har allerede sett hvordan lister fungerer. La oss se på de tre andre datatypene.
# 
# ## Arrayer
# Vi begynner med et eksempel som illustrerer forskjellen mellom lister og arrayer. For å kunne bruke arrayer, må vi først importere _numpy_ eller _pylab_.

# In[1]:


import numpy as np

liste1 = [1, 2, 3]
liste2 = [2, 3, 1]

print("listesum:", liste1 + liste2)

array1 = np.array(liste1)
array2 = np.array(liste2)

print("arraysum:", array1 + array2)


# ```{admonition} Underveisoppgave
# :class: tip
# Bruk koden ovenfor til å forklare forskjellen mellom listeaddisjon og arrayaddisjon.
# ```
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# Når to lister adderes, legges den ene lista til slutten på den andre. Når to arrayer adderes, får vi komponentvis addisjon av elementene: [1+2, 2+3, 3+1]. Dette er det samme som vektoraddisjon.
# ```
# 
# ### Opprette arrayer
# Vi kan opprette arrayer på flere måter:
# 
# <iframe src="https://trinket.io/embed/python3/33741d423e?font=1.2em" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Forklar de ulike måtene å opprette arrayer på ved å endre på forskjellige parametre i programmet ovenfor.
# ```
# 
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# Vi kan oppsummere måter å opprette arrayer på slik:
# | Operasjon | Forklaring |
# | --------- | ---------- |
# | array([x1,x2,x3,...]) | gjør om en liste med tall til en array |
# | arange(a,b,c) | lager en array med tallene a til, men ikke med, b, der c er steglengden |
# | linspace(a,b,c) | lager en array med c elementer fra a til og med b |
# | zeros(n) | lager en array med _n_ nuller |
# | ones(n) | lager en array med _n_ enere |
# ```
# 
# ### Behandle arraydata
# I motsetning til med lister, kan vi ikke bruke listeoperasjoner som _append_, _remove_ og liknende når vi opererer med arrayer. Vi kan derimot få tilgang til elementene ved å bruke indekser, akkurat som med lister.
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Hva tror du koden nedenfor skriver ut? Bruk det du husker om listeindeksering.
# ```
# 
# <iframe src="https://trinket.io/embed/python3/40c6ef7e3e?font=1.2em" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# Vi kan også lage flerdimensjonale arrayer, ved å sette inn arrayer i arrayer. Dette kan i noen tilfeller ses på som tabeller med kolonner og rader, slik som nedenfor.
# 
# ```{admonition} Underveisoppgave
# :class: tip
# 1. Prøv å forklare/forutse hva koden nedenfor gjør.
# 2. Kjør koden og se om det stemmer med slik du hadde tenkt. Hvis ikke, hva er forskjellen?
# 3. Undersøk hva du får som output når du endrer på tallene i print-kommandoene. Beskriv hva som skjer.
# 4. Modifiser programmet slik at det kun skriver ut de fire første elementene i kolonne 2.
# 5. Lag et program med en array som representerer dataene i tabellen nedenfor.
# Skriv så ut alt i kolonne nummer 3 (hvis vi teller fra 1) og elementet 6.7.
# ```
# 
# | Kolonne 1   | Kolonne 2   | Kolonne 3   | Kolonne 4  |
# |-----|-----|-----|-----|
# | 0   | 1   | 2   | 3   |
# | 2   | 9.1 | 2.2 | 4   |
# | 3.5 | 9.1 | 6.7 | 5.5 |
# | 1.1 | 0.2 | 8.9 | 7.8 |
# 
# <iframe src="https://trinket.io/embed/python3/fb87ba613c?font=1.2em" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ````{admonition} Løsningsforslag
# Vi har en array med to arrayer i, som vi kaller _data_. Vi kan plukke ut elementer fra denne arrayen slik:
# 
# ```{code-block} Python
# print(data[1,2]) # Printer element 2 (det tredje elementet) fra array 1 (den andre arrayen i arrayen)
# print(data[1,:]) # Printer alle elementer fra array 1 (den andre arrayen i arrayen)
# print(data[:,0]) # Printer element 0 (det første elementet) fra alle (begge) arrayene
# ```
# ````

# ### Matematikk med arrayer
# Noe som er praktisk med arrayer, er at de kan opppføre seg matematisk som vektorer eller matriser. Eksempler på en matematiske vektor og en matrise er:
# 
# $\vec{v} = [1, 4, 5]$
# 
# $M = \begin{bmatrix}1\ 2\ 2\\0\ 4\ 5\\ 6\ 1\ 1\end{bmatrix} = \begin{bmatrix}\vec{v} \\\vec{u} \\ \vec{w}\end{bmatrix} $
# 
# Vi skal ikke se så mye på matriser her, men det er nyttig å vite at det finnes matematiske størrelser som kan representeres som flerdimensjonale arrayer. Matriser kan også ses på som en samling vektorer.
# 
# La oss se på de vanligste vektoroperasjonene gjennom et eksempelprogram:
# 
# <iframe src="https://trinket.io/embed/python3/824f64f65b" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Test programmet ovenfor og beskriv hvordan de ulike operasjonene fungerer.
# ```

# ### Vektorisering
# En annen ting som er svært nyttig med arrayer, er at de er svært raske å behandle. Vektorisering betyr å bruke arrayer istedenfor å bruke løkker til å repetere operasjoner. Arrayaddisjon er et eksempel på vektorisering. Vi kunne jo ha addert komponentene trinnvis i en løkke. Nedenfor ser du et eksempel på både ikke-vektorisert og vektorisert kode. For å illustrere forskjellen i tida det tar å gjøre de to ulike kodene har vi importert _time_-biblioteket. Det lar oss registrere start- og slutt-tida i programmet, og vi kan derfor beregne tida det tar å kjøre koden ved å ta differansen mellom disse.
# 
# <iframe src="https://trinket.io/embed/python3/b8e8d3ead3" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Forklar hva som foregår i programmet ovenfor. Test programmet ovenfor og beskriv hvordan de ulike operasjonene fungerer. Sjekk også forskjellen i tid mellom komponentvis multiplikasjon av arrayer i en løkke og vektorisert multiplikasjon.
# ```

# ## Tupler
# Tupler blir brukt til å lagre statisk innhold som ikke skal endres. Et typisk eksempel er når vi skal spesifisere en fargekode i RGB (rød, grønn, blå). Da angis intensiteten til rød, grønn og blå som et tall mellom 0 og 255. Dette kan vi beskrive i en liste, men lister kan endres og er derfor ikke så robuste som tupler. Vi bruker derfor tupler til å lagre slike data. Istedenfor klammeparenteser bruker vi runde parenteser når vi lager tupler:

# In[1]:


svart = (0, 0, 0)
hvit = (255, 255, 255)
rød = (255, 0, 0)
magenta = (255, 0, 255)

print(magenta)


# ## Dictionarier
# 
# Dictionarier er en samling av data som indekseres med strenger istedenfor tall. Istedenfor klammeparenteser bruker vi krøllparenteser når vi lager dictionarier. Vi kaller indeksene i en dictionary for _nøkler_, og hver nøkkel har en _verdi_.
# 
# ```{code-block} Python
# dictionary = {"nøkkel1": verdi1, "nøkkel2": verdi2, "nøkkel3": verdi3, ...}
# ```
# 
# Dictionarier er spesielt nyttig når vi skal lagre informasjon om bestemte kategorier, som ulike arter, grunnstoffer eller radioaktive nuklider. Programsnutten nedenfor viser hvordan vi bruker en dictionary der vi oppgir atommassen til ulike grunnstoffer.

# In[3]:


atommasse = {"H": 1.01, "He": 4.00, "Li": 6.94, "Be": 9.01}

print(atommasse["Li"]) # Skriver ut atommassen til litium


# ```{admonition} Underveisoppgave
# :class: tip
# Forklar forskjellen mellom hvordan vi får ut elementer fra en liste sammenliknet med en dictionary.
# ```
# 
# Dictionarier blir ekstra nyttige når vi forstår hvordan vi kan lagre dictionarier i dictionarier. Da kan vi for eksempel lagre høyde, bredde og vekt til en bestemt art, eller ulike egenskaper ved grunnstoffene. Programmet nedenfor viser hvordan du kan gjøre dette. Vi ser også at vi enkelt kan skrive ut alle nøkler og verdier i en dictionary
# 
# <iframe src="https://trinket.io/embed/python3/b2e87a8abf?font=1.2em" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Legg inn et ekstra valgfritt grunnstoff i programmet ovenfor i tillegg til hydrogen og vanadium. Legg også til kokepunkt for alle grunnstoffene. Skriv ut kokepunktet til det nye grunnstoffet.
# ```

# ## Oppgaver
# 
# ```{admonition} Oppgave 6.1
# :class: tip
# Lag to arrayer. Fyll den ene med oddetall fra 1 til 101 og den andre med partall fra 0 til og med 100. Legg sammen arrayene.
# ```
# 
# ```{admonition} Oppgave 6.2
# :class: tip
# Et program skal regne ut $c = a + b$. Forklar hva $c$ vil bli dersom
# 1. $a = [1,2,3,4]$ og $b = [1,2,3,4]$
# 2. $a = [1,2,3,4]$ og $b = 1$
# 3. $a = array([1,2,3,4])$ og $b = 1$
# 4. $a = array([1,2,3,4])$ og $b = array([1,2,3,4])$
# ```
# 
# ```{admonition} Oppgave 6.3
# :class: tip
# Et program skal regne ut $c = a * b$. Forklar hva $c$ vil bli dersom
# 1. $a = [1,2,3,4]$ og $b = [1,2,3,4]$
# 2. $a = [1,2,3,4]$ og $b = 4$
# 3. $a = array([1,2,3,4])$ og $b = array([1,2,3,4])$
# ```
# 
# ```{admonition} Oppgave 6.4
# :class: tip
# Lag en array med alle tall i 9-gangen opp til 1000. Skriv ut tallene til slutt
# ```
# 
# ```{admonition} Oppgave 6.5 (kjemi)
# :class: tip
# Følgende kode regner ut pH i en løsning gitt ulike verdier av konsentrasjonen av oksoniumioner. Vektoriser koden.
# 
# import numpy as np
# H3O = [1E-10, 2.4E-9, 1E-8, 3.5E-7, 7E-6, 1.2E-5, 1E-4, 1E-2, 1.2]
# 
# def surhet(oksonium):
#     pH = -np.log10(oksonium)
#     return pH
#     
# pH = []
# 
# for kons in H3O:
#     pH.append(surhet(kons))
# ```
# 
# ```{admonition} Oppgave 6.6 (matematikk)
# :class: tip
# Vi har vektorene $\vec{v} = [2, 2]$ og $\vec{w} = [1, -3]$. Avgjør om vektorene er ortogonale ($\vec{v}\cdot \vec{w} = 0$). Kontroller ved å regne ut for hånd.
# ```
# 
# ```{admonition} Oppgave 6.7
# :class: tip
# Lise prøver å lage tre arrayer: én med alle partall fra og med 0 til og med 10, én med 1000 jevnt fordelte tall fra og med 0 til og med 10 og én med alle heltall fra og med 100 til og med 1 i synkende rekkefølge. Men programmet hennes gir feil output. Hva er feil? Rett opp programmet slik at Lise får gjort det hun ønsker.
# 
# <iframe src="https://trinket.io/embed/python3/f68691cb51" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# import numpy as np
# 
# partall = np.arange(0, 11, 2)
# mange_tall = np.linspace(0, 10, 1000)
# heltall_synkende = np.arange(100, 0, -1)
# 
# print("Første array:", partall)
# print("Andre array:", mange_tall)
# print("Tredje array:", heltall_synkende)
# ```
# ````
# 
# ```{admonition} Oppgave 6.8
# :class: tip
# Programmet nedenfor tegner fire sirkler, men sirklene trenger farge. Lag fire tupler som inneholder RGB-verdiene til fire valgfrie farger.
# 
# <iframe src="https://trinket.io/embed/python/03c16c2d46" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# ```
# 
# ```{admonition} Oppgave 6.9
# :class: tip
# Lag en dictionary med farger som nøkler og RGB-verdier som verdier (som tupler). Lag minst fem farger og skriv ut "RGB-koden for FARGE er: (R, G, B)" for hver farge i dictionarien.
# ```
# 
# ````{admonition} Oppgave 6.10
# :class: tip
# Følgende program har noen variabler som inneholder informasjon om noen elever som har en bestemt lærer. Legg dem inn i en dictionary isteden. Hva er fordelen med å bruke dictionarier her?
# ```{code-block} Python
# elever = ["Gunnar", "Marius", "Kristian"]
# lærer = ["Andreas"]
# ```
# ````
# 
# ````{admonition} Oppgave 6.11 (biologi)
# :class: tip
# Lag en dictionary med ulike arter og forskjellige egenskaper til disse artene. Det bør være minst 3 ulike arter med 3 egenskaper hver.
# ````

# ## Filmer
# I videoene nedenfor kan du få en innføring eller repetisjon i den grunnleggende teorien bak arrayer og dictionarier:
# 
# ````{tabbed} Arrayer og tupler
# <iframe width="800" height="600" src="https://www.youtube.com/embed/MCrjhPeEUWg? autoplay=0&rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# ````
# ````{tabbed} Dictionarier
# <iframe width="800" height="600" src="https://www.youtube.com/embed/ji5WjVfs_hQ? autoplay=0&rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# ````
