#!/usr/bin/env python
# coding: utf-8

# # Datahåndtering I: Visualisering
# 
# ```{admonition} Læringsutbytte
# Etter å ha arbeidet med dette temaet, skal du kunne:
# 1. bruke matplotlib-biblioteket til visualisering
# 2. plotte datapunkter og funksjoner
# 3. lage og tolke ulike visualiseringer
# ```
# Håndtering av data blir stadig viktigere i dagens samfunn. En viktig del av datahåndtering er å kunne generere fine og informative figurer som beskriver dataene på en god måte. Det blir stadig vanligere å bruke programmering til dette. Det finnes flere typer biblioteker som kan gi oss fine og profesjonelle figurer. Vi begynner med et mye brukt bibliotek som heter _matplotlib_. Hvis du foretrekker å importere _pylab_ istedenfor, kan du godt gjøre det. Pylab-biblioteket inneholder også alle de samme plotteverktøyene.
# 
# ## Plotting av lister
# Hvis vi har få datapunkter, kan vi skrive dem inn i lister direkte i programmet vårt og plotte dem. La oss si at vi har samlet data for hvor raskt en hurtigvoksende plante vokser annenhver dag. Vi registerer dagene og høyden til planten i cm, og legger disse verdiene inn i lister.

# In[7]:


import matplotlib.pyplot as plt       # importerer relevante plotteverktøy

tid = [0, 2, 4, 6, 8, 10, 12, 14]     # tid i dager
plantehøyde = [0, 1, 4.2, 7.9, 12.5, 13, 13.7, 13.9] # høyde i cm

plt.plot(tid, plantehøyde)            # plotter plantehøyde mot tid
plt.show()                            # viser plottet


# Hvis vi har lyst til å modifisere og pynte på plottet, har vi mange muligheter til det. Her er noen forslag til en del nyttige endringer av plottet ovenfor:

# In[9]:


plt.plot(tid, plantehøyde, color = 'limegreen', marker = 'o', linestyle = '--')
plt.title("Forsøk: Plantevekst")      # tittel
plt.xlabel("Tid (dager)")             # x-aksetittel
plt.ylabel("Plantens høyde (cm)")     # y-aksetittel
plt.xlim(0,15)   # definisjonsmengde
plt.ylim(0,20)   # verdimengde
plt.grid()       # tegner rutenett
plt.show()


# Det finnes utrolig mange måter å modifisere et plott på. Tabellene nedenfor viser en oversikt over nyttige plottekommandoer, linjestiler, markører og farger, som du kan bruke for å lage akkurat den figuren du ønsker. Du bør også søke litt rundt på nettet for å finne andre muligheter, for eksempel ved å søke på «python plotting colors» og liknende. Du må bruke internett flittig når du lurer på noe i programmering!
# 
# En veldig nyttig kommando når vi skal representere flere grafer i samme koordinatsystem, er _legend_. Denne kommandoen viser merkelappene ("labels") til de ulike plottene. Programmet nedenfor gir et eksempel på dette.
# 
# ```{admonition} Underveisoppgave
# :class: tip
# Programmet nedenfor plotter miljøgifter i ulike organismer i to innsjøer. Studer programmet og eksperimenter med ulike verdier fra tabellen nedenfor.
# ```
# 
# <iframe src="https://trinket.io/embed/python3/ffda9bdd1b" width="100%" height="400" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>

# ````{tabbed} Nyttige plottekommandoer
# ```{code-block} Python
# plot(x,y)         # plotter x mot y og trekker rette linjer mellom
# scatter(x,y)      # plotter kun punkter
# show()            # viser plottet
# 
# title("tittel")   # tittel på plottet
# xlabel("tekst")   # x-aksetittel
# ylabel("tekst")   # y-aksetittel
# xlim(fra, til)    # definisjonsmengde
# ylim(fra, til)    # verdimengde
# grid()            # rutenett på
# 
# axhline(y=0, color='black') # x-akse
# axvline(x=0, color='black') # y-akse
# 
# savefig("filnavn.png") # lagrer bildet med god oppløsning
# ```
# Inni plottekommandoen kan vi også legge til farger, linjestiler, markører, merkelapper og liknende:
# 
# ```{code-block} Python
# plot(x,y,color="",marker="",linestyle="",label="")
# ```
# ```` 
# 
# ````{tabbed} Markører
# | Markør | Forklaring |
# | -----  | ---------- |
# | "." | punkt |
# | "o" | sirkel |
# | " " (mellomrom) | ingen markør |
# | "^" | triangel opp |
# | "v" | triangel ned |
# | "s" | firkant |
# | "p" | femkant |
# ```` 
# 
# ````{tabbed} Linjestiler
# | Linjestil | Forklaring |
# | -----  | ---------- |
# | "-" | heltrukket linje |
# | "--" | stipla linje (lange) |
# | ";" |  stipla linje (korte) |
# | "-." | stilpa linje (annenhver kort/lang) |
# | " " (mellomrom) | ingen linje |
# ```` 
# 
# ````{tabbed} Farger
# ![farger](https://matplotlib.org/2.0.2/_images/named_colors.png)
# ```` 

# ## Plotting av funksjoner
# En datamaskin kan bare håndtere _diskrete_ verdier, altså ikke-uendelige tallmengder. En matematisk funksjon kan derimot være kontinuerlig og ha uendelig mange funksjonsverdier. På en datamaskin må vi tilnærme denne uendelige mengden med et ganske stort antall. Dette kan vi gjøre med for eksempel _linspace_-kommandoen. Programmet nedenfor plotter funksjonen $f(x) = 2x^2 - 2x + 1$ for $x\in[-2, 3]$

# In[1]:


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 3, 1000) # lager 1000 x-verdier mellom -2 og 3
y = 2*x**2 - 2*x + 1 # lager 1000 tilsvarende y-verdier til en funksjon

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


# Det Python egentlig gjør når den plotter funksjoner, er å plotte et bestemt antall punkter og "tegne" rette linjer mellom disse punktene. Dette kalles "lineær interpolasjon". Det blir tydelig dersom vi kun velger ut fem punkter å plotte funksjonen i.

# In[4]:


x = np.linspace(-2, 3, 5) # lager 5 x-verdier mellom -2 og 3
y = 2*x**2 - 2*x + 1      # lager 5 tilsvarende y-verdier til en funksjon

plt.plot(x,y,marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


# Dersom vi definerer en Python-funksjon, kan vi også bruke denne til å generere _y_-verdier: 

# In[5]:


def f(x):
    return 2*x**2 - 2*x + 1 

x = np.linspace(-2, 3, 1000) # lager 5 x-verdier mellom -2 og 3
y = f(x)                     # lager 1000 tilsvarende y-verdier til en funksjon

plt.plot(x,y,)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()


# ```{admonition} Underveisoppgave
# :class: tip
# Plott tre funksjoner i samme koordinatsystem. Eksperimenter med farger, linjestiler og annet. Husk aksetitler!
# ```
# 
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# <iframe src="https://trinket.io/embed/python3/87f8b456bd" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# ```

# ## Flere plott i samme figur
# Dersom vi ønsker å lage flere plott i samme figur, kan vi bruke kommandoen _subplot(antall rader, antall kolonner, figurnummer)_ for å plotte flere grafer samtidig. Her er et eksempel:

# In[13]:


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 50)
y = np.sin(x)
 
plt.subplot(2, 1, 1)   # To rader, én kolonne, figur 1
plt.plot(x, y, color = "green", linestyle = "--")
plt.title("Grønn stiplekurve")

plt.subplot(2, 1, 2)            # To rader, én kolonne, figur 2
plt.plot(x, y, color = "red", linestyle = " ", marker = "o")
plt.title("Rød prikkekurve")
plt.tight_layout()              # Fikser slik at det ikke blir overlapp mellom f.eks. aksetitler

plt.show()
#plt.savefig("kulfigur.png")    # Lagrer figuren på datamaskinen din


# Vi kan også lage flere funksjoner i samme koordinatsystem. Da bruker vi _labels_ (merkelapper) for å skille mellom de ulike grafene, og _legend_ for å vise merkelappene i koordinatsystemet.

# In[2]:


import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 3, 10)

def f(x):
    return x**2 - 2*x

def g(x):
    return np.sin(x)

def h(x):
    return - x + 6

y1 = f(x)
y2 = g(x)
y3 = h(x)

plt.plot(x,y1,color='lawngreen',label='f(x)', marker='^') # Bruker merkelapp (label) for å skille mellom kurvene
plt.plot(x,y2,color='maroon',label='g(x)', marker='o')
plt.plot(x,y3,color='deepskyblue',label='h(x)', marker='s')
plt.legend() # Viser merkelappene
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(y=0,color='black') # Tegner x-akse
plt.axvline(x=0,color='black') # Tegner y-akse
plt.grid()
plt.show()


# ```{admonition} Underveisoppgave
# :class: tip
# Plott tre av dine favorittfunksjoner i samme koordinatsystem. Tilpass akser og tittel og pynt på plottet.
# ```

# ```{admonition} Underveisoppgave
# :class: tip
# Modifiser figuren ovenfor slik at plottene vises ved siden av hverandre i samme figur istedenfor under hverandre.
# ```
# 
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# Spesifiser subplottene som _subplot(1, 2, 1)_ og _subplot(1, 2, 2)_. Da blir det to kolonner istedenfor to rader. 
# ```

# ## Videoer
# I videoen nedenfor kan du få en innføring eller repetisjon i hvordan du plotter i Python.
# 
# <iframe width="800" height="600" src="https://www.youtube.com/embed/71SeDOstEwY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
