# Wiederholungsfragen K5 — NFV & Cloud-native Networking

*Zu Kapitel 5 (`5-AdvCompNet-NFV.md`, L8) · Literatur: ETSI GS NFV; 7E §10; CNCF/eBPF*

*Übernommen aus „Wiederholungsfragen 5: Network Function Virtualization" (WiSe 25/26); Cloud-native-Fragen neu (L8).*

1. Wie können Multi-Tenant-Netze in virtualisierten Umgebungen (z. B. Cloud) realisiert werden? Was ist die Motivation, welche Herausforderungen ergeben sich? *(Welche Rolle spielen dabei VLAN/VXLAN aus Kapitel 3?)*
2. Wie werden virtuelle Switches (vSwitches) realisiert? Welche Funktionen werden von vSwitches erbracht bzw. unterstützt?
3. Beschreiben Sie den Einsatz mehrerer Netzwerkkarten bei der Server-Virtualisierung in einem Hypervisor zur Adressierung der Ausfallsicherheit und Lastverteilung.
4. Welche Formen zur Bereitstellung einer Network Interface Card (NIC) für VMs über den Hypervisor kennen Sie? Diskutieren Sie deren Vor- und Nachteile (emuliert, para-virtualisiert, SR-IOV, DPDK).
5. Welche grundlegenden Konzepte/Elemente werden in einer High-Level-NFV-Architektur (vgl. MANO) differenziert? Skizzieren Sie die Elemente und deren Abhängigkeiten.
6. Was umfasst die NFVI, was ist eine VNF — und wie hat sich der Begriff VNF zu cloud-nativen Netzwerkfunktionen (Container, CNI) verschoben? *(neu, L8)*
7. Was sind CNI und eBPF im Kontext containerisierter Workloads — und was leisten sie im Vergleich zu klassischer Netz-Virtualisierung? *(neu, L8; Beispiel Cilium)*
8. Was ist ein Service Mesh, und welches Netz-Problem löst es? Worin unterscheidet es sich von klassischen Netz-Middleboxes? *(neu, L8)*
9. Ist eine VNF heute schlicht ein Container? Begründen Sie Ihre Antwort. *(aus der Vorlesungsdiskussion)*
10. Welche vermeintlichen Veränderungen erwarten Sie im Netzbereich durch Network Softwarization — SDN, NFV und deren Integration? Wie bewerten Sie diese Veränderungen?
