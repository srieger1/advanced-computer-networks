# Wiederholungsfragen K3 — Netzvirtualisierung & Overlays

*Zu Kapitel 3 (`3-AdvCompNet-Netzvirtualisierung.md`, L5) · Literatur: 7E Kap. 9 (9.1–9.5)*

*Fragen 1–3 und 13 übernommen bzw. abgeleitet aus „Wiederholungsfragen 3: Software-defined Networking" (WiSe 25/26), Fragen 10–12 neu; Übungspunkte beziehen sich auf Lab L1, Szenario 3.*

## Motivation

1. Warum brauchen Clouds virtuelle Netze? Nennen Sie drei Treiber (Mandantentrennung, Skalierung, Beweglichkeit) und erläutern Sie jeweils einen.
2. Was unterscheidet *Netz-Virtualisierung* von *Network Slicing*? Nennen Sie zu beiden je ein Beispiel.
3. Wie unterstützt Netz-Virtualisierung die Migration von virtuellen Maschinen hinsichtlich der Netz-Konfiguration im Data Center? *(übernommen aus WiSe 25/26, ehemals SDN-Kapitel)*

## VLANs

4. Was ist ein VLAN und welche VLAN-Arten (Einordnungskriterien) kennen Sie? Diskutieren Sie allgemeine sowie individuelle Vorteile und Herausforderungen.
5. Was steht im 802.1Q-Tag — und warum sind 12 Bit VID schnell zu wenig? Skizzieren Sie die Tag-Struktur (EtherType, PCP/DEI, VID).
6. Was versteht man unter VLAN Trunking und wie funktioniert es? Unterscheiden Sie Access- und Trunk-Port (incl. Konfigurationsbeispiel).
7. An welchen Grenzen stoßen VLANs in Cloud-Umgebungen? Nennen Sie mindestens drei und ordnen Sie ein, ab wann ein Overlay wie VXLAN nötig wird.

## Overlays — VXLAN und EVPN

8. Wie funktioniert VXLAN? Beschreiben Sie den Kapselungsstapel (äußeres Ethernet → IP → UDP → VXLAN → inneres Ethernet) und den UDP-Port.
9. Was leisten VNI (24 Bit → 16 Mio. Segmente) und VTEP? Warum haben Overlay und Underlay getrennte Adressräume?
10. Wie unterscheiden sich Flood & Filter (Data Plane) und EVPN (Control Plane)? Was spricht für EVPN in Data-Center-Fabrics?
11. Vergleichen Sie VXLAN und VLAN entlang der Kriterien Kennung, Unterlage, Endpunkte und Mobilität.
12. Praktikumsbezug: Wie würden Sie in einer Mitschnitt-Analyse (Lab L1, Szenario 3) nachweisen, dass ein Frame zum VLAN 10 gehört — und wie, dass ein Paket durch einen VXLAN-Tunnel geht (UDP 4789, VNI)?

## VPN und Segmentierung

13. Erläutern Sie das Tunneling-Konzept: Wie entsteht aus dem fremden Internet eine private Punkt-zu-Punkt-Strecke? Welche Rolle spielen Verschlüsselung (WireGuard, OpenVPN, IPsec)?
14. Vergleichen Sie die VPN-Topologien Site-to-Site, Remote Access und Mesh/Zero Trust — wohin entwickelt sich der Trend und warum?
15. Was ändert Microsegmentation an klassischer Firewall-Zonierung? Erläutern Sie am Beispiel einer 3-Tier-Anwendung (Web-, App-, DB-Tier).
