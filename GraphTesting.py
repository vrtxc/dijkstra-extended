import DjisktraAlghorythmus
import datetime


localTimeStart = datetime.datetime.now()
timeStart = localTimeStart.strftime("%M.%S.%f")[:-3]
splitTimeStart = timeStart.split(".")

# Erzeugung des Graph-Objekts
g = DjisktraAlghorythmus.GraphDijkstra()
# Erzeugung der Knoten und Kanten aus einer GraphML-Datei
print('Autobahndaten werden geladen ...')
datei = open('karteDeutschland.xml', 'r')
xml_quelltext = datei.read()
g.graphmlToGraph(xml_quelltext)
# Ausführung des Dijkstra-Algorithmus
start = 'TRIER - VERTEILERKREIS (A 602)'
ziel = 'KREUZ MÜNCHEN - WEST'
print('kürzester Weg von', start, 'nach', ziel, ':')
(weg, laenge) = g.kuerzesterWegDijkstra(start, ziel)
for w in weg:
    print(w)
print('Weglänge:', laenge)


localTimeEnd = datetime.datetime.now()
timeEnd = localTimeEnd.strftime("%M.%S.%f")[:-3]
splitTimeEnd = timeEnd.split(".")

resultSec = int(splitTimeEnd[1]) - int(splitTimeStart[1])
if int(splitTimeStart[2]) <= int(splitTimeEnd[2]):
    resultMiliSec = int(splitTimeEnd[2]) - int(splitTimeStart[2])
else:
    resultMiliSec = (int(splitTimeEnd[1]) + 1000) - int(splitTimeStart[2])
    resultSec = resultSec - 1


print("Time passed while executing the Code:")
print(resultSec, "seconds")
print(resultMiliSec, "mili-seconds")
