# Wiederholungsfragen K2 — Data Center Networking

*Zu Kapitel 2 (`2-AdvCompNet-DataCenterNetworking.md`, L3/L4) · Literatur: 7E §4.5, §9.4; SDN-Buch Ch. 3, 7*

## Rechenzentrum: Aufbau & Evolution

1. Beschreiben Sie den grundlegenden Aufbau eines Rechenzentrums sowie die darin verwendeten Komponenten und Ressourcen-Klassen (Compute, Storage, Network).
2. Was versteht man unter ToR- und EoR-Switches in Data-Center-Netzen? Worin liegen die Unterschiede, welche Vor- und Nachteile haben beide Ansätze?
3. Wie trägt die Virtualisierung zur Evolution aktueller Rechenzentren bei?
4. Welche aktuellen Anforderungen und Trends für Rechenzentren existieren (Strom, Standorte, KI-Treiber)? Nennen Sie Beispiele mit Zahlen und Quelle.
5. Welche Traffic-Pattern existieren in Data-Center-Netzen? Beschreiben und begründen Sie den Wandel hinsichtlich der Traffic-Volumina der einzelnen Pattern (north/south vs. east/west).

## Tree, Leaf-Spine und Fehlertoleranz

6. Erläutern und skizzieren Sie die klassische, hierarchisch organisierte Tree-Architektur (3-Tier) mit den verbundenen Vorteilen und Herausforderungen. Warum wird sie bei East-West-Traffic zum Engpass?
7. Welche Vor- und Nachteile bietet der Einsatz des Spanning Tree Protocols (STP) in Layer-2-Topologien? Welche Lösungen für die STP-Herausforderungen kennen Sie?
8. Was versteht man unter einem *Single Point of Failure* (SPoF) und wie lässt sich dieser im Netzbereich verhindern?
9. Was versteht man unter Oversubscription in Data-Center-Netzen? Welche Vor- und Nachteile sind damit verbunden — und warum ist sie eine Auslegungsentscheidung und kein Fehler?
10. Was versteht man unter Bisektionsbandbreite? Berechnen Sie sie für einen Fat Tree aus k-Port-Switches (k = 4) und für einen 3-Tier-Tree mit 4:1-Uplinks.
11. Was versteht man im Netzwerkbereich unter *Multi Pathing* und unter *Equal Cost Multi Pathing* (ECMP)? Wie wird ECMP für Flows umgesetzt — und warum führt der Hash zu „sticky" Pfaden pro Host-Paar?
12. Warum nutzt man im Fabric ECMP statt Spanning Tree?
13. Erläutern und skizzieren Sie die Leaf-Spine-Architektur (Clos). Wie skaliert sie, und warum laufen Fabrics mit BGP (RFC 7938)?

## Fabrics der Hyperscaler

14. Wie entwickeln sich der Machine-to-Machine- und der Machine-to-User-Traffic im Meta-Rechenzentrum exemplarisch? Begründen Sie diesen Wandel und beschreiben Sie die daraus entstehenden Anforderungen.
15. Erläutern und skizzieren Sie die grundlegende Architektur der Meta Data Center Fabric (Altoona, 2014). Wie hat sie sich bis F16 (2019) und zu den KI-Clustern (2024) entwickelt?
16. Welche Vor- und Nachteile hat der Einsatz „eigener" Data-Center-Switches bzw. „eigener" Network Operating Systems? Welche Rolle spielt SONiC laut Marktdaten (Gartner 3/2025)?
17. Beschreiben Sie den grundlegenden Aufbau des Fabric Aggregators von Meta. Welche Aufgaben übernimmt dieser hinsichtlich der Data-Center-Fabrics?
18. Was sind DCell und Jellyfish — und warum bleibt trotz dieser Alternativen Clos/Fat-Tree das Standarddesign?

## PortLand und VL2

19. Beschreiben Sie die Struktur und Bedeutung der Positional Pseudo MAC Address (PMAC) bei PortLand. Welche weiteren Adressinformationen existieren in diesem Kontext und wie unterscheiden sich diese von der PMAC?
20. Welche zentrale Aufgabe übernimmt der Fabric Manager in PortLand?
21. Erläutern und skizzieren Sie den grundlegenden Aufbau der VL2-Architektur. Welche Adressinformationen (AA/LA) existieren und wofür werden diese genutzt?
22. Beschreiben Sie die prinzipielle Adressauflösung (ARP) in VL2 und die zentrale Aufgabe des Directory Service.
