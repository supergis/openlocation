
OpenLocation Project.
{Exchange Location by using MQTT and GeoJSON.}

==============================================
Please Visit: 
http://www.github.com/supergis/openlocation
http://www.mqtt.org
http://git.eclipse.org/c/paho
==============================================

Install on Ubuntu:

sudo apt-get install python
sudo apt-get install python-pip

sudo pip install geojson

git clone git://git.eclipse.org/gitroot/paho/org.eclipse.paho.mqtt.python.git
cd org.eclipse.paho.mqtt.python
sudo python setup.py install 

=============================================

Install Mosquitto locally:

    sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
    sudo apt-get update

or From source:
hg clone https://bitbucket.org/oojah/mosquitto
sudo apt-get install libssl-dev
sudo apt-get install ares
sudo apt-get install xsltproc

