#!/usr/bin/env python
# coding: utf-8

# # Løkker
# 
# ```{admonition} Læringsutbytte
# Etter å ha arbeidet med dette temaet, skal du kunne:
# 1. bruke while- og for-løkker til å gjenta kode
# 2. tegne geometriske mønstre med turtle-grafikk
# 3. beregne rekkesummer
# 4. løse naturvitenskapelige problemer med løkker
# ```
# 
# ## Definisjon
# 
# Den kanskje viktigste strukturen i programmering er løkker. De lar datamaskinen gjenta en operasjon så mange ganger vi vil. Det er dette som er datamaskinens styrke.
# 
# ```{admonition} Løkker
# En løkke er en struktur som gjør at vi kan gjenta kode. Ofte skiller vi mellom en _telleløkke_, som gjentar noe et visst antall ganger, og en _tilstandsløkke_, som gjentar seg så lenge noe er sant. I Python heter disse henholdsvis _for_-løkke og _while_-løkke.
# ```
# 
# ## Skilpaddegrafikk
# Vi skal se hvordan løkker fungerer ved å introdusere deg for en skilpadde. Han heter Gunnar. Her er han:
# 
# <iframe src="https://trinket.io/embed/python/e00b86de83?font=1.5em" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# Gunnar følger enkle kommandoer, som "forward", "backward", "right" og "left".
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Endre programmet ovenfor slik at Gunnar tegner en trekant. Hva er sammenhengen mellom vinkelen som skilpadden snur og vinklene i trekanten?
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Du kan tegne hvilken som helst trekant, men dersom vi velger en likesidet trekant, må alle vinkler være 60 grader (slik at summen av de tre vinklene er 180 grader). Men vi kan ikke snu skilpadden 60 grader mot venstre. Da blir ikke den indre vinkelen i trekanten 60 grader. Det er altså forskjell på å snu 60 grader og lage en vinkel på 60 grader. Siden en helomvending er 180 grader, må skilpadden snu 180 - 60 = 120 grader for at vinklene i trekanten skal være 60 grader.
# 
# ```{code-block} Python
# from turtle import *
# 
# shape("turtle")    # gir pekeren skilpaddeform 
# color("limegreen") # gjør skilpadden limegrønn
# forward(100)       # går framover 100 steg
# left(120)          # vender 30 grader mot høyre (går ikke framover)
# forward(100)       # går framover 100 steg
# left(120)
# forward(100)
# ```
# ````
# 
# ### Skilpadder i løkker
# Å tegne en trekant krever få linjer kode, men hva hvis du vil tegne en åttekant, en førtitokant, eller en nittisekskant? Det er slitsomt og kjedelig å skrive samme kommando hundrevis av ganger. Og det er totalt unøvdendig. Vi bruker nemlig løkker til å gjenta kode, for eksempel slik:
# 
# <iframe src="https://trinket.io/embed/python/f047f7a36d?font=1.5em" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Prøv å forklare hvordan programmet ovenfor fungerer. Hva tror du "for i in range(n)" betyr? Hva tror du _i_ er?
# ```
# 
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# Programmet tegner en regulær (likesidet) mangekant. Vi velger først antall sider og en sidelengde. Vi regner så ut hva vinklene i mangekanten må være. Deretter går vi inn i en løkke. Helt enkelt kan vi si at løkka repeterer alt som står rykket inn (med tab) _n_ ganger. Skilpadden går altså framover (50) og snur (45), og dette gjentas _n_ ganger.
# ```
# 
# ```{admonition} Mer komplisert/grundig løsning
# :class: tip, dropdown
# Vi kan forklare programmet ovenfor litt grundigere med at "for i in range(n)" betyr at for hver verdi av en variabel _i_, skal løkka gjentas. Variabelen _i_ får hver verdi i intervallet [0, 1, 2, 3, ..., n-1], som lages med funksjonen _range_. Det betyr at første gang løkka kjører, er $i = 0$, andre gang $i = 1$ og så videre. Løkka gjentas helt til $i = n - 1$, altså til, men ikke med verdien _n_.
# ```
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Modifiser programmet ovenfor slik at skilpadden Gunnar tegner en 20-kant.
# ```
# 
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# Det er så enkelt som å endre _n_ til 20. Problemet er at 20-kanten blir litt stor, så vi kan også med fordel endre sidelengden, for eksempel til 25.
# ```
# 
# ```{admonition} Oppgave
# :class: tip
# Få Gunnar til å tegne et menneske eller en blomst.
# ```
# 
# ````{admonition} Løsning
# :class: tip, dropdown
# Mulighetene er uendelige, men her er et vakkert eksemplar av et menneske
# ```{code-block} Python
# from turtle import *
# 
# n = 100
# vinkel = 360/n
# 
# for i in range(n):
#   forward(3)
#   left(vinkel)
#   
# right(90)
# forward(50)
# 
# for i in range(2):
#   left(120)
#   forward(75)
#   backward(75)
# 
# left(120)
# forward(50)
# 
# right(30)
# forward(75)
# backward(75)
# left(60)
# forward(75)
# ```
# ````

# ## While-løkker
# Vi har to typer løkker i Python: while-løkker (tilstandsløkker) og for-løkker (telleløkker). While-løkker gjentar noe helt til et kriterium er nådd. Her er et eksempel:
# 
# <iframe src="https://trinket.io/embed/python3/aae1a3f582?font=1.5em" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# Programmet kjører så lenge variabelen _partall_ har en verdi som er mindre enn eller lik 10. Alt som er rykket inn, gjentas hver gang løkka går. Programmet skriver derfor ut alle positive partall (og 0) som er mindre enn eller lik 10.
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Modifiser programmet ovenfor slik at programmet skriver ut alle positive _oddetall_ under 10.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# oddetall = 1
# 
# while oddetall < 10:
#     print(oddetall)
#     oddetall = oddetall + 2
# ```
# ````

# ## For-løkker
# I for-løkker lager vi en _teller_ eller _tellevariabel_ som går igjennom en slags liste med tall. Denne listeliknende tallmengden kan vi lage med funksjonen _range_. Her er noen eksempler:
# 
# | kommando | liste |
# | -------- | --------- |
# | range(3) | [0, 1, 2] |
# | range(2,4) | [2, 3] |
# | range(1,8,2) | [1, 3, 5, 7] |
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Forklar hvordan _range_-funksjonen fungerer med utgangspunkt i eksemplene ovenfor.
# ```
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# Vi kan skrive en generell range-kommando slik: range(fra og med, til, steglengde). Vi kaller de tre tallene i range-funksjonen for _argumenter_. Dersom vi kun bruker ett argument, for eksempel _range(3)_, får vi en mengde fra 0 til, men ikke med, 3 (som er spesifisert), med steglengde 1, altså er hvert heltall med. Dersom vi bruker to argumenter, som i _range(2,4)_, får vi en tallmengde fra 2 til, men ikke med, 4, med en automatisk steglengde på 1. Dersom vi bruker tre argumenter, gir vi også steglengden, for eksempel hvert andre tall mellom 1 og 8, som i _range(1,8,2)_.
# ```
# 
# Et enkelt eksempel på en for-løkke er slik:
# ```{code-block} Python
# for i in range(5):
#     print(i)
# ```
# Vi kan også gjøre noe mer enn å telle i løkka:
# 
# ```{code-block} Python
# a = 2
# for i in range(5):
#     print(i)
#     a = a + i
#     
# print(a)
# ```
# Så hva betyr dette? Helt enkelt betyr det at alt som er rykket inn (med tab eller fire mellomrom), blir gjentatt 5 ganger. Operasjonen der vi oppdaterer _a_ er 
# 
# Hvis vi skal forklare litt mer presist hva som skjer, kan vi si at _range_-funksjonen lager en tallmengde [0, 1, 2, 3, 4], og at _i_ blir tilordnet hver av disse verdiene etter tur. Første gang løkka går, er $i = 0$. Da printes denne verdien, og $a = 2 + 0 = 2$. Deretter gjentas alt inni løkka på nytt, og _i_ får verdien 1. Så gjentas det som står rykket inn en gang til: Vi printer 1, og $a = 2 + 1 = 3$. Slik fortsetter det til og med $i = 4$. Når _i_ har hatt alle verdiene i tallmengden, avsluttes løkka.
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Vi kan systematisere løkkene med en _løkketabell_. Den holder styr på hva verdien til de ulike variablene er underveis i løkka. Fyll inn resten av løkketabellen for løkka ovenfor.
# 
# | Løkkerunde | i | a |
# |---|---|---|
# |Startverdi| - | 2 |
# | 1 | 0 | 2 |
# | 2 | 1 | 3 |
# | 3 | | |
# | 4 | | | 
# | 5 | | |
# ```
# 
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# | Løkkerunde | i | a |
# |---|---|---|
# |Startverdi| - | 2 |
# | 1 | 0 | 2 |
# | 2 | 1 | 3 |
# | 3 | 2 | 5 |
# | 4 | 3 | 8 | 
# | 5 | 4 | 12 |
# ```
# 
# I for-løkker kaller vi ofte tellevariabelen for _i_, _j_, _k_ eller liknende, men den kan egentlig hete hva som helst. I tillegg trenger vi ikke å _gjøre_ noe med tellevariabelen. Mange ganger brukes den bare for å telle. Her er et eksempel:
# 
# <iframe src="https://trinket.io/embed/python3/8596417056?font=1.5em" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Modifiser programmet ovenfor slik at det skriver ut hvor mye penger du har etter et visst antall år. Lag en variabel som inneholder antall år, og som du bruker i løkka. Legg også inn hensiktsmessige kommentarer.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# penger = 100   # kroner i banken
# renter = 1.025 # Rente (1+x%/100) 
# tid = 25       # Antall år pengene står i banken
# 
# for år in range(tid):
#     penger = penger*renter
#   
# print("Etter", tid, "år har du", round(penger, 2), "kroner i banken.")
# ```
# ````
# 
# ## Å tenke i løkker
# Løkker kan brukes til alt fra å summere tallrekker i matematikk til å finne ut hvor mange harer det er i økosystem etter en viss tid, finne posisjonen til et legeme eller utforske hvordan kjemiske reaksjoner foregår. Når vi skal bruke løkker, må vi dele opp problemer slik at de kan utføres trinnvis. I matematikk og naturvitenskapelige fag er det ofte slik at vi representerer sammenhenger med kontinuerlige funksjoner og formler, men når vi løser problemene med løkker, gjør vi det trinnvis. For hvert trinn, gjør vi en bestemt operasjon. Dette kalles å løse noe _iterativt_, fordi _iterasjon_ betyr gjentakelse. Litt mer uformelt kan vi kalle det å løse noe trinnvis med små, repeterende operasjoner "å tenke i løkker". La oss se på noen eksempler fra både matematikk og naturvitenskap.
# 
# ### Tallfølger
# En tallfølge er en oppramsing av tall som kan være enten endelig eller uendelig. Et eksempel på en endelig tallfølge er 2, 4, 6, 8, 10, som er en tallfølge av de 5 første partallene. En berømt uendelig tallfølge er _Fibonacci-tallene_: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ..., der de tre siste prikkene sier oss at rekka er uendelig lang. Fibonacci-tallene starter på 1, og hvert tall er deretter summen av de to foregående tallene.
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Beskriv mønsteret i følgen 1, 3, 5, 7, ... og skriv opp det neste tallet i følgen.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Hvert tall er lik summen av det forrige tallet og 3. Det neste tallet må derfor være 7 + 3 = 10.
# ````
# 
# Hvert tall i en tallfølge kalles et _ledd_. Vi kan beskrive hvert ledd i en følge med symboler, for eksempel $a_n$, der _n_ er en indeks som beskriver leddnummeret. I tallfølgen 1, 3, 5, 7, ... kan for vi for eksempel si at $a_1 = 1$ og $a_2 = 3$. Poenget med å beskrive en følge med symboler, er at vi kan lage formler for hvert generelle ledd $a_n$. Følgen 1, 3, 5, 7, ... kan beskrives med den generelle formelen $a_{n+1} = a_n + 2$, der $a_1 = 1$. En slik formel kalles en _rekursiv formel_ fordi vi tar utgangspunkt i en tidligere verdi for å regne ut neste verdi.
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Forklar hvorfor $a_{n+1} = a_n + 2$ er det samme som $a_n = a_{n-1} + 2$.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Formlene beskriver det samme, men med ulike indekser. Begge sier at neste tall er lik forrige tall + 2. Den første formelen vil starte med _n = 0_. Da har vi at $a_1 = a_0 + 2$. Den andre formelen vil starte med _n = 1_. Da har vi også at $a_1 = a_0 + 2$.
# ````
# Når vi først har kommet fram til en generell formel for en tallfølge, kan vi finne det _n_-te leddet ved hjelp av programmering. Vi bruker tallfølgen 1, 3, 7, 15, 31, ... som eksempel. Denne følgen kan vi beskrive med formelen $a_{n+1} = a_n + 2^n$. La oss finne det hundrede leddet i denne følgen:
# 
# <iframe src="https://trinket.io/embed/python3/112c41d19b?font=1.5em" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# ```{admonition} Underveisoppgave
# :class: tip
# Forklar hva som skjer i programmet ovenfor. For å sjekke om programmet vårt fungerer, kan det være lurt å beregne tall som vi kjenner i følgen. Prøv å finne tall nr. 3, 4 og 5 for å sjekke at programmet gjør det det skal.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Programmet definerer først et tall som er med i tallfølgen, deretter hvilket ledd (nummer) vi ønsker å finne i følgen. Løkka går fra 1 til (men ikke med) _n_. Det er fordi vi allerede har et tall i følgen, $a_0 = 1$. Da trenger bare løkka å gå to ganger for å finne ledd nr. 3, og for eksempel 6 ganger for å finne ledd nr. 7, og så videre. Hvis vi teller fra 0, er tall nummer 3 lik $a_2 = 7$, tall 4 er $a_3 = 15$ og tall 5 er $a_4 = 31$
# ````
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Endre programmet ovenfor slik at det finner det 20. elementet i tallfølgen 1, 5, 11, 19, 29, ...
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Tallfølgen ovenfor kan beskrives med den rekursive formelen $a_{n+1} = a_{n} + 2n + 2$. Vi kan finne det tjuende elementet slik:
# ```{code-block} Python
# a = 1   # første verdi i tallfølgen
# n = 20 # n-te ledd i tallfølgen
# 
# for i in range(1, n):
#     a = a + 2*i + 2
# 
# print("Tall nummer", n, "i følgen er:", a)
# ```
# Det tjuende elementet er 419.
# ````
# 
# ### Tallrekker
# Når vi beskriver en tallfølge som en serie med tall som adderes med hverandre, kaller vi det for en _rekke_. For eksempel er 1, 5, 11, 19, 29, ... en tallfølge, mens 1 + 5 + 11 + 19 + 29 + ... er en tallrekke. Vi kan summere slike rekker, selv om de er uendelige.
# 
# Noen rekkesummer går mot uendelig  mens andre går mot en bestemt verdi. Vi kan utlede formler for å regne ut summen av slike rekker, men vi kan også lage programmer som gjør det. La oss si at vi har denne rekka (ei såkalt uendelig geometrisk rekke):
# 
# $1 + \frac{2}{3} + \frac{4}{9} + \frac{8}{27} + ...$
# 
# Vi kan regne ut summen av denne rekka ved å først kjenne igjen et mønster i tallmengden. Vi kan vise at det _n_-te tallet i rekka er $\left(\frac{2}{3}\right)^n$. Deretter kan vi programmere ei løkke som legger sammen så mange av disse tallene som mulig. Vi tilnærmer altså den uendelige rekka med et endelig antall ledd. Det kan vi gjøre slik

# In[1]:


N = 100
S = 0

for n in range(N):
    S = S + (2/3)**n  # summen er lik forrige sum + sum av nytt tall
print(S)


# Den nøyaktive, analytiske verdien vi kan få dersom vi uleder en summeformel for rekka, er 3 (uten desimaltall). Men når vi legger sammen de 100 første tallene i programmet ovenfor, får vi faktisk  et tall som er ganske nærme. Det er ikke verst! Vi får sjeldent helt nøyaktige svar når vi bruker slike metoder, men vi kommer ganske nærme.

# ### Naturvitenskapelige problemer
# 
# Det som er ekstra morsomt med å løse problemer iterativt, er at vi ofte løser ting på samme måte på tvers av ulike fag. Se bare på de tre ulike programmene nedenfor, fra fagområdene fysikk og biologi. Du kan også sammenlikne med det du har lært om følger og rekker.

# In[17]:


# Fysikkeksempel

tid = 10    # slutt-tid i sekunder
dt = 0.001  # tidssteg mellom hver iterasjon
t = 0       # start-tid
a = 9.8     # akselerasjonen til et legeme

v = 0       # startfart i m/s
s = 0       # startposisjon i m

while t <= tid:
    v = v + a*dt # bevegelsesformel for hastighet (konstant a)
    s = s + v*dt # bevegelsesformel for posisjon (konstant v)
    t = t + dt   # oppdaterer tida med dt

print("I løpet av", tid, "sekunder falt steinen", s, "m.")


# ```{admonition} Underveisoppgave
# :class: tip
# Beskriv hva programmet ovenfor gjør. Problemet kan løses relativt enkelt ved hjelp av formler, men kan du tenke deg hvorfor denne måten å gjøre det på kan være nyttig likevel?
# ```

# In[22]:


B0 = 100          # antall bakterier ved t = 0
B = B0
antall_timer = 30 # slutt-tid i timer
t = 0             # start-tid
vekst = 1.20      # vekstfaktor

for i in range(antall_timer):
    B = B*vekst

print("Antall bakterier er:", int(B))


# ```{admonition} Underveisoppgave
# :class: tip
# Forklar hva programmet ovenfor gjør. Dette programmet gjør det samme som å sette t = 30 inn i funksjonen $B(t) = 100\cdot 1.20^t$. Hva beskriver denne funksjonen, og hvorfor kan det være nyttig å lage et program for å regne ut dette når det er såpass lett å løse analytisk?
# ```

# De to programmene ovenfor benytter samme løsningsstrategi: Ut fra en startbetingelse (startposisjon og startfart eller antall bakterier til å begynne med) regner vi ut utviklingen over tid i et system (enten posisjonen til en stein som faller, eller antall bakterier til slutt), gitt noen premisser for systemet (henholdsvis akselerasjon og vekstfaktor). Det er altså mange likheter mellom måten vi løser problemene på.
# 
# Fordelen ved å bruke programmering til å løse slike problemer, er at det er lett generaliserbart. Selv om det finnes formler som ganske nøyaktig kan beskrive posisjonen til steinen ved enhver tid, er det ikke så lett å forutse posisjonen til en fallskjermhopper, der akselerasjonen varierer ganske mye, eller veksten til bakterier hvis den avhenger av temperatur. Alt dette er relativt enkelt å legge til i programmene våre, mens de analytiske (formelbaserte) løsningene blir veldig kompliserte, og ofte uløselige.
# 
# For eksempel kan vi enkelt legge inn en temperaturavhengighet i bakterieveksten vår slik:

# In[24]:


B = 100
antall_timer = 30
vekst_liste = [1.20, 1.30, 1.42, 1.48]
temperatur = 30

for i in range(antall_timer): 
    if 30 <= temperatur <= 40: 
        vekst = vekst_liste[0]
    elif 40 < temperatur < 52: 
        vekst = vekst_liste[1]
    elif 53 <= temperatur <= 65: 
        vekst = vekst_liste[2]
    else:
        vekst = vekst_liste[3] 
    B = B*vekst 
    temperatur = temperatur + 1

print("Antall bakterier er:", int(B))


# Nå har vi egentlig lagd ulike modeller for to forskjellige systemer. Utvikling, testing og utforsking av modeller skal vi se mye på seinere. Her er hovedpoenget at du skal se hvordan løkker kan brukes til å løse problemer på en effektiv, robust og relativt intuitiv måte.

# ## Nøstede løkker
# Nøstede løkker er løkker inni løkker. Da gjelder det å holde tunga rett i munnen. La oss bruke et eksempel for å forklare hvordan det virker:

# In[3]:


print("i | j")
print("-----")
for i in range(2):
    for j in range(1,3):
        print(i,"|", j)


# Vi ser at den innerste løkka, som bruker _j_ som tellevariabel, gjentas to ganger for hver gang den ytterste løkka går. Først er altså _i = 0_. Det er første runde i den ytre løkka. Mens _i = 0_ går den indre løkka to ganger, en gang for _j = 1_ og en gang for _j = 2_. Deretter går neste runde i den ytre løkka, og _i = 1_. Den indre løkka går igjen to ganger, en gang for _j = 1_ og en gang for _j = 2_. Totalt har vi altså gått fire løkkerunder.
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Lag et program som printer ut denne løkketabellen:
# 
# | a | b |
# |---|---|
# |1|0|
# |1|2|
# |1|4|
# |2|0|
# |2|2|
# |2|4|
# |3|0|
# |3|2|
# |3|4|
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# print("i | j")
# print("-----")
# for i in range(1,4):
#     for j in range(0,5,2):
#         print(i,"|", j)
# ```
# ````

# ## Oppgaver
# `````{tabbed} Grunnleggende
# ````{admonition} Oppgave 4.1
# :class: tip
# Sammenlikn programmene nedenfor. Beskriv eventuelle forskjeller og likheter.
# 
# ```{code-block} Python
# partall = 0
# 
# for i in range(5):
#     partall = partall + 2
#     print(partall)
# ```
# ```{code-block} Python
# partall = 0
# 
# while partall < 10:
#     partall = partall + 2
#     print(partall)
# ```
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Begge programmene gir samme input. I det første programmet bruker vi en telleløkke som gjentar en operasjon (legger til 2 til variabelen partall) 5 ganger. I det andre programmet bruker vi en tilstandsløkke som legger 2 til partallsvariabelene helt til partall ikke er mindre enn 10.
# ````
# 
# ````{admonition} Oppgave 4.2
# :class: tip
# Lag en løkketabell med utgangspunkt i følgende kode:
# ```{code-block} Python
# a = 0
# 
# for i in range(5):
#     a = a + 1
#     b = a*i
# ```
# ````
# ```{admonition} Løsningforslag
# :class: tip, dropdown
# | Løkkerunde | i | a | b |
# |------------|---|---|---|
# | Startverdi | - | 0 | - |
# | 1          | 0 | 1 | 0 |
# | 2          | 1 | 2 | 2 |
# | 3          | 2 | 3 | 6 |
# | 4          | 3 | 4 | 12|
# | 5          | 4 | 5 | 20|
# ```
# 
# ```{admonition} Oppgave 4.3
# :class: tip
# Lag et program som skriver ut "Du er flink til å programmere!" tusen ganger. Hvilken funksjon har "tellevariabelen" (_i_) her?
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# for i in range(1000):
#     print("Du er flink til å programmere!")
# ```
# Vi bruker ikke tellevariabelen til utregning eller output, men den teller i bakgrunnen slik at løkka går 1000 ganger. Hver gang løkka går, får variabelen _i_ en ny verdi (først 0, så 1, så 2, osv. opp til 999).
# ````
# 
# ```{admonition} Oppgave 4.4
# :class: tip
# Programmet nedenfor skal finne summen av de 100 første tallene i en tallfølge der hvert ledd er den dobbelte av det forrige. Forklar hvordan programmet fungerer. Endre gjerne på ulike variabler og test hva utfallet blir for å forstå hvordan programmet fungerer.
# 
# <iframe src="https://trinket.io/embed/python3/51f01c11f8?font=1.5em" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Vi starter med å definere variablene våre. Variabelen _tall_ representerer et tall som dobles hver gang vi kjører løkka, _summen_ inneholder summen av alle disse tallene, og øker med _tall_ hver gang løkka kjører. Tellevariabelen _i_ sørger for at vi legger sammen 100 tall (den går fra 0 til 99), og har ingen funksjon utenom dette. Til slutt skriver vi ut summen av alle disse tallene.
# ````
# 
# ```{admonition} Oppgave 4.5
# :class: tip
# Skriv om programmet ovenfor slik at du benytter en while-løkke istedenfor en for-løkke.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# tall = 1
# summen = 0
# i = 0
# 
# while i < 100:
#   summen = summen + tall
#   tall = tall*2
#   i = i + 1
# 
# print(summen)
# ```
# ````
# 
# ````{admonition} Oppgave 4.6
# :class: tip
# Hva skrives ut i følgende program? Prøv å undersøke dette for hånd. Til slutt kan du sjekke ved å kopiere programmet inn i en editor og kjøre det.
# 
# ```{code-block} Python
# a = 0
# 
# for i in range(5):
#     b = a*i
#     print(b)
#     a = a + 1
# print(a)
# ```
# ````
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Husk at print som skjer inni løkka gjør at vi får output hver gang løkka går, mens print utenfor løkka gir sluttverdien til variabelen etter at løkka har kjørt. Siden _i_ får verdien 0, 1, 2, 3 og 4, får _b_ verdien 0, 1, 4, 9 og 16, siden _a_ øker med 1 hver gang løkka går. Det betyr at 0, 1, 4, 9, 16 skrives ut, etterfulgt av sluttverdien til _a_, 5.
# ````
# 
# ```{admonition} Oppgave 4.7
# :class: tip
# Bruk turtle-grafikk til å tegne et hus. Du bestemmer selv hvor detaljert huset skal være.
# ```
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Mulighetene er uendelige, men her er et enkelt forslag:
# ```{code-block} Python
# from turtle import *
# 
# for i in range(4):
#   forward(100)
#   right(90)
#   
# for i in range(3):
#   forward(100)
#   left(120)
# ```
# ````
# 
# `````
# 
# `````{tabbed} Matematikk
# ```{admonition} Oppgave 4.8
# :class: tip
# Bruk turtle-grafikk til å tegne en hundrekant. Hva slags form minner dette deg om?
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# from turtle import *
# 
# sidelengde = 5
# n = 100
# vinkel = 360/n
# 
# for i in range(n):
#   forward(sidelengde)
#   left(vinkel)
# ```
# Hundrekanten minner om en sirkel. Det er faktisk slik at når _n_ nærmer seg uendelig, får vi en perfekt sirkel! En sirkel er altså en slags uendeligkant.
# ````
# 
# ```{admonition} Oppgave 4.9
# :class: tip
# Programmet nedenfor skal regne ut hvor lang tid det tar før du har doblet beløpet ditt i banken gitt en årlig rente på 5 \% og en startkapital på 5000 kroner, men programmet fungerer ikke som det skal. Hva er feil? Rett opp programmet slik at det fungerer.
# 
# <iframe src="https://trinket.io/embed/python3/156cd31940?font=1.5em" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Feilen er ikke kodeteknisk, men matematisk. Vi må enten definere rente som 1.05 eller gjøre slik i løkka:
# ```{code-block} Python
# startkapital = 5000
# penger = startkapital
# år = 0
# rente = 0.05
# 
# while penger < startkapital*2:
#   penger = penger + penger*rente
#   år = år + 1
#   
# print("Det tar", år, "år å doble beløpet.")
# ```
# ````
# 
# ```{admonition} Oppgave 4.10
# :class: tip
# Lag et program som regner ut denne summen:
# $\sum_{n = 0}^{50} \frac{1}{2^n}$
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# s = 0
# n = 0
# while n <= 50:
#     s = s + 1/2**n
#     n = n + 1
# print("Summen er lik:", s)
# ```
# ````
# 
# ```{admonition} Oppgave 4.11
# :class: tip
# Lag et program som regner ut denne summen:
# 
# $\sum_{n = 2}^{16} n^2 + n + 1$
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# s = 0
# n = 2
# while n <= 16:
#     s = s + (n**2 + 1 + n)
#     n = n + 1
# print("Summen er lik:", s)
# ```
# ````
# 
# ```{admonition} Oppgave 4.12
# :class: tip
# Fibonnacifølgen er en kjent tallfølge med heltall der hvert tall etter det første er summen av de to foregående. Følgen starter slik: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# 
# Lag et program som finner tall nr. _n_ i rekka.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# x0 = 0
# x1 = 1
# n = 100
# 
# for i in range(n):
#     print(f'Fibonaccitall nr. {i+1} er: {x1}')
#     x0_ny = x1
#     x1 = x1 + x0
#     x0 = x0_ny
# ```
# ````
# 
# ```{admonition} Oppgave 4.13
# :class: tip
# Lag et program som viser at summen av denne rekka er 4.5:
# 
# $\displaystyle 3 + 1 + \frac{1}{3} + \frac{1}{9} + \frac{1}{27} + ...$
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# Rekka kan skrives slik: $3 + \sum^{\infty}{i=0} \frac{1}{3**i}$. Vi kan ikke summere et uendelig antall ledd på en datamaskin. Derfor tilnærmer vi svaret ved å bruke svært mange ledd, for eksempel 10 000.
# 
# ```{code-block} Python
# N = 10000
# s = 3
# for i in range(N+1): # for at rekka summes fra og med 0 til og med N
#     s = s + 1/3**i
# print(s)
# ```
# ````
# 
# ```{admonition} Oppgave 4.14
# :class: tip
# I kombinatorikk er _n-fakultet_ definert som produktet av alle heltall fra og med 1 til og med _n_. Dette kan vi skrive slik:
# 
# $n! = \prod_{k=1}^{n} k$
# 
# Lag en funksjon som regner ut fakultetet av et tall.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# n = int(input("Skriv inn n:"))
# fakultet = 1
# for k in range(1, n+1) :
#     fakultet = fakultet*k
# print("n! =", fakultet)
# ```
# ````
# `````
# 
# `````{tabbed} Naturvitenskap
# ```{admonition} Oppgave 4.15 (biologi)
# :class: tip
# Tøffeldyr formerer seg ukjønnet annenhver time dersom de befinner seg i en omgivelse med temperatur på $20 ^{\circ}C$.
# 
# Skriv et program som regner ut og skriver ut hvor mange tøffeldyr det vil være dersom vi begynner med 5 tøffeldyr som formerer seg ukjønnet i løpet av 24 timer. Du kan anta at ingen tøffeldyr dør.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# toeffeldyr = 5
# for time in range(2, 25, 2):
#     toeffeldyr = toeffeldyr*2
# print("Antall tøffeldyr etter 24 timer :", toeffeldyr)
# ```
# ````
# 
# ```{admonition} Oppgave 4.16 (fysikk)
# :class: tip
# Vi kan bruke Bohrs formel til å regne ut frekvensen til et foton som emitteres når et elektron i et hydrogenatom deeksiterer fra skall $n$ til $m$:
# 
# $$f =\frac{B}{h}\cdot \left( \frac{1}{m^2} - \frac{1}{n^2} \right)$$
# 
# der $B = 2.18\cdot 10^{-18} J$ er Bohrs konstant, $h = 6.63\cdot 10^{-34}$ m$^2$kg s$^{-1}$. Vi har også en sammenheng mellom frekvens og bølgelengden til fotonene:
# 
# $$\lambda = \frac{c}{f}$$
# 
# der $c = 3.00\cdot10^8$ m/s er lysets hastighet i vakuum.
# 
# a) Lag et program som skriver ut bølgelengden ti lyset som emitteres ved en gitt deeksitasjon. Test programmet ved deeksitasjon fra $n = 5$ til $n = 2$. Dette skal gi $\lambda = 434.47 \ nm$.
# 
# b) Lag et program som regner ut alle bølgelengdene til fotonene som emitteres når atomet deeksiterer fra et skall _n_ til alle mulige energinivåer _m_.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# a)
# 
# ```{code-block} Python
# B = 2.18E-18
# h = 6.63E-34
# c = 3e8
# 
# n = 5
# m = 2
# 
# f = B/h *(1/ m**2 - 1/n **2)
# bl = c/f            # bølgelengde i meter
# bl_nm = bl*1E9      # bølgelengde i nanometer
# print("Bølgelengden til fotonet fra n =", n, "til m =", m, ":", round(bl_nm,2), "nm")
# ```
# 
# b)
# ```{code-block} Python
# n = int(input("Skriv inn en verdi for n:"))
# 
# B = 2.18E-18
# h = 6.63E-34
# c = 3e8
# for m in range(n-1, 0, -1): # Går baklengs, men kan godt gå forlengs med range(1, n)
#     f = B/h *(1/ m**2 - 1/n **2)
#     bl = c/f            # bølgelengde i meter
#     bl_nm = bl*1E9      # bølgelengde i nanometer
#     print("Bølgelengden til fotonet fra n =", n, "til m =", m, ":", round(bl_nm,2), "nm")
# ```
# ````
# 
# ```{admonition} Oppgave 4.17 (fysikk)
# :class: tip
# Over tid vil den radioaktive strålingen i et radioaktivt stoff reduseres. Dette skjer fordi atomene i det radioaktive stoffet vil omdannes til andre grunnstoffer. Mengden $N(t)$ som gjenstår av det radioaktive stoffet etter ei tid $t$ kan finnes ved:
# 
# $N(t) = N_0e^{-at}$
# 
# der $N_0$ er hvor mye radioaktivt stoff vi starter med ved tida $t = 0$. Verdien til $a$ forteller hvor raskt det radioaktive stoffet omdannes til andre grunnstoffer. Hvis vi kjenner halveringstida $T$, vil $a = \frac{\ln(2)}{T}$.   
# 
# Plutonium-239 har halveringstid på omtrent $T = 24\ 000$ år. 
# Skriv et program som skriver ut hvor mye Plutonium-239 som gjenstår etter hvert 5000. år over en periode på 50 000 år dersom $N_0 = 4$ kg. 
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# from numpy import log, exp
# N0 = 4
# a = log(2)/24000
# 
# for t in range(0, 50001, 5000):
#     N = N0*exp(-a*t)
#     print("Etter ", t, "år gjenstår", N0*exp(-a*t), "kg av Plutonium-239.")
# ```
# ````
# `````

# ## Videoer
# I videoene nedenfor kan du få en innføring eller repetisjon i den grunnleggende teorien bak løkker:
# 
# `````{tabbed} For-løkker
# <iframe width="800" height="600" src="https://www.youtube.com/embed/C3W_5_NjHFw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# 
# Når du har sett videoen, kan du gjøre følgende oppgave for å sjekke om du forstår innholdet:
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Skriv et program som regner ut summen av alle heltallene fra og med 1 til og med 449 ved hjelp av en for-løkke.
# ```
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# s = 0
# 
# for tall in range(1, 450):
#     s = s + tall
#     
# print("Summen er:", s)
# ```
# ````
# 
# `````
# `````{tabbed} While-løkker
# <iframe width="800" height="600" src="https://www.youtube.com/embed/8VXQ2jw6Dpw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
# 
# Når du har sett videoen, kan du gjøre følgende oppgave for å sjekke om du forstår innholdet:
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Skriv et program som regner ut summen av tallene fra og med 1 til og med 449 ved hjelp av en while-løkke.
# ```
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# s = 0
# tall = 1
# 
# while tall <= 449:
#   s = s + tall
#   tall = tall + 1
# 
# print("Summen er:", s)
# ```
# ````
# `````
