# DS 5100 Final Project

## Metadata

### Project Name: Montecarlo Simulator 

### Name: Alexa Owen

## Synopsis 

### Install

```
pip install montecarlo
```

### Import

```
from Montecarlo import montecarlo
```

**or**

```
from montecarlo import Die, Game, Analyzer
```

### Necessary Packages 
```
import pandas as pd
import numpy as mp
import random
```

### Create Die

```
d = Die (np.array([1,2,3,4,5,6]))

d.adj_weights(2,5)

d.show_df()
```

### Play a Game
The default for g.recent_play() is 'wide' and returns a wide data frame.
```
g = Game ([d,d,d,d])

g.play(100)

g.recent_play()

g.recent_play ('narrow')
```

### Analyze a Game

```
a = Analyzer (g)

a.jackpot()

a.face_counts()

a.combo_count()

a.perm_count()
```

## API Description
```
NAME
    Montecarlo.montecarlo

CLASSES
    builtins.object
        Analyzer
        Die
        Game
    
    class Analyzer(builtins.object)
     |  Analyzer(game)
     |  
     |  A class representing an analyzer for game results.
     |  
     |  Attributes:
     |      game (Game): A game object whose results will be analyzed.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, game)
     |      Initializes the analyzer object with a game.
     |      
     |      Args:
     |          game (Game): A game object.
     |      
     |      Raises:
     |          ValueError: If the passed value is not a Game object.
     |  
     |  combo_count(self)
     |      Computes the distinct combinations of faces rolled, along with their counts.
     |      
     |      Returns:
     |          pd.DataFrame: A data frame of results with distinct combinations as MultiIndex and count as a column.
     |  
     |  face_counts(self)
     |      Computes how many times a given face is rolled in each event.
     |      
     |      Returns:
     |          pd.DataFrame: A data frame of results with roll number as index, face values as columns, and count values in the cells.
     |  
     |  jackpot(self)
     |      Computes how many times the game resulted in a jackpot (all faces are the same).
     |      
     |      Returns:
     |          jp_count: A count of the number of jackpots.
     |  
     |  perm_count(self)
     |      Computes the distinct permutations of faces rolled, along with their counts.
     |      
     |      Returns:
     |          pd.DataFrame: A data frame of results with distinct permutations as MultiIndex and count as a column.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Die(builtins.object)
     |  Die(face)
     |  
     |  A class representing a die.
     |  
     |  Attributes:
     |      _die_df (pd.DataFrame): A private data frame containing the faces and their weights.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, face)
     |      Initializes the die object with a set of faces and default weights.
     |      
     |      Args:
     |          face: A numpy array of sides (int or str) of the die.
     |      
     |      Raises:
     |          TypeError: If faces argument is not a NumPy array.
     |          ValueError: If the faces array does not have distinct values.
     |  
     |  adj_weights(self, face, new_weight)
     |      Changes the weight of a single face in the die.
     |      
     |      Args:
     |          face: The face value to be changed.
     |          new_weight: The new weight to set for the specified face.
     |      
     |      Raises:
     |          IndexError: If the face is not in the die array.
     |          TypeError: If the new_weight is not numeric (integer or float) or castable as numeric.
     |  
     |  die_roll(self, roll=1)
     |      Rolls the die one or more times.
     |      
     |      Args:
     |          roll: Number of times the die is rolled. Defaults to 1.
     |      
     |      Returns:
     |          list: A Python list of outcomes from the rolls.
     |  
     |  show_df(self)
     |      Returns a copy of the private die data frame containing faces and weights.
     |      
     |      Returns:
     |          pd.DataFrame: A copy of the private die data frame.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
    
    class Game(builtins.object)
     |  Game(_dice_list)
     |  
     |   A class representing a game with similar dice.
     |  
     |  Attributes:
     |      _dice_list (list): A list of similar dice (Die objects).
     |      _play_df (pd.DataFrame): A private data frame to store the results of the game.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, _dice_list)
     |      Initializes the game object with a list of similar dice.
     |      
     |      Args:
     |          _dice_list (list): A list of already instantiated similar dice.
     |  
     |  play(self, roll)
     |      Plays the game by rolling all dice a given number of times.
     |      
     |      Args:
     |          roll (int): Number of times the dice should be rolled.
     |      
     |      Returns:
     |          pd.DataFrame: A data frame of results with roll number as index and dice outcomes as columns.
     |  
     |  recent_play(self, form='wide')
     |      Shows the results of the most recent play.
     |      
     |      Args:
     |          form (str, optional): The form of the data frame to return ('wide' or 'narrow'). Defaults to 'wide'.
     |      
     |      Returns:
     |          pd.DataFrame: A copy of the private play data frame in the specified form.
     |      
     |      Raises:
     |          ValueError: If the user passes an invalid option for narrow or wide.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  __dict__
     |      dictionary for instance variables (if defined)
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
```
