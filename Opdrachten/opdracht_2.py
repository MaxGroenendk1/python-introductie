from math import *

people = 67893584
print(people)

people = 67_893_584 #python ignores the underscores
print(people)

meals = 3
days = 365
people_eat = people * meals
print(people_eat)

meals_per_year = people_eat * days
print(meals_per_year)

ethernet_speed_mbps = 1000
efficiency = 0.7
maximum_capacity = ethernet_speed_mbps * efficiency
print(maximum_capacity)

ethernet_speed_mbps = 1000
download_speed_average = 96.25
usage = ethernet_speed_mbps / download_speed_average
print(usage)

# Speed of light in m/s
speed_of_light = 299_792_458

# Distance Rotterdam / New York in km
distance_Rotterdam_NewYork = 5_862.03
# Distance Rotterdam to New York in meters divided by the speed of light
time_to_reach_NYC = (distance_Rotterdam_NewYork * 1000) / speed_of_light
print(f'Time spend for light to reach New York from Rotterdam is: {time_to_reach_NYC} seconds => {time_to_reach_NYC * 1000.0} milliseconds.')

# What is the data type?
type(time_to_reach_NYC)

ship = 'Titanic'
print(ship)
ship = "Titanic"
print(ship)
ship = """Titanic"""
print(ship)

zonder_escape = 'This is a "good" plan' #<- klein verschil van 1 ' op de buitste regel
print(zonder_escape)
met_escape = "This is a \"good\" plan"
print(met_escape)

Laadsnelheid = 331 / 441 #aantal containers per minuut
lossnelheid = 287 / 295 #aantal containers per minuut
gelost = False #leeg
geladen = True #vol

print(f'de gemiddelde lostijd bedraagt {lossnelheid} minuten per container')
print(f'de gemiddelde laadtijd bedraagt {Laadsnelheid} minuten per container')


x = 9.1

antwoord_berekening = sqrt(3 * x - 1) + (1 + x)**2
print(f'De waarde van y = {antwoord_berekening} als x = {x}.')


c = 299792458 #m/s light speed in miliseconds
t = 4 # in uren
v = 179875474.8 #m/s speed of comet in miliseconds
formule_delta = t * 1 / (v*(1 - (v ** 2 / c ** 2)) )
print(formule_delta) # in uren
print(formule_delta * 60)   # in minuten
print(formule_delta * 60 * 60) # in seconden

uur = formule_delta
minuten = formule_delta * 60
seconden = formule_delta * 60 * 60
miliseconden = formule_delta * 60 * 60 * 1000
print(f'Vanaf een komeet gezien zit u {uur} uur op de tuinstoel voordat de lichtstraal de aarde bereikt.')
print(f'Vanaf een komeet gezien zit u {minuten} minuten op de tuinstoel voordat de lichtstraal de aarde bereikt.')
print(f'Vanaf een komeet gezien zit u {seconden} seconden op de tuinstoel voordat de lichtstraal de aarde bereikt.')
print(f'Vanaf een komeet gezien zit u {miliseconden} miliseconden op de tuinstoel voordat de lichtstraal de aarde bereikt.')

