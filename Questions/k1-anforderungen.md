# Wiederholungsfragen K1 — Anforderungen & Performance

*Zu Kapitel 1 (`1-AdvCompNet-Anforderungen.md`, L1/L2) · Literatur: 7E Kap. 1 (1.1–1.5)*

## Anforderungen und Performance

1. Nennen und beschreiben Sie fünf Anforderungen an *Advanced Computer Networks*.
2. Welche Netz-Anforderungsbereiche werden grundsätzlich differenziert? Erläutern Sie zwei Netz-Anforderungen jeweils im Kontext dieser Bereiche.
3. Was versteht man unter *Quality of Service* und unter *Quality of Experience*?
4. Welchen Einfluss haben die Anforderungen Performance, Fehlertoleranz und Skalierbarkeit auf die Entwicklung von Computernetzen?
5. Welche Herausforderung stellt die Lichtgeschwindigkeit für die Weiterentwicklung von Computernetzen dar?
6. Was sind Bitrate, Latenz und Round Trip Time? Gibt es einen Zusammenhang zwischen erzielbarer Bitrate und Latenz — falls ja, welchen?
7. Welchen Einfluss hat die verfügbare Bitrate auf die Anbindung eines File-Servers? Unter welchen Bedingungen macht es wenig Sinn, diese zusätzlich zu steigern?
8. Welchen Einfluss hat die verfügbare Bitrate bei Audio-/Video-Streams? Welche Möglichkeit gibt es, mit veränderlich verfügbarer Bitrate in diesem Bereich umzugehen?
9. Was versteht man unter *Bursts* (*Peaks*) bei Netzübertragungen? Wie lässt sich der Einfluss dieser Bursts auf die Quality of Experience einer Netzanwendung reduzieren?
10. Was bestimmt die Übertragungsgeschwindigkeit des ersten Bits über eine Kommunikationsstrecke? Welchen Einfluss hat die Bitrate bei der Übertragung?
    - Wie verändert sich der Einfluss auf den gesamten Transfer, wenn statt 1 MB hingegen 10 GB übertragen werden? Welchen Einfluss wird auf die Übertragung von Dateien mit 100 KB ausgeübt?
    - Ist der angenommene Einfluss des Anwendungsprotokolls realistisch? Was bestimmt die Anzahl der RTTs, die zur Übertragung einer Datei erforderlich sind? Welchen Einfluss hat das Transportprotokoll hierbei zusätzlich?
11. TCP nutzt in aktuellen Betriebssystemen eine Skalierung der Window Size auf bis zu 1 GB. Bedeutet dies, dass über eine Verbindung mit hohem Delay und hoher Bitrate sofort 1 GB am Stück als Window übertragen wird? Begründen Sie Ihre Antwort.
12. Welche Window-Größen benutzt TCP? Beschreiben Sie die Verwendung und den Zusammenhang beider Window-Größen.
13. Die folgende Abbildung zeigt den Verlauf des Congestion Windows bei TCP über die Zeit einer exemplarischen TCP-Verbindung. Identifizieren und beschreiben Sie die einzelnen Phasen sowie damit verbundene Ereignisse, die Sie innerhalb dieser TCP-Sitzung vermuten.

    ![Congestion Window einer exemplarischen TCP-Verbindung](figures/tcp.png)

14. Beschreiben Sie die wesentlichen Einflussfaktoren auf die Netz-Performance.

## Skalierbarkeit und Design-Prinzipien

15. Erläutern Sie die grundlegende Architektur und Funktionsweise des Internets. Wie lässt sich die Größe und Skalierbarkeit des Internets bestimmen?
16. Was besagt das *End-to-End*-Internet-Design-Prinzip? Erläutern Sie die Auswirkungen anhand einer Skizze. *(übernommen aus „Grundlagen", WiSe 25/26)*
17. Wie hängen *great engineering* und *good science* in Bezug auf die Weiterentwicklung von Netzen zusammen?
