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
You'll be asked to give an option for an algorithm:
```
Select option: 1. Hillclimber or 2. Simluated Annealing
```
Both Hillclimber and Simulated Annealing use the Random algorithm as input.

### Random algorithm

Select the number of buildings to place:
```
20, 40 or 60
```
The BuildingQueue function will build a list of buildings according to this amount.
Maison will be added to the list first, as they are the biggest, than bungalows
and than the houses.

The BuildingGenerator function creates instances of houses and puts them in a list.
To get unique x and y coordinates,the function getCoordinates is called.

GetCoordinates will generate coordinates and check for any collision with water
or other already placed buildings. This is done by calling a few functions that
check different aspects, such as overlap of buildings and overlap of freespace.

When all the buildings have been added to the list by the BuildingGenerator function,
a function to calculate the total score is being ran. This function is located in the
classes.py file.

This function calculates the score of all buildings from the just created list. It
measures the distance between a building and its neighbours, selects the smallest distance
and calculates a score from here. The scores from all buildings are being summed up.

Last, but not least, the Grid function is being called. This function first places
four waterbodies on the map, as testing has shown that this gives the best results.
Then, it loops over the list of buildings and addes them to the map one by one.
With a simple plt.show() statement will the map be plotted.

### Hillclimber

The Hillclimber starts by saving the old score from the Random algorithm.
Then, it loops a given amount. In this loop it will randomly select two buildings from
the Buildingsplaced list, the list that BuildingGenerator has filled.

After this, it will select either to generated new coordinates for the first selected building, or swap the first with the second building. This will be chosen randomly.

Generating new coordinates will be done the same way as with the Random algorithm.
Once new coordinates are chosen and proven to be valid, a new score will be calculated.
This score will be compared with the old score. If the score is not better, the coordinates
will be turned to the previous ones. If it is better, that score will become the new score.

When two buildings are swapped, checks for any collision will be done. If there is any,
the two buildings will be swapped back. If not, a new score will be calulated and compared
with the previous score. If it is the same or lower, the buildings will be swapped back.
If the score is higher, that score will become the new score.

In each iteration, a different building will be selected and one of the two methods to
try to improve the score, will be applied.

The last best score will be returned and picked up by grid, along with the updated list
of buildings with their new coordinates. And of course, a new plot will be shown.

### Simulated Annealing

Simulated Annealing works almost the same as the Hillclimber. The only differences is
that is it accepts some deteriorations. At the top of the algorithm, a temperature and
a minimal temperature, along with an alpha, the cooling factor.

Where the Hillclimber randomly selects a method to try to improve the score, the Simulated
Annealing algorithm also defines an acceptance probility and checks if this is higher
a random number between 0 and 1, it will calculate a new score.

Then, it decreases the temperature by multiplying the temperature on the moment with
the alpha. It also appends the score the a list of scores.

Finally, it selects the highest score of the list and returns this number to grid.
A new plot with updated buildings will be shown.

## Authors

* **Leyla Banchaewa** - [Nova0125](https://github.com/Nova0125)
* **Auke Geerts** - [Fadarrizz](https://github.com/Fadarrizz)
* **Daniel Walters** - [Danprog](https://github.com/Danprog)


## Acknowledgments

* Readme template made by [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
