# DockerConsulSynchonizer

A simple script to sync from one consul instance to another.



## What's the difference between this script and consul cluster?

This script only syncs the k/v storage. However, consul is more than a k/v database. The purpose of this script is only for backup/syncs the state of `docker swarm`, so I just keep it as simple.



## Usage

Just defined two environment variable and it should keep syncing from source to target

`CONSUL_SOURCE` (i.e `192.168.99.101:8500`)

`CONSUL_TARGET` (i.e `192.168.99.102:8500`)



 