# Python Bikes
### Featuring [Bicycle Repairman](https://www.dailymotion.com/video/x2howud)

## Motivation
This project is a repeat of my earlier [Boris Bikes](https://github.com/marcusventin/boris-bikes) exercise. While that project was completed using Ruby, this project serves as an introduction to Python.

This project is intended to satisfy the following user stories:  
> As a person,  
> So that I can use a bike,  
> I'd like a docking station to release a bike.

> As a person,  
> So that I can use a good bike,  
> I'd like to see if a bike is working.

> As a member of the public,  
> So I can return bikes I've hired,  
> I want to dock my bike at the docking station.

> As a member of the public,  
> So I can decide whether to use the docking station,  
> I want to see a bike that has been docked.  

> As a member of the public,  
> So that I am not confused and charged unnecessarily,  
> I'd like docking stations not to release bikes when there are none available.

> As a maintainer of the system,  
> So that I can control the distribution of bikes,  
> I'd like docking stations not to accept more bikes than their capacity.

> As a system maintainer,  
> So that I can plan the distribution of bikes,  
> I want a docking station to have a default capacity of 20 bikes.

> As a system maintainer,  
> So that busy areas can be served more effectively,  
> I want to be able to specify a larger capacity when necessary.

> As a member of the public,  
> So that I reduce the chance of getting a broken bike in future,  
> I'd like to report a bike as broken when I return it.

> As a maintainer of the system,  
> So that I can manage broken bikes and not disappoint users,  
> I'd like docking stations not to release broken bikes.  

> As a maintainer of the system,  
> So that I can manage broken bikes and not disappoint users,  
> I'd like docking stations to accept returning bikes (broken or not).

> As a maintainer of the system,  
> So that I can manage broken bikes and not disappoint users,  
> I'd like vans to take broken bikes from docking stations and deliver them to garages to be fixed.  

> As a maintainer of the system,  
> So that I can manage broken bikes and not disappoint users,  
> I'd like vans to collect working bikes from garages and distribute them to docking stations.  

## Features
Users can dock and withdraw bikes from docking stations. Although broken bikes can be docked, they cannot be withdrawn.  

If a user encounters a problem with their bike, they can report it as not working.  

Bicycle repairmen can collect broken bikes from docking stations and deliver them to garages. They can also collect working bikes from garages and return them to docking stations.  

Garages can repair broken bikes.  

## How to Use
#### Set-Up
1. Fork this repository and clone it to your machine.
2. Check for bugs by running `pipenv shell` in your terminal to initialize a virtual environment, followed by `python -m unittest discover tests` to ensure that all tests are passing. 
3. Run `python3` to initialise your REPL.
4. Run `from lib.bike import Bike` to load the Bike class.
5. Run `from lib.docking_station import DockingStation` to load the DockingStation class.
6. Run `from lib.garage import Garage` to load the Garage class.
7. Run `from lib.repair_man import RepairMan` to load the RepairMan class.
8. Play to your heart's content using the following commands.

#### Docking Station Methods
`NAME = DockingStation(optional maximum capacity)` - creates a new DockingStation object with an optional maximum capacity - the default is currently set to 20.  
`.dock(bike)` - docks a bike in the docking station, or raises an error if the station is full.  
`.release_bike(bike)` - releases a working bike from the docking station, or raises an error if there are no working bikes in the station.  

#### Repairman Methods
`NAME = RepairMan(optional maximum capacity)` - creates a new RepairMan object with an optional maximum capacity - the default is currently set to 20.  
`.collect_broken(docking_station)` - collects broken bikes from a docking station, provided the repairman has capacity to hold them.  
`.deliver_broken(garage)` - repairman deposits broken bikes in a garage, subject to its capacity.  
`.collect_working(garage)` - collects working bikes from a garage, provided the repairman has the capacity to hold them.  
`.deliver_working(docking_station)` - repairman deposits working bikes at a docking station, subject to capacity.  

#### Garage methods  
`NAME = Garage(optional maximum capacity)` - creates a new Garage object with an optional maximum capacity - the default is currently set to 20.  
`.repair(bike)` - repairs a broken bike, with accompanying Pythonesque onomatopoeias.  

#### Bike methods  
`NAME = Bike()` - create a new Bike object. By default its status is set to "released" (not in dock), and it is fully operational.  
`.release()` - changes a bike's status to released.  
`.dock()` - changes a bike's status to docked.  
`.report()` - changes a bike's working status to not working.  
`.repair()` - changes a bike's working status to working.  

## Sample REPL Interaction
```
>>> from lib.bike import Bike
>>> from lib.docking_station import DockingStation
>>> from lib.garage import Garage
>>> from lib.repair_man import RepairMan
>>> dock = DockingStation()
>>> bike1 = Bike()
>>> monty = RepairMan()
>>> garage = Garage()
>>> dock.dock(bike1)
>>> dock.bikes
[<lib.bike.Bike object at 0x100bffdf0>]
>>> dock.release_bike()
>>> bike1 in dock.bikes
False
>>> bike1.report()
>>> bike1.working
False
>>> dock.dock(bike1)
>>> monty.collect_broken(dock)
>>> monty.deliver_broken(garage)
>>> garage.bikes
[<lib.bike.Bike object at 0x100bffdf0>]
>>> garage.repair(bike1)
Clink!
>>> garage.repair(bike1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/marcusventin/Projects/python_extensions/boris_bikes/lib/garage.py", line 10, in repair
    raise NotImplementedError("This bike already works.")
NotImplementedError: This bike already works.
>>> monty.collect_working(garage)
>>> garage.bikes
[]
>>> monty.bikes
[<lib.bike.Bike object at 0x100bffdf0>]
>>> monty.deliver_working(dock)
```
