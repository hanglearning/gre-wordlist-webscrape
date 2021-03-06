#!/usr/bin/python
# coding:utf-8

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# make a word list (grabbed from the wordlist pdf, converted to Excel and extracted)

wordList = '''Day One
abandon
abate
abbreviate
aberration
abeyant
abnegation
abound
absolute
absolve
absorbing
abstemious
abstinence
abstracted from
abstraction
abstruse
absurd
abundance
abuse
accelerate
accept
accession
acclaim
accommodate
acerbic
achieve
acknowledge
acquiescence
acquire
adapt
adaptability
addiction
adhere
admirable
adopt
adroit
adulation
advanced
advantage
adversarial
adverse
advocate
aesthetic
affable
affinity
affirm
aimlessness
alacrity
alarmist
alien
alienation
allure
alternative
altruism
altruistic
ambivalence
anachronistic
analogous
analytical
anathema
ancestry
anchor
anecdote
animadversion
animate
anomalous
anomaly
anonymous
antagonistic
antediluvian
anthropogenic
anticipate
antithesis
apathy
apocryphal
apology
applaud
apposite
apprehend
approbation
appropriate
appropriation
apt
arcane
archaic
archetypical
arousal
arrest
arrogant
artifact
artificial
artlessness
ascetic
aspersion
assert
assertive
astonish
astringent
at a premium
atypical
augment
augmentation
auspicious
austerity
authoritarianism
authoritative
autonomy
available
avaricious
aversion
avert
awkward
awry
badger
baffle
balanced
balk at
banal
baneful
banter
bargain
baseless
bedrock
belabor
belie
bemoan
beneficence
benevolent
betoken
bias
blameless
bland
boast
bolster
boon
boundary
breakthrough
brook
bucolic
budding
buoy
burdensome
burgeoning
buttress
bypass
callous
callow
calm
calumny
camaraderie
canned
canny
capricious
captivate
capture
castigate
caterwaul
cede to
celebrate
celerity
censure
centralize
chagrin
challenging
champion
chaotic
characteristic
charity
chastise
check
cheerless
chic
chimera
choreograph
churlish
Day Two
circuitous
circumscribe
circumspect
circumstantial
circumvent
civic
civility
clandestine
cliquish
clumsy
cluster
coherent
collective
colossal
comity
commercial
commonplace
comparable
compartmentalize
compelling
competitive
complex
complicated
composed
comprehend
comprehensive
comprise
compromise
compunction
concede
conciliatory
concoct
condemn
condign
confessional
confine
conform to
confound
confused
conjectural
conjecture
consensus
considerable
consistent
conspicuous
constitute
constrain
consumption
contagious
contemplate
contented
contention
contentious
contingent
contract
contradict
contradictory
contravene
contribution
controversial
conundrum
convoluted
convulsion
cooperate
corrupt
counterforce
counterpart
covert
covet
crab
crass
credibility
credit
credulous
criminality
cryptic
cumbersome
curative
cure-all
cursory
curt
damp
darken
dated
daunting
dearth
debunk
decay
decisive
decline
decouple
decrepitude
decry
defend
defender
defensive
deferential
defining
definite
deflate
defy
degenerative
deify
delegate
deliberate
delight in
delightful
demand
demanding
demarcation
demise
demur
denounce
denunciation
deplete
deprecatory
depressing
derision
derivative
derive from
design
despair
detect
detectable
deter
deterioration
determine
detestation
detract
detracting
devious
dexterous
diatribe
dichotomous
didactic
differential
diffident
diffuse
dilatory
diligent
dim
diminish
diminutive
discard
discern
discordance
discretionary
discursion
disdain
disgorge
disinclination
disingenuous
disinterested
dismiss
disorganize
disparage
disparate
disparity
dispassionate
dispatch
dispel
displace
disproportionate
dispute
disregard
dissemblance
dissimilar
distend
distinctive
distribution
diverge
diversity
diverting
Day Three
divided
divorced
document
documentary
dogmatic
doom
douse
dovish
downplay
drag
dramatic
draw
dreary
droll
dubious
duplicate
duplicity
dwindle
easygoing
ebb
eclipse
economic
ecstasy
efficient
effusive
egalitarian
egregious
elegiac
elemental
elicit
eliminate
elite
elude
elusive
emblematic
embody
embrace
embryonic
emendation
emergent
eminent
emotional
empirical
employ
empower
emulate
enamor
encomium
encourage
encumber
encyclopedic
endemic
endorse
endowment
enduring
energize
engaging
engender
enhance
enigmatic
enrich
entail by
entangle
enterprising
entreat
entrench
enviable
envy
ephemeral
equable
equanimity
equivocal
erode
errant
erratic
erstwhile
erudite
eschew
esoteric
espouse
essential
established
estrange
eternal
eulogize
euphoria
evanescent
evasive
evenhandedness
evolve
exact
exacting
exactitude
exaggerate
exalt
exasperation
exceptional
excoriate
exculpate
exemplary
exhaustive
exigent
exiguous
exonerate
expansion
expel
experimental
explicit
exploit
external
extinguish
extirpate
extol
extraneous
extrapolate
extremist
exuberant
eye-catching
facile
facilitate
factious
fairness
fallacious
fanciful
faultless
favorable
fealty
feeble
feedback
feigned
fervor
fiery
figurative
filter
fitting
fixated
flagrant
flexibility
flourish
flout
fluctuate
flummery
flummox
flush with
forbear
forerunner
foresee
forestall
forgo
formidable
formulaic
forsake
foster
foundation
founder
fractious
fraudulence
frustrating
fund
fungible
fusty
futility
gaffe
galvanize
garrulous
gauge
generality
generate
generic
genial
genius
germane
glean
gloat
gloomy
glut
govern
Day Four
gratify
gregarious
groundless
guardian
guile
hail
half-formulated
halfhearted
hallmark
hallow
hamper
hamstring
haphazard
harmonize
harsh
hasty
heartless
hedge
helter-skelter
heterogeneity
heterogeneous
hew to
hierarchical
high-minded
hinder
hitch
hodgepodge
homogeneity
hone
honor
honorific
hortatory
hubris
humility
hyperbole
hypocrisy
iconoclast
idealistic
ignorance
illusory
imbibe
immaterial
immense
immortality
immutable
impair
impartial
impassioned
impassive
impecunious
impede
imperceptible
impermanent
impetuous
implacable
implausible
implement
import
impotence
impracticable
impressive
improvise
impugn
impulsive
inaccessible
inadequate
inborn
inception
inclusive
incommensurable
incommensurate
inconsequential
inconsistent
inconstant
incorporate
incursion
indict
indifferent
indigent
indiscernible
indiscriminate
indispensable
indubitable
industrious
inert
inevitable
infectious
inferable from
infinite
inflammatory
inflate
informative
ingenuous
inherent
inimical
innate
innocuous
innovative
insatiable
inscrutable
insightful
insipid
inspire
insufferable
insufficient
insular
insulate
intelligible
intensity
interchangeable
interdependent
interpret
interrelated
intractable
intransigent
intricate
intrinsic
intuitive
invalidate
inverse
irascibility
irascible
irenic
ironic
irrelevant
irreparable
irresistible
irresolution
isolationism
itinerant
jarring
jejune
jettison
judicious
keen
kinfolk
knotty
laboratory
laborious
laconic
lambaste
languish
lapse
largesse
laudable
laudatory
lawlike
layperson
legitimacy
lethargic
liberalize
liberation
limited
limiting
limpid
linked
lionize
list
loath
loquacious
lowly
lucidity
lucrative
ludicrous
lugubrious
lull
luxuriant
madcap
maintain
malady
malfeasance
malleable
malodorous
manifest
Day Five
manipulate
marginal
marked
mask
master
match
materialize
maturity
maudlin
maverick
meager
measured
meet
meld
mendacity
mercurial
metaphor
meticulous
mimic
minimal
minimize
minuscule
misconception
misconstrue
misguide
mishandle
misrepresent
misuse
mitigate
mixed
mockery
modest
modicum
modulate
mollify
momentary
monitor
monolithic
monstrous
mordant
muddle
mundane
mutable
naiveté
nascent
naysayer
nebulous
negotiable
neutrality
nimble
noisome
nonconformist
nondescript
nonspecialist
novel
novice
numinous
obdurate
obedience
obeisance
obfuscate
objectionable
objective
obligatory
obliterate
obscure
obsequious
obsessed
obtain
obtrusive
obviate
occlude
occult
old-fashioned
ominous
onerous
onetime
onset
opaque
opinionated
opportune
oppressive
opprobrium
optimism
opulent
orderly
orientation
origin
original
originate
oust
outdo
outmoded
outstanding
outstrip
overblown
overclaim
overlook
oversell
overthrow
pacific
painstaking
palliate
palliative
paltry
panacea
paradigm
paradoxical
parity
parochial
parsimonious
passive
pastiche
pastoral
patchwork
paucity
pecuniary
pedestrian
peer
pellucid
penalty
perceptible
peregrinate
perennial
perfunctory
perilous
peripatetic
peripheral
periphery
permeable
perpetuate
perplex
perplexing
persist
persistence
perspicacious
pertain
pervasive
pessimistic
philosophy
pilfer
pioneering
plague
plaintive
plastic
platitudinous
please
plentiful
plethora
plodding
pointless
polemic
polymath
ponder
porous
portend
potential
pragmatic
preachy
precarious
precipitate
preclude
precocious
preconception
precursor
predate
predictable
predilection
predominant
prefigure
prejudice
preoccupy
presage
prescient
prescriptive
preside
Day Six
prestige
preternatural
pretext
prevail
prevalent
primitive
pristine
privilege
probity
proclaim
proclivity
prodigious
profess
proficient
profitmonger
profound
profusion
proliferate
prolix
prominence
prominent
promise
prompt
prophetic
propitious
proponent
proprietary
protean
protract
provenance
provincial
provocative
proximity
prudent
pseudonym
pugnacious
puncture
purport
purposefulness
purview
put to rest
quaff
qualify
quash
query
quiescence
quiescent
quirky
quixotic
quotidian
radical
raillery
rally
rampant
rant
rapacious
rapprochement
rationale
rattle
reactivate
readable
realize
rebuff
recant
recast
reckon
recoil
reconciliation
recondite
rehabilitate
rehash
rejection
reliability
relic
relief
relinquish
relish
reluctant
remarkable
remedy
remiss
repudiate
requisite
resemblance
reserved
resolve
resonate
respite
responsive
restive
restorative
restrain
retain
reticent
retreat
revision
revolutionary
riddle
ridicule
ring true
risible
ritualize
robust
routine
rudimentary
rule out
sacrifice
sacrosanct
salient
salutary
sanctimonious
sanction
sanguine
sanity
scant
scarce
scaremonger
schism
scrutinize
secondhand
secure
self-aggrandizing
self-effacing
self-evident
self-perpetuating
seminal
senescence
sequential
sever
shackle
short-lived
shortcoming
shrewd
shriek
shrink
shy away
sidestep
sift
signal
signify
simplicity
singular
skeptical
sketchy
skullduggery
slapdash
sleazy
slight
slippery
sluggish
slumberous
slur
smother
snag
snub
sobering
sociability
solemn
solidarity
somber
somnolent
soothe
sophist
sordid
sound
sovereignty
spartan
specious
spectacular
speculation
spontaneity
spontaneous
spur
spurious
Day Seven
square with
stability
stagnate
stale
stalwart
standstill
staunch
stave off
stem
sterling
stifle
stingy
stratified
striking
strip away
stubborn
stun
stymie
subordinate
successive
succumb
suffocate
sullen
superficial
superfluous
supplant
supple
surfeit
surly
surmise
surrender
surreptitious
survival
sustain
sway
sycophantic
sympathetic
synonymous
synthesis
systematic
taciturn
taint
tantamount
taxing
tedious
teem with
temper
temperate
temporary
tenacity
tenuous
tepid
terrifying
terse
testimony
thorough
thrive
tilt
timely
timid
tolerate
tonic
tortuous
totemic
tractable
transgress
transient
transitory
treasure
trenchant
trepidation
tribute
trifling
trigger
triumph
trivial
truculent
turbid
tyro
ubiquitous
umbrage
unalloyed
unambiguous
unassailable
unassuming
unattainable
unavoidable
unbalanced
unblemished
unbounded
unceasing
unchecked
uncompromising
unconventional
undeniable
undermine
undesirable
undisputed
unencumbered
unerring
unethical
uneven
unexampled
unexceptional
unexploited
unfathomable
unfeeling
unflagging
unfounded
ungainly
unimpeachable
unimpressed
uninformative
universal
unjustified
unkempt
unlinked
unmistakable
unorthodox
unostentatious
unprecedented
unprepossessing
unproven
unqualified
unremitting
unsettle
unsophisticated
unsurpassed
untenable
untether
unwarranted
unwieldy
unyielding
upend
upheaval
urbane
urgent
utilitarian
utopia
vacant
vacillation
vacuous
vague
valediction
valid
valorize
vanish
vaporize
variance
vehement
venal
venerable
venerate
veracity
verbose
verisimilitude
versatile
vestige
vigorous
violate
virtue
visible
vitiate
vitriol
vivacious
volatile
voracious
wane
wanting
wayward
wealth
welter
wherewithal
whimsical
wide-ranging
wield
winning
wistful
witless
wondrous
yield
youthful
zealot
zealous'''

wordList = [y for y in (x.strip() for x in wordList.splitlines()) if y]
print(wordList)

wordList = [y for y in (x.strip() for x in wordList.splitlines()) if y]

dayIndex = 0
dayArray = ['Day One', 'Day Two', 'Day Three', 'Day Four', 'Day Five', 'Day Six', 'Day Seven']

for item in wordList:
        if item == dayArray[dayIndex]:
                if dayIndex == 0:
                        print(dayArray[dayIndex].upper() + '\n')
                        dayIndex += 1
                elif dayIndex == 7:
                        break
                else:
                        print(dayArray[dayIndex].upper() + '\n')
                        dayIndex += 1
        else:
                # construct url for each word
                myUrl = 'http://gre.kmf.com/vocab/detail/' + item

                # opening up the connection, grabbing the page
                uClient = uReq(myUrl)
                page_html = uClient.read()
                uClient.close()

                # html parsing
                pageSoup = soup(page_html, "html.parser", from_encoding='utf-8')

                # grab word container
                container = pageSoup.findAll("div", {"class", "word-d-maintile"})
                contain = container[0]# actually only 1 item in the container array

                # grab the word(should be the same as item)
                word = contain.span.text

                # grab word detail
                wordDetail_container = contain.findAll("div", {"class": "word-g-translate"})
                wordDetail = wordDetail_container[0].text.strip()# again should be only 1 item in the array.strip() the extra spaces and useless indentation

                # manipulate the string wordDetail(string is immutable but you know what I mean)
                detailArray = []
                for letter in wordDetail:
                        if letter != '【' and letter != '例' and letter != '近' and letter != '反':
                            detailArray.append(letter)
                        elif letter == '【':
                            detailArray.append("\n\n\n" + letter)
                        else:
                            detailArray.append("\n\n" + '[' + letter + ']' + ' ')
                        newWordDetail = ''.join(detailArray)
                #print("CUT\n") debug
                print(word + '  &  \n')
                print(newWordDetail + '  $  \n')
                #f.write(word +',' + '&' + ',' + newWordDetail.replace(',', 'douhao').encode('gb2312') + ',' + '$')
