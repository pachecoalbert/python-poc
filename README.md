python-poc
==========

-- Install SetupTools
sudo curl https://bootstrap.pypa.io/ez_setup.py -o - | sudo python



-- Install boto

sudo easy_install boto

-- Intall Paramiko for SSH2 secure connections
git clone https://github.com/paramiko/paramiko
cd paramiko
sudo python setup.py install

-- Setup euca2ools

git clone https://github.com/eucalyptus/euca2ools.git
cd euca2ools/


sudo easy_install m2crypto




-- Store credentials in the boto config file



