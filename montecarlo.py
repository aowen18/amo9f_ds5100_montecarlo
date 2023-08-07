import numpy as np
import pandas as pd
import random

class Die:
    '''
    A class representing a die.

    Attributes:
        _die_df (pd.DataFrame): A private data frame containing the faces and their weights.
    '''
    def __init__(self, face):
        '''
        Initializes the die object with a set of faces and default weights.

        Args:
            face: A numpy array of sides (int or str) of the die.

        Raises:
            TypeError: If faces argument is not a NumPy array.
            ValueError: If the faces array does not have distinct values.
        '''
        if not isinstance(face, np.ndarray):
           raise TypeError("Input must be a numpy array")

        if len(face) > len(set(face)):
            raise ValueError("The sides must be unique values")

        weights = np.ones(len(face))

        self._die_df = pd.DataFrame(weights.T, index=face)

    def adj_weights(self, face, new_weight):
        '''
        Changes the weight of a single face in the die.

        Args:
            face: The face value to be changed.
            new_weight: The new weight to set for the specified face.

        Raises:
            IndexError: If the face is not in the die array.
            TypeError: If the new_weight is not numeric (integer or float) or castable as numeric.
        '''
        if face not in self._die_df.index:
            raise IndexError("The value is not in the array")

        if not isinstance(new_weight, (int,float)):
            raise TypeError("Weight must be an int or float value")

        self._die_df[0][face] = new_weight
        self._die_df = self._die_df.rename(columns= {0:'Weights'})
        return self._die_df

    def die_roll(self, roll = 1):
        '''
        Rolls the die one or more times.

        Args:
            roll: Number of times the die is rolled. Defaults to 1.

        Returns:
            list: A Python list of outcomes from the rolls.
        '''
        results = random.choices(self._die_df.index, weights=self._die_df['Weights'], k=roll)
        return results

    def show_df(self):
        """
        Returns a copy of the private die data frame containing faces and weights.

        Returns:
            pd.DataFrame: A copy of the private die data frame.
        """
        return self._die_df.copy()

class Game:
    '''
     A class representing a game with similar dice.

    Attributes:
        _dice_list (list): A list of similar dice (Die objects).
        _play_df (pd.DataFrame): A private data frame to store the results of the game.
    '''
    def __init__(self, _dice_list):
        '''
        Initializes the game object with a list of similar dice.

        Args:
            _dice_list (list): A list of already instantiated similar dice.
        '''
        self._dice_list = _dice_list
        self._play_df = None

    def play(self, roll):
        '''
        Plays the game by rolling all dice a given number of times.

        Args:
            roll (int): Number of times the dice should be rolled.

        Returns:
            pd.DataFrame: A data frame of results with roll number as index and dice outcomes as columns.
        '''
        results = {f'Die_{i}': die.die_roll(roll) for i, die in enumerate(self._dice_list)}
        self._play_df = pd.DataFrame(results)
        return self._play_df.copy()

    def recent_play(self, form='wide'):
        '''
        Shows the results of the most recent play.

        Args:
            form (str, optional): The form of the data frame to return ('wide' or 'narrow'). Defaults to 'wide'.

        Returns:
            pd.DataFrame: A copy of the private play data frame in the specified form.

        Raises:
            ValueError: If the user passes an invalid option for narrow or wide.
        '''
        if form not in ['wide','narrow']:
            raise ValueError("The form must be 'wide' or 'narrow'.")

        if form == 'wide':
            return self._play_df.copy()

        else:
            nar_df = self._play_df.melt(ignore_index=False).reset_index()
            nar_df = nar_df.rename(columns = {'index': 'Roll', 'variable': 'Die', 'value': 'Value'})
            return nar_df.copy()


class Analyzer:
    '''
    A class representing an analyzer for game results.

    Attributes:
        game (Game): A game object whose results will be analyzed.
    '''
    def __init__(self, game):
        '''
        Initializes the analyzer object with a game.

        Args:
            game (Game): A game object.

        Raises:
            ValueError: If the passed value is not a Game object.
        '''
        if not isinstance(game, Game):
            raise ValueError("The game object was not found in Game.")

        self.game = game

    def jackpot(self):
        '''
        Computes how many times the game resulted in a jackpot (all faces are the same).

        Returns:
            jp_count: A count of the number of jackpots.
        '''
        match = self.game.recent_play()
        jp_count = match.apply(lambda row: row.nunique() == 1, axis=1).sum()
        jp_count = jp_count.item()
        return jp_count

    def face_counts (self):
        '''
        Computes how many times a given face is rolled in each event.

        Returns:
            pd.DataFrame: A data frame of results with roll number as index, face values as columns, and count values in the cells.
        '''
        face = self.game.recent_play()
        face = face.apply(lambda row: row.value_counts()).fillna(0).astype(int)
        return face

    def combo_count (self):
        '''
        Computes the distinct combinations of faces rolled, along with their counts.

        Returns:
            pd.DataFrame: A data frame of results with distinct combinations as MultiIndex and count as a column.
        '''
        combo = self.game.recent_play()
        combo = np.sort(combo.values, axis = 1)
        combo_df = pd.DataFrame(combo).value_counts().reset_index()
        return combo_df

    def perm_count (self):
        '''
        Computes the distinct permutations of faces rolled, along with their counts.

        Returns:
            pd.DataFrame: A data frame of results with distinct permutations as MultiIndex and count as a column.
        '''
        perm = self.game.recent_play()
        perm = perm.value_counts().reset_index()
        return perm

d= Die(np.array([1,2,3,4,5,6]))
print(d.adj_weights(4, 10))
print(d.die_roll(10))
print(d.show_df())


game = Game([d,d,d])
print(game.play(10))
print(game.recent_play())

a = Analyzer(game)
print(a.jackpot())
print(a.face_counts())
print(a.combo_count())
print(a.perm_count())