from game import Directions
from game import Agent
from game import Actions

import random

from pacman_extraeFeatures import obtenerFeatures

#Importando librerías para ML
# requiere haber instalado (sugerencia: usar pip): scipy, numpy, matplotlib, pandas, 
# sklearn, keras, tensorflow

# version de Python
import sys
print('Python: {}'.format(sys.version))
# scipy
import scipy
print('scipy: {}'.format(scipy.__version__))
# numpy
import numpy
print('numpy: {}'.format(numpy.__version__))
# matplotlib
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
# pandas
import pandas
print('pandas: {}'.format(pandas.__version__))
# scikit-learn
import sklearn
print('sklearn: {}'.format(sklearn.__version__))
# keras
import keras
print('keras: {}'.format(keras.__version__))
# pickle
import pickle

# Fin de importación de

class my_ML_Agent(Agent):
    """
    This is a behaviour clonned agent!
    """

    def __init__(self):
        import pickle
        import numpy as np

        # open a file, where you stored the pickled data
        file_modeloCargado = open('modeloEntrenado.p', 'rb')

        # load information from that file
        self.modelo = pickle.load(file_modeloCargado)

        # close the file
        file_modeloCargado.close()

        self.cantAccionesInvalidas = 0
   

    def getAction(self, state):
        """
        Returns the next action in the path chosen earlier (in
        registerInitialState).  Return Directions.STOP if there is no further
        action to take.

        state: a GameState object (pacman.py)
        """
        features = obtenerFeatures(state).reshape(1,-1)

        #Si es un DecisionTreeClassifier
        accionNum = int(self.modelo.predict(features))
        directions = list(Directions.LEFT)
        accionStr = directions[accionNum]
        legal_actions = state.getLegalActions()
        
        if accionStr in legal_actions:
            action = accionStr 
        else:
            action = random.choice(legal_actions)
        
        return action # Directions.STOP
        #Si es un keras sequential
        #accionNum = self.modelo.predict(features).argmax(axis=-1)

        #Convertir el índice de la acción a su respectivo string

        ####Si deseas, usa la variable `self.cantAccionesInvalidas`

        #Codificar el comportamiento del agente para el caso de predecir una accion inválida
        #return 'Stop'
