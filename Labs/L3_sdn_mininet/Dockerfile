# ACN Lab L3 — SDN/OpenFlow mit Mininet: BYOD-Container (ersetzt die learn-sdn-hub-VM)
#
# Ubuntu 24.04 + Mininet + Open vSwitch + os-ken (aktive Ryu-Gabelung von OpenStack;
# Ryu selbst ist seit 04/2024 ohne Commits). Läuft als containerlab-Knoten (privileged):
#
#   docker build -t acn-l3-mininet:2026.10 .
#   Smoke:  docker run --rm --privileged acn-l3-mininet:2026.10 sh -c \
#           "/usr/share/openvswitch/scripts/ovs-ctl start && mn --test pingall"
#           (OVS-Daemon startet im rohen docker run NICHT selbst — ohne ovs-ctl start
#            bricht mn mit "Error connecting to ovs-db" ab; im containerlab-Knoten
#            startet das exec in sdn.clab.yml den Daemon.)
FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y --no-install-recommends \
      mininet openvswitch-switch iproute2 iputils-ping net-tools tcpdump \
      iperf3 python3-pip less vim nano psmisc && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --break-system-packages os-ken==4.2.2 tinyrpc && \
    # Stolperfalle 3: Mininet wartet im iperf-Test auf 2 Server-Reports (Probe + Test),
    # iperf 2.1.9 liefert aber nur einen (Probe-Verbindung erzeugt keinen Report) —
    # der monitor()-Loop haengt endlos. Patch: count 2 -> 1.
    sed -i "s/count = 2 if l4Type == 'TCP' else 1/count = 1/" \
      /usr/lib/python3/dist-packages/mininet/net.py && \
    mn --version && ovs-vsctl --version | head -1 && \
    echo 'service() { /usr/share/openvswitch/scripts/ovs-ctl start; }' >/etc/profile.d/ovs.sh

CMD ["sleep", "infinity"]

# Stolperfalle 1: os-ken unversioniert zieht inzwischen 5.x — OpenStack hat dort
# eventlet entfernt (hub.patch fehlt, Manager-Port bricht beim Import). Deshalb Pin auf
# 4.2.2 (eventlet-basiert, Stand letztes Jahr).
# Stolperfalle 2: os-ken-Wheels (4.2.2) enthalten KEIN os_ken/cmd (Manager) und kein
# app/wsgi — beide kommen hier portiert aus ryu 4.34 (Module umbenannt ryu -> os_ken).
# osken-manager ersetzt den klassischen ryu-manager; default_port 6633 wie im alten Lab.
COPY osken_patch/os_ken/cmd/ /usr/local/lib/python3.12/dist-packages/os_ken/cmd/
COPY osken_patch/osken-manager /usr/local/bin/osken-manager
RUN chmod +x /usr/local/bin/osken-manager && osken-manager --version
