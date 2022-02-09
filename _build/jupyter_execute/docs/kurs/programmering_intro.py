#!/usr/bin/env python
# coding: utf-8

# # Programmering med ENT3R
# <img src="https://raw.githubusercontent.com/andreasdh/Programmering-og-modellering/master/docs/bilder/enter-logo.png" style="height:50px">
# <br />
# 
# Datamaskinen er et fantastisk verktøy som lar oss gjøre ting som nesten er umulig uten. La oss se litt på hva vi kan få til!
# 
# ## Gjett tallet
# 
# La oss starte med et lite "gjettespill". Spillet finner et tilfeldig tall mellom 0 og 100, og du må deretter gjette deg fram til hva tallet skal være. Kjør programmet ved å trykke på "play"-knappen over programkoden. Deretter skriver du inn gjettet ditt i ruta til høyre. Hvor mange forsøk bruker du?
# 
# <iframe src="https://trinket.io/embed/python3/87424e58ac" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# Husk at du ikke trenger å forstå alt som foregår i koden ovenfor enda, men kanskje du kan forstå noe?
# 
# ```{admonition} Oppgave
# :class: tip
# Prøv å forklare hva koden ovenfor gjør. Hvilke kodesnutter syns du gir mening, og hvilke syns du er vanskelig å forstå?
# ```

# I gjetteprogrammet bruker vi til slutt kommandoen _print_ for å gi beskjeden om at du har vunnet spillet. For å få noe ut av et program, må vi nemlig be datamaskinen om å "skrive ut" noe. Dette gjør vi med kommandoen _print_. Dersom vi ønsker å skrive ut flere variabler, må vi skille dem med komma i print-kommandoen. Her ser du to eksempler:
# 
# <iframe src="https://trinket.io/embed/python3/6fa8114dc6" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Eksperimenter med programmet ovenfor og forklar hvordan print fungerer. Gi gjerne variablene _navn_ og _alder_ en annen verdi. Bruk for eksempel ditt eget navn og alder eller navnet og alderen på noen du kjenner.
# ```
# 
# ```{admonition} Løsning
# :class: tip, dropdown
# Kommandoen _print_ gir oss et ouput fra programmet vårt. Vi sier at noe blir skrevet ut til "konsollen". Konsollen er der du får output i et programmeringsmiljø. Inni print-kommandoen kan vi skrive flere ting. Da må hver variabel og hver verdi være adskilt med komma.
# ```

# ## Løkker
# 
# Den kanskje viktigste strukturen i programmering er løkker. De lar datamaskinen gjenta en operasjon så mange ganger vi vil. Det er dette som er datamaskinens styrke.
# 
# ```{image} https://cdn.pixabay.com/photo/2015/06/08/15/02/roller-coaster-801833_960_720.jpg
# :alt: berg-og-dalbane
# :class: bg-primary mb-1
# :height: 300px
# :align: center
# ```
# 
# ## Skilpaddegrafikk
# Vi skal se hvordan løkker fungerer ved å introdusere deg for en skilpadde. Han heter Gunnar. Her er han:
# 
# <iframe src="https://trinket.io/embed/python/e00b86de83?font=1.5em" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# <br />
# 
# ```{image} https://cdn.pixabay.com/photo/2016/11/29/08/31/animal-1868436_960_720.jpg
# :alt: skilpadde
# :class: bg-primary mb-1
# :height: 200px
# :align: center
# ```
# 
# <br />
# 
# Gunnar følger enkle kommandoer, som "forward", "backward", "right" og "left".
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Endre programmet ovenfor slik at Gunnar tegner en trekant. Hva er sammenhengen mellom vinkelen som skilpadden snur og vinklene i trekanten?
# ```
# 
# ````{admonition} Løsning
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
# ```{admonition} Oppgave
# :class: tip
# Modifiser programmet ovenfor slik at skilpadden Gunnar tegner en 20-kant.
# ```
# 
# ```{admonition} Løsning
# :class: tip, dropdown
# Det er så enkelt som å endre _n_ til 20. Problemet er at 20-kanten blir litt stor, så vi kan også med fordel endre sidelengden, for eksempel til 25.
# ```
# 
# ```{admonition} Oppgave
# :class: tip
# Få Gunnar til å tegne et hus. Du velger hvor detaljert huset skal være, men du bør bruke løkker for å automatisere ting.
# ```
# 
# ````{admonition} Løsning
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

# ## Skilpaddekunst
# Du kan være ganske så kreativ med skilpaddegrafikk. Her er et eksempel på et lite kunstverk som du kan eksperimentere med og gjøre til ditt eget. Bruk gjerne oversikten nedenfor over ulike turtle-kommandoer og farger.
# <br />
# 
# ```{image} https://cdn.pixabay.com/photo/2018/03/04/23/25/sea-turtle-3199593_960_720.png
# :alt: skilpaddekunst
# :height: 200px
# :align: center
# ```
# <br />
# 
# <iframe src="https://trinket.io/embed/python/71c19b468b" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# `````{tabbed} Turtle-kommandoer
# ````{code-block} Python
# from turtle import *   # Importerer kommandoene vi trenger
# 
# forward(100)           # Går framover 100 skritt
# backward(100)          # Går bakover 100 skritt
# right(45)              # Snur 45 grader mot høyre
# left(45)               # Snurt 45 grader mot venstre
# goto((30,45))          # Går til koordinaten (30, 45)
# print(pos())           # Skriver ut posisjonen til pekeren
# penup()                # Slutter å tegne
# pendown()              # Begynner å tegne igjen
# 
# shape('turtle')        # Gir pekeren form som en skilpadde
# color('green')         # Fargelegger pekeren
# pencolor('red')        # Fargelegger det vi tegner
# pensize(10)            # Angir tykkelsen på strekene som tegnes
# speed(4)               # Tegnefart fra 1-10
# ````
# `````
# 
# `````{tabbed} Oversikt over fargenavn
# ![farger](https://matplotlib.org/2.0.2/_images/named_colors.png)
# `````

# ## Avsluttende oppgave
# ```{admonition} Avsluttende oppgave
# Lag logoen til ENT3R med Turtle-grafikk! Du kan gjerne være kreativ med farger og former. Ta også gjerne utgangspunkt i programmet nedenfor.
# 
# 
# <iframe src="https://trinket.io/embed/python/349b67c909" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# ```
