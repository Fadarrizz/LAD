# Heuristics - Amstelhaege

This code is designed to create housingplan of 3 variations (20, 40 or 60 houses).
The land, upon which 3 different housetypes can be built, is 160 by 180 meters
and 20% of its surface includes water.

The objective is to create a design that is the most lucrative, as the price of
a house inflates with every extra meter of detachment.
Another objective is to find out what the maximum amount of detached meters that
a house can have is.

## Getting Started

These instructions will help to get the project up and running for your testing
purposes.

### Prerequisites

The software that's necessary to run the code:
    * [Python3](https://www.python.org/download/releases/3.0/) was used to write the code.
    * [Matplotlib](http://matplotlib.org/users/installing.html) is necessary to plot the grid.
    * [Atom](https://atom.io/) is the texteditor we have used.


### Installing

With Windows, matplotlib can be installed using pip.

```
python -m pip install -U pip setuptools
python -m pip install matplotlib
```


## Running the tests

Classes.py contains the classes for the three different housetypes
(all three subclasses come from one parentclass Building) and a completely
separate class for the waterbody.

For creating a grid in Matplotlib, run:

```
python grid.py
```

Select the number of buildings to place

```
20, 40 or 60
```
After all the called functions within grid.py have run, grid.py will show a grid
containing every house that has been instanced.

The BuildingGenerator function in BuildingGenerator.py is be called upon in
grid.py, it creates instances of houses puts them in an array.
To get unique x and y coordinates,the function getCoordinates from coordinates.py is called.


Coordinates.py contains a function to iterate over all the coordinates of the already placed houses
and check if the new coordinates don't match exisiting coordinates. This is done to avoid overlap of houses.

## Authors

* **Leyla Banchaewa** - [Nova0125](https://github.com/Nova0125)
* **Auke Geerts** - [Fadarrizz](https://github.com/Fadarrizz)
* **Daniel Walters** - [Danprog](https://github.com/Danprog)


## Acknowledgments

* Readme template made by [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
