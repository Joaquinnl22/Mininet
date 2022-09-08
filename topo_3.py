
from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.node import CPULimitedHost
from mininet.link import TCLink

def emptyNet():

    "Creacion de la net"

    net = Mininet( controller=Controller,link = TCLink )

    info( '*** Adding controller\n' )
    net.addController( 'c0' )

    info( '*** Adding hosts\n' )
    h1 = net.addHost( 'h1', ip='10.0.0.1' )
    h2 = net.addHost( 'h2', ip='10.0.0.2' )
    
    info( '*** Adding switch\n' )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    s3 = net.addSwitch( 's3' )
    s4 = net.addSwitch( 's4' )

    info( '*** Creating links\n' )
    net.addLink( s1, s2, bw=5, delay='50ms', loss=2, use_htb=True )
    net.addLink( s2, s3, bw=10, delay='70ms',loss=2, use_htb=True )
    net.addLink( s3, s4, bw=5, delay='30ms', loss=2, use_htb=True )
    net.addLink( h1, s1 )
    net.addLink( h2, s4 )
    
    
    
    info( '*** Starting network\n')
    net.start()
    
    info( '*** Running CLI\n' )
    CLI( net )

    info( '*** Stopping network' )
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    emptyNet()

