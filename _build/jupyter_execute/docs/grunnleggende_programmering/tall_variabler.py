#!/usr/bin/env python
# coding: utf-8

# # Variabler og datatyper
# 
# ```{admonition} Læringsutbytte
# Etter å ha arbeidet med dette temaet, skal du kunne:
# 1. kjøre enkle programmer med en programmeringseditor
# 2. definere og gjøre rede for ulike variabeltyper: heltall, flyttall og strenger
# 3. skrive ut output ved å bruke print-funksjonen
# 4. gjøre enkel aritmetikk i Python
# 5. ta input fra brukeren av programmet
# 6. importere og bruke biblioteker
# ```
# 
# ## Variabler
# 
# ```{admonition} Variabel
# En programmeringsvariabel er en størrelse som lagrer en verdi i et program.
# ```
# 
# Variabler er spesielt nyttig når vi skal bruke samme verdi flere ganger, eller når vi skal oppdatere en verdi underveis i programmet. Et enkelt eksempel er hvis vi ønsker å finne ti tall i en bestemt tallrekke. Dette kan vi beskrive slik med en pseudokode:
# 
# ```{code-block} text
# tall = 0
# gjenta 10 ganger:
#     tall = tall + 3
#     vis tall på skjermen
# ```
# 
# Du kan tenke på en variabel som en boks vi kan putte ting i, og som vi kan modifisere, endre og hente informasjon fra underveis.
# 
# ```{admonition} Hva er en pseudokode?
# :class: caution, dropdown
# En pseudokode er en beskrivelse av en algoritme uten å bruke et bestemt programmeringsspråk. Pseudokode kan skrives på mange måter og kan beskrives med ord, bilder og symboler.
# ```
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Nedenfor er et eksempel på en programkode i Python der vi beregner gjennomsnittshastigheten i m/s for ulike legemer som har beveget seg henholdsvis 3, 4.5, 7 og 14 meter i løpet av 3 sekunder. Hva er fordelen med å bruke variablen _t_ her?
# ```
# 
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# Kommandoen _print_ gir oss et ouput fra programmet vårt. Vi sier at noe blir skrevet ut til "konsollen". Konsollen er der du får output i et programmeringsmiljø. Inni print-kommandoen kan vi skrive flere ting. Da må hver variabel og hver verdi være adskilt med komma.
# ```

# In[1]:


t = 3

v1 = 3/t
v2 = 4.5/t
v3 = 7/t
v4 = 14/t


# ## Print
# For å få noe ut av programmet vårt, må vi be datamaskinen om å "skrive ut" noe. Dette gjør vi med kommandoen _print_. Dersom vi ønsker å skrive ut flere variabler, må vi skille dem med komma i print-funksjonen. Her ser du tre måter å bruke print-kommandoen på:

# In[2]:


print(v1)
print(v1, v2, v3, v4)
print("Gjennomsnittsfarten for legeme 4 er: ", v4, "m/s.")


# ```{admonition} Underveisoppgave
# :class: tip
# Lag et program som regner ut arealet av et rektangel og skriver ut en svarsetning med enheter.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# side1 = 5
# side2 = 3
# A = side1*side2
#  
# print("Arealet til rektangelet er:", A, "kvadratmeter")
# ```
# ````

# ## Kommentarer
# Bruk av kommentarer i koden er viktig for at en selv skal huske hva koden illustrerer, hvilke enheter som brukes, og liknende. I tillegg er det viktig dersom andre skal bruke koden din til noe, for eksempel i store samarbeidsprosjekter. Kommentarer legges til ved å sette en \# foran kommentaren. Eventuelt, dersom du kommenterer over flere linjer, kan du bruke triple anførselstegn før og etter kommentarene. Her er et eksempel:

# In[11]:


"""
Regner ut kinetisk energi i én dimensjon 
for et legeme med masse m og hastighet v
"""

m = 2.0        # masse i kg
v = 1.0        # fart i m/s

E = 0.5*m*v**2 # Kinetisk energi i J
print("Den kinetiske energien er", E)


# ## Aritmetikk
# Vi kan bruke Python som en enkel kalkulator. Vi har blant annet følgende operatorer:
# 
# |Operator | Forklaring |
# |---------|------------|
# | + | Addisjon (a + b) |
# | - | Subtraksjon (a - b) |
# | * |Multiplikasjon (a\*b) |
# | / | Divisjon (a/b) |
# | ** | Eksponent (a\*\*b) |
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Det finnes også to spesielle operatorer: // og %. Finn ut hva disse operatorene gjør ved å prøve dere fram i koderuta nedenfor. Vi har lagt til fire linjer som du kan bruke som utgangspunkt.
# ```
# 
# <h4><iframe src="https://trinket.io/embed/python3/1cdda2d57c?font=2em" width="100%" height="356" allowfullscreen="allowfullscreen"></iframe></h4>
# 
# ```{admonition} Løsning
# :class: tip, dropdown
# // utfører heltallsdivisjon, det vil si at operatoren finner det høyeste heltallet divisjonen går opp i. 24 // 5 = 4 fordi 4 * 5 = 20, som er det nærmeste vi kommer 24 i 5-gangen uten å overskride 24. Resten etter denne divisjonen er 4. Det får vi fram ved å bruke «modulusoperatoren» %, som ikke har noe med prosent å gjøre. 24 % 5 er altså 4.
# ```
# 
# ### Biblioteker
# De fleste matematiske operatorer og funksjoner finnes ikke i standard Python. For å få tilgang til mer avansert matematikk, må vi importere _biblioteker_ (eller _moduler_) inn i Python-programmet vårt. Et bibliotek er en pakke med ekstra kommandoer og funksjoner som vi kan bruke, som _sqrt_, _cos_, _log_ og så videre. Det finnes ulike måter å importere på. Her er noen måter vi kan importere det svært nyttige _nympy_-biblioteket (**num**erical **py**thon):

# In[5]:


# Første metode: Importerer kun funksjonene du trenger
from numpy import log10

pH = -log10(1E-7)

# Andre metode: Importere hele biblioteket
import numpy

A = 2 
radius = numpy.sqrt(A/numpy.pi)

# Tredje metode: Importere hele biblioteket med et alias. Dette er den mest brukte metoden.
import numpy as np

A = 2
radius = np.sqrt(A/np.pi)

# Fjerde metode: Importere alt fra biblioteket uten å spesifisere hvor funksjonene kommer fra
from numpy import *

vinkel = arccos(0.5) # Invers cosinus av 0.5
pH = -log10(1E-7)    # pH = -log([H3O+]), log10 er tierlogaritmen


# ```{admonition} Underveisoppgave
# :class: tip
# Lag et program som regner ut radius til en sirkel med arealet 4 ved å importere sqrt og pi fra numpy-biblioteket. Kunne du gjort beregningene uten disse funksjonene?
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# from numpy import pi, sqrt
# 
# A = 4
# r = sqrt(A/pi) # Vi kunne også skrevet (A/pi)**0.5
#  
# print("Radius til sirkelen er:", r)
# ```
# ````

#  ## Brukerinput
# Vi kan også få programmet vårt til å spørre brukeren av programmet om å taste inn enkelte variabler selv. Dette gjøres i samme ruta som du får _output_ i editoren din. For å få brukerinput, bruker vi funksjonen _input_. Kjør programmet nedenfor og beskriv hvordan det fungerer. Prøv å bytte ut ulike kodelinjer og se hva slags output du får. Du må skrive inn input-verdiene i konsollen til høyre i koderuta.
# 
# <iframe src="https://trinket.io/embed/python3/4af0f30f45" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# Input er ikke nødvendig for annet enn å lage et mer interaktivt program. Men hvis du lager et program med input, bør du legge til input helt til slutt. Start med å gi variablene verdier, og test at programmet fungerer. Deretter kan du bruke input på de variablene du ønsker. Dette er for å unngå å måtte taste inn input-verdier hver gang du kjører programmet ditt, spesielt hvis det inneholder feil du må rette opp!
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Modifiser programmet fra forrige underveisoppgave slik at det tar arealet som input fra brukeren.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# from numpy import pi, sqrt
# 
# A = input("Skriv arealet til sirkelen: ")
# A = float(A)
# r = sqrt(A/pi) # Vi kunne også skrevet (A/pi)**0.5
#  
# print("Radius til sirkelen er:", r)
# ```
# ````

# ## Variabeltyper
# I matematikk har vi ulike tallmengder, som _reelle tall_, _irrasjonale tall_, _rasjonale tall_, _naturlige tall_, _hele tall_ og _komplekse tall_. Disse tallmengdene er uendelig store, som betyr at de ikke kan eksistere på en datamaskin. Vi har derfor en del andre tallmengder og variabeltyper. For eksempel heter desimaltall _float_ fordi ikke alle desimaltall er representert på en datamaskin. Det er altså en annen tallmengde. De viktigste variabeltypene ser du her:
# 
# | Datatype | Forklaring            |Eksempel |
# |--------|----------------------|-------------|
# | Heltall (int)      | Hele tall       | 42 |
# | Flyttall (float)      | Desimaltall | 3.1415     |
# | Streng (str)     | Tekst           | "Hei!"|
# | Boolsk     | Sannhet       |True eller False  |
# 
# Når vi ønsker input fra en bruker av et program, må vi spesifisere hvilken variabeltype vi ønsker at inputen skal bli tolket som. Standard er tekst, men hvis vi for eksempel "adderer" teksten "4" med "2", får vi "42", mens tallet 4 + tallet 2 gir tallet 6. Eksempelet nedenfor illustrerer dette.

# In[6]:


tekst1 = input("Skriv et tall: ")
tekst2 = input("Skriv et tall til: ")

tall1 = float(tekst1)
tall2 = float(tekst2)

tullsvar = tekst1 + tekst2
tallsvar = tall1 + tall2

print("Summen av teksten er:", tullsvar, "og summen av tallene er:", tallsvar)


# ```{admonition} Underveisoppgave
# :class: tip
# Lag et program som skriver "Hei, _navn_!" til skjermen. Brukeren skal bes om å taste inn navnet sitt. Dette navnet skal lagres i en variabel, og så skrives ut som i setningen ovenfor.
# 
# Utvid programmet til å spørre om alderen din. La programmet skrive ut en kommentar til alderen din til slutt, for eksempel "_din alder_ er jammen gammelt!"
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# navn = input("Hva heter du? ")
# print("Hei,", navn, "!")  # Du kan eventuelt bruke + istedenfor komma mellom strenger for å unngå mellomrom
# 
# alder = input("Hvor gammel er du? ")
# print(alder, "år er jammen gammelt!")
# ```
# ````

# ## Datamaskinen krever nøyaktige instrukser
# Når du lager sammensatte programmer med Python, må du huske på følgende:
# - Programmet leses fra topp til bunn og fra venstre til høyre.
# - Små bokstaver er IKKE lik store bokstaver (p $\neq$ P).
# - Python bryr seg lite om mellomrom, med mindre det er på starten av ei linje. Bruk mellomrom for å gjøre programmet ditt mer lesbart.
# - Øv deg på å lese feilmeldinger: Du får beskjed om linja der feilen befinner seg og typen feil.
# 
# ````{admonition} Underveisoppgave
# :class: tip
# Forklar hva som er feil med følgende programmer:
# 
# ```{code-block} Python
# tall1 = 1
# print(tall1 + tall2)
# tall2 = 3
# ```
# ```{code-block} Python
# navn = "Gunnar"
# print(Navn)
# ```
# ```{code-block} Python
# a = 2
# b = 3
# 
# print("Differansen mellom" a "og" b "=" a + b)
# ```
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# 1. Programmet leser fra topp til bunn. Derfor må vi definere tall2 før vi bruker det til addisjon. Linje 2 og 3 må derfor bytte plass.
# 
# 2. Variabelen _navn_ har liten _n_. Variabelen _Navn_ finnes ikke.
# 
# 3. For det første trenger vi komma mellom alle variabler i print-funksjonen. For det andre må det stå "summen", ikke differansen!
# 
# ```{code-block} Python
# print("Summen av", a, "og", b, "=", a + b)
# ```
# ````
# 
# ```{figure} https://live.staticflickr.com/3136/2842497804_f2684b2dcf_c.jpg
# ---
# height: 500px
# name: bug
# ---
# En av de første "bugs" ble funnet av Grace Hopper, som også lagde den første kompilatoren, en oversetter fra programmeringsspråk til maskinkode. Bugs var altså faktiske insekter som satt seg fast i de mekaniske delene og lagde krøll. Forhåpentligvis får du ingen feilmeldinger om insekter i datamaskinen din.
# ```

# ## Oppgaver
# ```{admonition} Oppgave 1.1
# :class: tip
# Bruk kodeboksen nedenfor til å lage relevante variabler slik at programmet regner ut arealet av en trekant med grunnlinje 4 og høyde 2. Programmet inneholder litt kode fra før til å hjelpe deg på vei.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# g = 4
# h = 2
# A = g*h/2
#  
# print("Arealet til trekanten er:", A)
# ```
# ````
# 
# ```{admonition} Oppgave 1.2
# :class: tip
# Lag et program som regner ut farten i m/s gitt følgende formel:
# 
# $$v = v_0 + at$$
# 
# Utvid programmet slik at startfarten, akselerasjonen og tida blir tatt som input.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# 
# Løsning uten input:
# ```{code-block} Python
# v0 = 1 # startfart i m/s
# a = 10 # akselerasjon i m/s^2
# t = 5  # slutt-tid i s
# 
# v = v0 + a*t
# 
# print("Sluttfarten blir:", v, "m/s")
# ```
# 
# Løsning med input:
# ```{code-block} Python
# v0 = float(input("startfart i m/s: "))
# a = float(input("akselerasjon i m/s^2: "))
# t = float(input("slutt-tid i s: "))
# 
# v = v0 + a*t
# 
# print("Sluttfarten blir:", v, "m/s")
# ```
# ````
# 
# ```{admonition} Ekstra: Oppgave 1.3
# :class: tip
# Lag et program som bruker en valgfri formel fra matematikken til å regne ut noe. Bruk input-funksjonen til å hente variabelverdier fra brukeren.
# ```
# 
# <iframe src="https://trinket.io/embed/python3/201ecb4ca2" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# ### Videoer
# Her kan du se videoer som introduksjon og/eller repetisjon til fagstoffet:
# 
# `````{tabbed} Variabler
# <iframe width="800" height="600" src="https://www.youtube.com/embed/RKws2FSSa28? autoplay=0&rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# 
# Når du har sett videoen, kan du gjøre følgende oppgave for å sjekke om du forstår innholdet:
# 
# ```{admonition} Sjekk deg selv
# :class: tip
# Lag et program der du definerer to variabler *tall1* og *tall2* med hver sitt tall. Regn ut differansen i en egen variabel. Skriv ut "Differansen mellom *tall1* og *tall2 er *differansen*".
# ```
# <iframe src="https://trinket.io/embed/python3/c16e9a9ea7" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# tall1 = 4
# tall2 = 2
# differansen = tall1 - tall2
# 
# print("Differansen mellom", tall1, "og", tall2, "er", differansen)
# ```
# ````
# `````
# 
# `````{tabbed} Aritmetikk
# <iframe width="800" height="600" src="https://www.youtube.com/embed/BASO7iHDV54? autoplay=0&rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# 
# Når du har sett videoen, kan du gjøre følgende oppgave for å sjekke om du forstår innholdet:
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Lag et program der du definerer massen til et legeme i en variabel, regner ut energien ved hjelp av formelen $E = mc^2$ og skriver dette ut. Regn med at $c = 3.0\cdot 10^8$ m/s.
# ```
# 
# <iframe src="https://trinket.io/embed/python3/8e4b3a9f07" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# m = 1     # Masse i kg
# c = 3.0E8 # Lysets hastighet i m/s
# 
# E = m*c**2
# 
# print("Energi:", E, "joule")
# ```
# ````
# `````
# 
# `````{tabbed} Biblioteker og matematiske operasjoner
# <iframe width="800" height="600" src="https://www.youtube.com/embed/VnFNYt2D2Ng? autoplay=0&rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# 
# Når du har sett videoen, kan du gjøre følgende oppgave for å sjekke om du forstår innholdet:
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Lag et program regner ut pH-en i en løsning gitt $[H_3O^+]$.
# ```
# 
# <iframe src="https://trinket.io/embed/python3/b8f775f773" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# from numpy import log10
# 
# H3O = 1E-6
# pH = -log10(H3O)
# 
# print("pH =", round(pH,2))
# ```
# ````
# `````
# 
# `````{tabbed} Input
# <iframe width="800" height="600" src="https://www.youtube.com/embed/nwncCwwcV4s? autoplay=0&rel=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# 
# Når du har sett videoen, kan du gjøre følgende oppgave for å sjekke om du forstår innholdet:
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Lag et program som tar masse og fart som input, og som regner ut kinetisk energi vha. formelen $E_k = \frac{1}{2}mv^2$.
# ```
# 
# <iframe src="https://trinket.io/embed/python3/07702bed1b?font=1.5em" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# m = float(input("masse i kg: "))
# v = float(input("fart i m/s: "))
# 
# E = 0.5*m*v**2
# 
# print("Den kinetiske energien er:", E, "joule")
# ```
# ````
# `````
