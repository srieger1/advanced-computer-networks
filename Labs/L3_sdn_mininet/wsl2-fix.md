 Hoffnungsvoller Punkt zuerst: Der Ausweg ist sauber im Image/Topology verfügbar — Userspace-Datapath:

 ```
ovs-vsctl set bridge ofp-sw1 datapath_type=netdev
 ```

 braucht kein Kernel-Modul und reicht für dieses Lab locker: Die Links sind ohnehin per TCIntf bw=1 auf 1 Mbit/s gedeckelt — der langsamere Userspace-Datapath ist bei den auftretenden Paketraten (pingall, iperf in diesem Rahmen) messbar irrelevant. Falls der Kernel-Modul-Check
 morgen schiefgeht, wäre das meine erste Wahl statt „kaschieren".

 Morgen-Check in 30 Sekunden nach dem Deploy:

 ```
docker exec clab-acn-l3-mininet-mininet modprobe openvswitch   # "not found" ⇒ Kernel ohne Modul
docker exec clab-acn-l3-mininet-mininet ovs-vsctl show         # Bridge da? Fehler im ovs-start-Log?
 ```

 Einordnung WSL2: Netzwerk-Namespaces, veth, tc-qdiscs (TCIntf) funktionieren im WSL2-Kernel — Mininet selbst ist da unkritisch. Nur das OVS-Datapath-Modul ist die bekannte Lücke; Microsoft hat den Kernel zwar inzwischen öfter aufgebohrt, aber ob CONFIG_OPENVSWITCH drin ist,
 verrät genau dieser modprobe-Test. Eigener Kernel-Bau (.wslconfig mit Kernel aus dem WSL2-Linux-Kernel-Repo) ginge technisch, ist für Studierende aber Sackgasse.

 Die „kaschieren"-Variante ist realistisch: Studierende mit Linux (native oder volle VM) haben kein Problem, WSL2-Gruppe kriegt den netdev-Fallback — und die anderen Plattformen (learn-sdn-hub-VM der Vergangenheit) fällt bei 2-Hosts-Topo kaum noch ins Gewicht.

 Wenn der modprobe-Test morgen scheitert: Ich kann den netdev-Fallback als Kommentar-Stolperfalle in sdn.clab.yml hinterlegen (nicht ins Labsheet, bleib schlank) — sag einfach Bescheid.
