from mininet.topo import Topo
from mininet.node import Node
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import RemoteController

import os
import subprocess


def _ovs_datapath():
  """kernel, wenn das openvswitch-Kernelmodul ladbar ist (Linux-Host),
     sonst 'user' (= datapath_type=netdev, Userspace — z. B. WSL2 ohne
     openvswitch-Kernelmodul). Ueber OVS_DATAPATH=kernel|user erzwingebar."""
  forced = os.environ.get('OVS_DATAPATH')
  if forced in ('kernel', 'user'):
    return forced
  if os.path.isdir('/sys/module/openvswitch'):
    return 'kernel'  # Modul ist bereits geladen (Host-Kernel)
  try:
    ok = subprocess.run(['modprobe', 'openvswitch'],
                        capture_output=True).returncode == 0
  except FileNotFoundError:
    ok = False
  return 'kernel' if ok else 'user'


class CustomTopo(Topo):

  def __init__(self):
      Topo.__init__(self)

  def build(self):

    sw = self.addSwitch('ofp-sw1', dpid='0000000000000001',
                        datapath=_ovs_datapath())
        
    h1 = self.addHost('h1', ip='10.0.0.1/24', mac='ba:de:af:fe:00:01')
    
    h2 = self.addHost('h2', ip='10.0.0.2/24', mac='ba:de:af:fe:00:02')

    h3 = self.addHost('h3', ip='10.0.0.3/24', mac='ba:de:af:fe:00:03')
    
    for node1, node2 in [(h1, sw), (h2, sw), (h3, sw)]: 
      self.addLink(node1, node2,
                   intfName1=node1 + '-' + node2,
                   intfName2=node2 + '-' + node1)


def run():
  topo = CustomTopo()
  net = Mininet(topo=topo,
                controller=RemoteController('ofp-c1',
                                            ip='127.0.0.1',
                                            port=6633))
  net.start()
  _disable_offloads_if_netdev(net)
  CLI(net)
  net.stop()


def _disable_offloads_if_netdev(net):
  """netdev-Datapath (Userspace, z. B. WSL2 ohne openvswitch-Modul): der
     Re-Injection-Pfad verliert den CHECKSUM_PARTIAL-Status der veths, TCP-Pakete
     kommen am Ziel mit defekter Pruefsumme an und werden verworfen. Daher
     Offloads auf beiden Enden aller Links deaktivieren."""
  if not net.switches or getattr(net.switches[0], 'datapath', '') != 'user':
    return
  for node in net.hosts + net.switches:
    for intf in node.intfList():
      node.cmd('ethtool -K %s tx off tso off gso off sg off' % intf)


if __name__ == '__main__':
  run()
