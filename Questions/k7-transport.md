# Wiederholungsfragen K7 — Transport & Anwendungen

*Zu Kapitel 7 (`7-AdvCompNet-NetworkApplicationPerformance.md`, L11/L12) · Literatur: 7E §12–15; RFC 9000, 9621–9623*

*Übernommen aus „Wiederholungsfragen 8: Network Application Performance" (WiSe 25/26); Multipath-QUIC/TAPS-Fragen neu (L12), RDMA nach K8 verschoben.*

## Lastverteilung

1. Welche prinzipiellen Lösungen für die Lastverteilung im Data Center kennen Sie?
2. Erläutern Sie die Funktionsweise und Grenzen/Limitierungen von DNS Round Robin.
3. Beschreiben Sie die allgemeine Architektur und Funktionsweise beim Einsatz eines Reverse Proxies zur Lastverteilung über ein Server-Cluster.
4. Was versteht man beim Load Balancing unter statischem Hashing? Welche Herausforderungen ergeben sich hierbei und wie können diese adressiert werden?
5. Wie lassen sich mit Hilfe von IP Anycast sowohl Lastverteilung als auch Ausfallsicherheit realisieren? Welche Probleme entstehen hierbei?
6. Beschreiben Sie die Funktionsweise von Layer-7-/Application-Layer-Load-Balancern anhand eines konkreten Beispiels. Welche Vorteile bieten diese, welche Herausforderungen entstehen bei deren Einsatz?

## Fluss- und Staukontrolle

7. Erläutern Sie den Bedarf für die Weiterentwicklung der Fluss- und Staukontrolle bei TCP. Nennen und beschreiben Sie Beispiele für Erweiterungen/aktuelle Entwicklungen mit direktem oder indirektem Einfluss auf diese Mechanismen.
8. Welchen Einfluss haben UDP-Kommunikationen auf die TCP Congestion Control bzw. auf damit verbundene TCP-Verbindungen? Begründen Sie Ihre Antwort.
9. Wie bewerten Sie die Verwendung von UDP statt TCP zur Verbesserung der Fluss- und Staukontrolle? Welche Chancen und welche Herausforderungen entstehen hierbei?
10. Erläutern Sie das Konzept von TCP Offloading. Welche Vor- und Nachteile sind damit verbunden?
11. Was ist BBR? Welche Ideen liegen BBR zugrunde und welche Ziele werden verfolgt?

## HTTP/3, QUIC und Multipath

12. Welche Entwicklungen liegen HTTP/3 zugrunde? Welche neuen Herausforderungen entstehen dabei?
13. Was ist Quick UDP Internet Connections (QUIC)? Beschreiben Sie drei exemplarische Ziele, die bei/mit QUIC verfolgt werden.
14. Wie erweitert Multipath QUIC Standard-QUIC — und welche Scheduling-Entscheidungen entstehen dadurch (z. B. `minRTT` vs. Round-Robin)? *(neu, L12; Multipath-Extension kurz vor RFC-Status)*
15. Was bedeutet Reordering bzw. Head-of-Line Blocking bei Multipath-Übertragung — und warum ist das für TCP-basierte Ansätze gravierender als für QUIC? *(neu, L12)*
16. Was leistet die Transport-Services-API (TAPS, RFC 9621–9623)? Welches Problem der Transportauswahl für Anwendungen löst sie? *(neu, L12)*
17. Nennen Sie jeweils ein Beispiel für eine Technologie zur Realisierung von Fehlertoleranz und zur Steigerung der Performance auf: Layer 2, Layer 3, Layer 4, Layer 7.
