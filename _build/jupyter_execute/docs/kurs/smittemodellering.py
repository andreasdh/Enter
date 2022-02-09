#!/usr/bin/env python
# coding: utf-8

# # Smittemodellering
# 
# Hva tenker du når du hører ordet modell? En miniatyrdel av en liten by, kanskje? Eller kanskje du tenker på atommodeller? En modell er en forenklet representasjon av virkeligheten. Vi kan aldri representerere virkeligheten slik den er, så alle modeller vil ha visse forutsetninger og begrensninger. Her skal vi se på _matematiske modeller_, altså bruk av matematikk for å beskrive et eller annet fenom. Nærmere bestemt skal vi se på et veldig aktuelt tema i våre dager, nemlig modellering av smittespredning.
# 
# En modelleringsprosess innebærer flere trinn. For det første må vi ha en observasjon eller et fenomen vi ønsker å studere. Ut fra visse egenskaper ved dette systemet lager vi en modell som skal beskrive systemet under visse betingelser. Denne modellen kan vi teste, for eksempel gjennom eksperimenter eller simuleringer. Da får vi data som vi kan bruke til å evaluere modellens gyldighet. Deretter kan vi eventuelt justere modellen og gjøre nye simuleringer og målinger.
# 
# Modellering er altså en kontinuerlig prosess der modeller hele tiden evalueres og justeres opp mot virkeligheten. Programmering kan gjøre denne prosessen enklere fordi vi med noen tastetrykk kan endre modellen og observere utfallet av dette. For FHI har smittemodellering vært en svært viktig del av håndteringen av koronaviruspandemien, så la oss prøve oss som "smittemodellerere"!
# 
# 
# ### Modell 1
# Vi begynner med en enkel modell for smittespredning der antall smittede øker med en prosentvis andel hver dag. Vi kan da beskrive utviklingingen i antall smittede indivier *I* ("Inceptibles") slik:
# 
# $$I_{t+1} = I_t + aI_t$$
# 
# Her betyr indeksen _t + 1_ betyr at det er antall smittede ved neste tidspunkt (her neste dag), mens indeksen _t_ betyr antall smittede på nåværende tidspunkt. Det er jo ganske logisk at antall smittede neste dag er avhengig av antall smittede i dag. I tillegg øker antall smittede med en vekstfaktor _a_. Vi kaller _a_ for en _parameter_. Disse parameterne er ofte bestemt av observasjoner og data, så vi kan ikke vite hva som er en god verdi for _a_ til å begynne med. 
# 
# - Forklar med egne ord hva modellen forteller. Drøft også i hvilke sammenhenger det kan være hensiktsmessig å bruke en slik modell. Er det en realistisk modell i noen sammenhenger?
# 
# ```{admonition} Løsningsforslag
# :class: tip, dropdown
# 
# Modellen forteller at antall smittede individer ved neste tidssteg er lik antall smittede individer ved forrige tidssteg + en viss andel (a) av antall individer som sprer smitten videre.
# 
# Modellen forutsetter at det ikke er noen immunitet innenfor smittemengden, altså at ingen smittede møter på personer som allerede er smittet. Det kan være et realistisk bilde i en stor populasjon i begynnelsen av et smitteforløp. Det er derfor usannsynlig at modellen beskriver utviklingen langt fram i tid. Modellen forutsetter også at ingen blir friske i løpet av den tiden vi ser på. Igjen peker dette på at modellen kun representerer et kort tidsrom.
# ```
# 
# - Fyll inn det som mangler i programmet nedenfor for å simulere sykdomsutviklingen. Dersom du vil, kan du selvfølgelig viske ut alt og bygge programmet fra grunnen av. Varier med ulike verdier av _a_ og forklar betydningen av parameteren _a_ ut fra det du ser.
# 
# <iframe src="https://trinket.io/embed/python3/89e944ef8e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# from pylab import *
# 
# N = 157759     # Populasjonsstørrelse
# a = 0.2        # Kontaktrate per uke
# tid_slutt = 48 # Antall uker vi ønsker å simulere
# 
# # Startverdier
# I = 3          # Antall smittede til å begynne med
# 
# # Lister for å spare på verdiene
# smittede = [I]
# t = [0]
# 
# for tid in range(tid_slutt):
#     I = I + a*I
#     # Legger inn verdier i listene
#     smittede.append(I)
#     t.append(tid)
# 
# plot(t, smittede, label = "Smittede")
# xlabel("Antall uker fra siste uke i september 2004")
# ylabel("Antall individer")
# legend()        # Viser merkelapper
# show()
# ```
# ````

# ## Modell 2
# 
# La oss utvide modellen og innføre en ny kategori av individer som er mottakelige for smitte. Vi kaller dem _S_ (susceptibles).
# 
# Vi kan anta at de smittede da utvikler seg slik:
# 
# $$I_{n+1}=I_n+aI_nS_n$$
# 
# De mottakelige kan da beskrives slik:
# 
# $$S_{n+1}=S_n-aI_nS_n$$
# 
# - Bekriv modellene og prøv å forklare alle leddene og faktorene.
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# 
# Modellen sier at antall mottakelige er lik antall mottakelige ved forrige tidssteg minus andelen som er smittet. Årsaken til at vi også ganger inn de mottakelige her, er at smittespredningen nå avhenger av både mottakelige og de som allerede er smittet. 
# ````
# 
# - Fyll inn det som mangler i programmet nedenfor for å simulere sykdomsutviklingen. Dersom du vil, kan du selvfølgelig viske ut alt og bygge programmet fra grunnen av. Prøv å variere antall smittede til å begynne med. Beskriv utviklingen til hverandre og diskuter hva som skjer. Du kan også prøve med andre modeller, hvis du vil. Legg merke til at vi lagrer endringen i I og S i en egen variabel for å bruke I og S ved samme tidspunkt.
# 
# <iframe src="https://trinket.io/embed/python3/5e28200d13" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# ```{code-block} Python
# from pylab import *
# 
# N = 157759      # Populasjonsstørrelse
# a = 0.5/N       # Kontaktrate
# tid_slutt = 48  # Antall uker vi ønsker å simulere
# 
# # Startverdier
# I = 3           # Antall smittede til å begynne med
# S = N - I       # Antall usmittede til å begynne med
# 
# # Lister for å spare på verdiene
# mulige = [S]
# smittede = [I]
# t = [0]
# 
# for i in range(tid_slutt):
#     endring = a*S*I
#     I = I + endring
#     S = S - endring
#     # Legger inn verdier i listene
#     smittede.append(I)
#     mulige.append(S)
#     t.append(i)
#     
# plot(t, smittede, label = "Smittede")
# plot(t, mulige, label = "Mulige")
# xlabel("Antall uker fra siste uke i september 2004")
# ylabel("Antall individer")
# legend()         # Viser merkelapper
# show()
# ```
# ````

# ## Modell 3
# La oss nå utforske en modell som også tar hensyn til at det går an å bli frisk fra sykdommen. Da innfører vi en kategori til, nemlig de friske og tidligere smittede. Disse har da immunitet og kan ikke bli smittet igjen. Vi kaller dem R (recovered/removed), og de kan beskrives slik:
# 
# $$ R_{n+1}=R_n+bI_n$$
# 
# Da må de smittede utvikle seg slik:
# 
# $$I_{n+1}=I_n+aS_nI_n-bI_n$$
# 
# Antall usmittede, men mottakelige individer, S, må fortsatt følge denne modellen:
# 
# $$S_{n+1}=S_n-aI_nS_n$$
# 
# Dette kaller vi SIR-modellen for smitteutvikling.
# 
# 
# - Beskriv hva de ulike faktorene og leddene betyr. Hva tror dere den nye parameteren _b_ beskriver?
# 
# ````{admonition} Løsningsforslag
# :class: tip, dropdown
# 
# Parameteren _b_ beskriver bedringsraten, altså hvor stor andel av de smittede som blir friske, beskrevet av leddet $bI_n$.
# ````
# 
# - Nedenfor er det et program som simulerer smitte ved hjelp av SIR-modellen. Kjør programmet og forklar for hverandre hva det gjør, og hva resultatene er.
# 
# <iframe src="https://trinket.io/embed/python3/ecf278aa0b" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
# 
# 
# - Nå skal vi validere modellen vår. Vi utvider programmet og sammenlikner modellen med reelle data som viser antall smittede hver uke. Les filen «influensa.txt» og plott antall smittede (_I_) i det samme koordinatsystemet som den modellerte smittespredningen. Bruk gjerne programmet fra forrige aktivitet.
# 
# - Sammenlikne modellen og de reelle dataene, og tilpass gjerne koeffisientene _a_ og _b_ slik at modellen samsvarer bedre med dataene.
# 
# <iframe src="https://trinket.io/embed/python3/5984bdc7a1" width="100%" height="356" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>
