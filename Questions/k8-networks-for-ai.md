# Wiederholungsfragen K8 — Netze für KI (Networks for AI)

*Zu Kapitel 8 (`8-AdvCompNet-NetworksForAI.md`, L13/L14) · Literatur: 7E §13.4, §15; UEC 1.0; Meta SIGCOMM 2024*

*Neues Fragen-Set; RDMA übernommen aus „Wiederholungsfragen 8" (WiSe 25/26), die dort auskommentierten ML/AI-Fragen sind hier „reaktiviert" — das Kapitel existiert jetzt.*

## Workloads und Metrik

1. Warum reichen klassische DC-Netze für KI-Training nicht aus? *(Lernzielkontrolle)*
2. Unterscheiden Sie Trainings- und Inferenz-Workloads — welche Netz-Anforderungen folgen jeweils daraus?
3. Warum ist Tail-Latency (p99/p99.9) die entscheidende Metrik im KI-Netz — und warum sagt der Mittelwert nichts aus? Welche Kennzahl würden Sie in einem KI-Netz monitoren?
4. Was sind Straggler, und wie wirken sich z. B. ein warmer ASIC oder ein Hash-Konflikt auf den gesamten Trainings-Job aus?

## Topologie und Kollektive

5. Frontend- vs. Backend-Netz: Was trägt jedes der beiden, und warum ist die strikte Trennung der wichtigste Strukturunterschied zu klassischen Rechenzentren?
6. Wie funktioniert Rail-optimized Clos — und warum folgt die Verkabelungslogik der Kommunikationsstruktur statt der Topologie-Theorie?
7. Erklären Sie Ring-AllReduce und Tree-AllReduce. Wann nimmt man was, und welche Rolle spielt NCCL?
8. Was leistet In-Network-Aggregation (z. B. SHARP)?
9. Warum erzeugen Collectives Incast — und welche Gegenmittel kennen Sie?

## Transport und Congestion Control

10. Vergleichen Sie InfiniBand, RoCEv2 und Ultra Ethernet (UET) entlang der Kriterien Basis, Verlustverhalten, Mehrpfad-Fähigkeit, Ökosystem und Reifegrad.
11. Welche Nachteile hat PFC („lossless Ethernet") — und welche Alternativen gibt es (ECN, DCQCN, HPCC, Swift)? Warum ist „lossless" im Ethernet ein Problem, in InfiniBand aber Konstruktionsprinzip?
12. ECMP vs. Packet Spraying: Warum verschiebt sich die Lastverteilung im KI-Netz von „Flow" zu „Packet/Bit" — und was kostet Reordering?
13. Erläutern Sie das Konzept von Remote Direct Memory Access (RDMA). Welche Vor- und Nachteile sind mit RDMA verbunden? *(übernommen aus WiSe 25/26)*
14. Was leistet GPUDirect RDMA?

## Hardware und Ausblick

15. SmartNIC vs. DPU: Wo liegt der Unterschied, und was leisten DPUs für Training (AllReduce-Offload, GPUDirect) und Inferenz? Nennen Sie Beispiel-Generationen (z. B. BlueField-2/3/4).
16. „AI for Networking": Nennen Sie je ein Beispiel für eine belastbare Anwendung (Telemetrie + ML, Digital Twin, Intent-based) und für Hype (LLM-Agents für NetOps) — woran erkennen Sie den Unterschied?
