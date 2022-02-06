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
# Set-Up
1. Fork this repository and clone it to your machine.
2. Run `pipenv shell` to create a shell within the virtual environment.
3. MORE DETAIL TO COME


# Docking Station methods
`docking_station.dock(bike)` - docks a bike in the docking station, or raises an error if the station is full.  
`docking_station.release_bike(bike)` - releases a working bike from the docking station, or raises an error if there are no working bikes in the station.  

# Repairman methods
`repairman.collect_broken(docking_station)` - collects broken bikes from a docking station, provided the repairman has capacity to hold them.  
`repairman.deliver_broken(garage)` - repairman deposits broken bikes in a garage, subject to its capacity.  
`repairman.collect_working(garage)` - collects working bikes from a garage, provided the repairman has the capacity to hold them.  
`repairman.deliver_working(docking_station)` - repairman deposits working bikes at a docking station, subject to capacity.

# Garage methods  
`garage.repair(bike)` - repairs a broken bike, with accompanying Pythonesque onomatopoeias.

# Bike methods
`bike.report()` - changes a bike's status to not working.
