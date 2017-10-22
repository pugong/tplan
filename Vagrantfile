# -*- mode: ruby -*-
# vi: set ft=ruby :

# overrides = "#{__FILE__}.local"
# if File.exist?(overrides)
#     eval File.read(overrides)
# end

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "centos7-jdev"
  # config.vm.box_url ="http://192.168.1.202:8080/upload/download?file=%2Fhome%2Fdeploy%2Ftempupload%2Fcentos7-jdev.box"

  # Disable automatic box update checking. If you disable this, then
  # boxes will only be checked for updates when the user runs
  # `vagrant box outdated`. This is not recommended.
  # config.vm.box_check_update = false

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine. In the example below,
  # accessing "localhost:8080" will access port 80 on the guest machine.
  config.vm.network "forwarded_port", guest: 8080, host: 8080
#  if defined?(FORWARDED_PORTS)
#      FORWARDED_PORTS.each do |c|
#          guest, host = c
#          host = host.nil? ? guest : host
#          config.vm.network "forwarded_port", guest: guest, host: host
#      end
#  end

  # Create a private network, which allows host-only access to the machine
  # using a specific IP.
  # config.vm.network "private_network", ip: "192.168.33.10"

#  if defined?(PRIVATE_NETWORK)
#      config.vm.network "private_network", ip: PRIVATE_NETWORK
#  end

  # Create a public network, which generally matched to bridged network.
  # Bridged networks make the machine appear as another physical device on
  # your network.
  # config.vm.network "public_network"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.

  config.vm.synced_folder "./", "/vagrant", id: "outer", owner: "vagrant"
  # if defined?(SYNCED_FOLDERS)
  #     SYNCED_FOLDERS.each do |x|
  #         src, dst, owner = x
  #         owner = owner.nil? ? "vagrant" : owner
  #         config.vm.synced_folder src, dst, owner: owner
  #     end
  # end

  # Provider-specific configuration so you can fine-tune various
  # backing providers for Vagrant. These expose provider-specific options.
  # Example for VirtualBox:
  #
  config.vm.provider "virtualbox" do |vb|
    # Display the VirtualBox GUI when booting the machine
    # vb.gui = true
    vb.name = "tplan"
    # Customize the amount of memory on the VM:
    vb.memory = "1024"
  end
  #
  # View the documentation for the provider you are using for more
  # information on available options.

  # Define a Vagrant Push strategy for pushing to Atlas. Other push strategies
  # such as FTP and Heroku are also available. See the documentation at
  # https://docs.vagrantup.com/v2/push/atlas.html for more information.
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   apt-get update
  #   apt-get install -y apache2
      # start postgresql
      # su -l postgres -c "/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data/ -l /usr/local/pgsql/data/logfile start"

      # start zookeeper
      # /usr/local/develop/kafka_2.11-0.9.0.1/bin/zookeeper-server-start.sh /usr/local/develop/kafka_2.11-0.9.0.1/config/zookeeper.properties &

      # start kafka
      # /usr/local/develop/kafka_2.11-0.9.0.1/bin/kafka-server-start.sh /usr/local/develop/kafka_2.11-0.9.0.1/config/server.properties &

      # start redis
      # service redis_6379 restart

      # start tomcat
      # /usr/local/develop/apache-tomcat-8.5.6/bin/startup.sh

  # SHELL
end
