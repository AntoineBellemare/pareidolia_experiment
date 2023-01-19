#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.90.3),
    on March 29, 2021, at 21:51
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock, parallel
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import time

MEG_SETTINGS = {
'RS_start':int('00000001', 2),
'RS_stop':int('00000010', 2),
'cross':int('00000011', 2),
'im_start':int('00000100', 2),
'im_stop':int('00000101', 2),
'resp':int('00000110', 2),
'bloc_start':int('00001011', 2),
'bloc_start_sham':int('00001100', 2)
}


# Activate parallel port
port = parallel.ParallelPort(address=0x3FF8)
#port = []
def send_data(port, data):
    port.setData(data)
    print(data)
    time.sleep(0.001)
    port.setData(0)  # reset

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'Cloud_Experiment_FR_REAL'  # from the Builder filename that created this script
expInfo = {'session': '001', 'participant': ''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1024, 768], fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
Instruction = visual.TextStim(win=win, name='Instruction',
    text=u"Bienvenue \xe0 cette exp\xe9rience sur la par\xe9idolie.\nL'exp\xe9rience se divise en 8 blocs d'une dur\xe9e d'environ 12 minutes.\nVous aurez l'occasion, entre chaque bloc, de prendre un moment de r\xe9pis si d\xe9sir\xe9.\n\nAppuyez avec l'index de votre main gauche.\n\n",
    font='Arial',
    pos=[0, 0], height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Instructions2"
Instructions2Clock = core.Clock()
fatigueinstructions2 = visual.TextStim(win=win, name='fatigueinstructions2',
    text=u"T\xe2che:\n\nDes images de nuages informatiques vous seront pr\xe9sent\xe9es.\nVotre t\xe2che consistera \xe0 percevoir le plus grand nombre de formes figuratives dans chaque image.\nLorsque vous aurez d\xe9tect\xe9 une premi\xe8re forme figurative, vous devrez appuyer avec votre index.\n\n\nVous aurez par la suite \xe0 continuer votre recherche de formes figuratives pendant toute la pr\xe9sentation de l'image.\nApr\xe8s chaque image, il vous sera demand\xe9 le nombre total de formes per\xe7ues.\nVous utiliserez vos pouces pour changer de choix de r\xe9ponse, et vos index pour valider votre r\xe9ponse. Vous aurez 4 secondes pour donner votre réponse à chaque essai. \nAvant chaque bloc, il vous sera indiqu\xe9 si vous devez utiliser votre index gauche ou droit afin de \nsignaler la d\xe9tection d'une premi\xe8re forme reconnaissable.\n\n\xc0 la fin de l'exp\xe9rience, les images pour lesquelles vous avez r\xe9pondu avoir per\xe7u plusieurs formes figuratives vous seront pr\xe9sent\xe9es \xe0 nouveau\nafin que vous partagiez vos perceptions avec l'exp\xe9rimentateur.\n\nVous commencerez par un bloc d'essai pour vous familiariser avec la t\xe2che.\n\nVeuillez appuyer avec l'index gauche pour continuer.\n\n\nBonne exp\xe9rience!\n\n",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Resting_state_instructions"
Resting_state_instructionsClock = core.Clock()
Resting = visual.TextStim(win=win, name='Resting',
    text=u"Avant de d\xe9buter l'exp\xe9rience,\nnous allons vous demander de rester immobile\npendant 3 min, les yeux ouverts.\nVous n'avez aucune t\xe2che particuli\xe8re \xe0 effectuer\npendant ces 3 minutes, mis \xe0 part garder votre\nregard fix\xe9 sur la croix de fixation.\n\nIl vous sera demand\xe9 de faire le m\xeame exercice\n\xe0 la fin de l'exp\xe9rience.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Resting_state"
Resting_stateClock = core.Clock()
fix_resting_state = visual.ImageStim(
    win=win, name='fix_resting_state',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Start_pratique"
Start_pratiqueClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text=u"Le bloc de pratique est constitu\xe9 de 10 essais.\nVeuillez appuyer avec l'index droit pour commencer le bloc de pratique.\nVous aurez \xe0 utiliser l'index droit pour signaler \nla d\xe9tection d'un objet pour l'enti\xe8ret\xe9 de ce bloc, ",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nVeuillez fermer les yeux et attendre les consignes de l'exp\xe9rimentateur.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Start_b1"
Start_b1Clock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=u"Vous aurez \xe0 utiliser l'index' gauche pour signaler \nla d\xe9tection d'un objet pour l'enti\xe8ret\xe9 de ce bloc, \n\n\nAppuyez avec l'index gauche\npour commencer l'exp\xe9rience.\n\n",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Start_b2"
Start_b2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text=u"Vous venez de terminer la moiti\xe9 du bloc.\nLe bloc suivant commencera dans 30 secondes.\n Vous pouvez appuyer avec l'index gauche lorsque vous êtes prêt à continuer \n",
    font=u'Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nVeuillez fermer les yeux et attendre les consignes de l'exp\xe9rimentateur.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Start_b3"
Start_b3Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text=u"Vous aurez \xe0 utiliser l'index droit pour signaler \nla d\xe9tection d'un objet pour l'enti\xe8ret\xe9 de ce bloc, \n\nAppuyez avec l'index droit pour continuer l'exp\xe9rience.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Start_b4"
Start_b4Clock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text=u"Vous venez de terminer la moiti\xe9 du bloc.\nLe bloc suivant commencera dans 30 secondes.\n\nVous pouvez appuyer avec l'index droit lorsque vous êtes prêt à continuer \n",
    font=u'Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nVeuillez fermer les yeux et attendre les consignes de l'exp\xe9rimentateur.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Start_b5"
Start_b5Clock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text=u"Vous aurez \xe0 utiliser l'index gauche pour signaler \nla d\xe9tection d'un objet pour l'enti\xe8ret\xe9 de ce bloc, \n\nAppuyez avec l'index gauche\npour continuer l'exp\xe9rience.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Start_b6"
Start_b6Clock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text=u"Vous venez de terminer la moiti\xe9 du bloc.\nLe bloc suivant commencera dans 30 secondes.\n\nVous pouvez appuyer avec l'index gauche lorsque vous êtes prêt à continuer ",
    font=u'Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nVeuillez fermer les yeux et attendre les consignes de l'exp\xe9rimentateur.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Start_b7"
Start_b7Clock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text=u"Vous aurez \xe0 utiliser l'index droit pour signaler \nla d\xe9tection d'un objet pour l'enti\xe8ret\xe9 de ce bloc, \n\nAppuyez avec l'index droit pour continuer l'exp\xe9rience.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Start_b8"
Start_b8Clock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text=u"Vous venez de terminer la moiti\xe9 du bloc.\nLe bloc suivant commencera dans 30 secondes.\n\nVous pouvez appuyer avec l'index droit lorsque vous êtes prêt à continuer \n",
    font=u'Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nVeuillez fermer les yeux et attendre les consignes de l'exp\xe9rimentateur.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Start_b9"
Start_b9Clock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text=u"Vous aurez \xe0 utiliser l'index gauche pour signaler \nla d\xe9tection d'un objet pour l'enti\xe8ret\xe9 de ce bloc, \n\nAppuyez avec l'index gauche\npour continuer l'exp\xe9rience.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Start_b10"
Start_b10Clock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text=u"Vous venez de terminer la moiti\xe9 du bloc.\nLe bloc suivant commencera dans 30 secondes.\n\nVous pouvez appuyer avec l'index gauche lorsque vous êtes prêt à continuer ",
    font=u'Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nVeuillez fermer les yeux et attendre les consignes de l'exp\xe9rimentateur.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Start_b11"
Start_b11Clock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text=u"Vous aurez \xe0 utiliser l'index droit pour signaler \nla d\xe9tection d'un objet pour l'enti\xe8ret\xe9 de ce bloc, \n\nAppuyez avec l'index droit pour continuer l'exp\xe9rience.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Start_b12"
Start_b12Clock = core.Clock()
text_17 = visual.TextStim(win=win, name='text_17',
    text=u"Vous venez de terminer la moiti\xe9 du bloc.\nLe bloc suivant commencera dans 30 secondes.\n\nVous pouvez appuyer avec l'index droit lorsque vous êtes prêt à continuer \n",
    font=u'Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nVeuillez fermer les yeux et attendre les consignes de l'exp\xe9rimentateur.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Redondance"
RedondanceClock = core.Clock()
Redondance_question = visual.RatingScale(win=win, name='Redondance_question', marker=u'triangle',
                                        size=0.8, pos=[0.0, -0.4], low=1, high=7,
                                        labels=[u'Presque toujours la m\xeame cat\xe9gorie', u' Cat\xe9gories vari\xe9es'],
                                        scale=u"Pour l'ensemble des 6 premiers blocs, veuillez indiquer \xe0 quel point vos perceptions \xe9taient diversifi\xe9es",
                                        disappear=True, respKeys = (), leftKeys = '5', rightKeys = '6', acceptKeys = ['4', '7'],
                                        markerStart = '4')
# Initialize components for Routine "Instructions_sham"
Instructions_shamClock = core.Clock()
instructions_sham = visual.TextStim(win=win, name='instructions_sham',
    text=u"Au courant des 6 premiers blocs que vous venez de compl\xe9ter, \nun algorithme d\u2019apprentissage-machine s\u2019est entra\xeen\xe9 \xe0 diff\xe9rencier les images pour lesquelles vous rapportiez une forte par\xe9idolie \nde celles o\xf9 la par\xe9idolie \xe9tait inexistante ou faible. \nPour les 2 derniers blocs, cet algorithme d'apprentissage-machine utilisera \nvotre activit\xe9 c\xe9r\xe9brale afin de cr\xe9er en temps r\xe9el \nles images de nuages g\xe9n\xe9ratifs de mani\xe8re \xe0 soit maximiser ou réduire votre par\xe9idolie. \n\nPour le premier bloc, l'algorithme cherchera à MAXIMISER votre paréidolie. \n\nVous aurez \xe0 utiliser l'index gauche pour signaler \nla d\xe9tection d'un objet pour l'enti\xe8ret\xe9 de ce bloc.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Start_sham2"
Start_sham2Clock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text=u"Vous venez de terminer la moiti\xe9 du bloc.\n\nVous pouvez appuyer avec l'index gauche lorsque vous êtes prêt à continuer \n",
    font=u'Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nVeuillez fermer les yeux et attendre les consignes de l'exp\xe9rimentateur.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Start_sham3"
Start_sham3Clock = core.Clock()
text_19 = visual.TextStim(win=win, name='text_19',
    text=u"Pour ce dernier bloc, l'algorithme cherchera à RÉDUIRE votre paréidolie. \nVous aurez \xe0 utiliser l'index droit pour signaler \nla d\xe9tection d'un objet pour l'enti\xe8ret\xe9 de ce bloc, \n\nAppuyez avec l'index droit pour continuer l'exp\xe9rience.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker='triangle', size=1.0, pos=[0.0, 0.0], low=0, high=5, labels=['0', ' 5 et plus'], scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us", disappear=True)

# Initialize components for Routine "Start_sham4"
Start_sham4Clock = core.Clock()
text_20 = visual.TextStim(win=win, name='text_20',
    text=u"Vous venez de terminer la moiti\xe9 du bloc.\n\nVous pouvez appuyer avec l'index droit lorsque vous êtes prêt à continuer \n",
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color=u'white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
empty_gray = visual.ImageStim(
    win=win, name='empty_gray',
    image='empty_gray', mask=None,
    ori=0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
fixation_cross = visual.ImageStim(
    win=win, name='fixation_cross',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=[0, 0], size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
n_objets = visual.RatingScale(win=win, name='n_objets', marker=u'triangle',
                                size=1.0, pos=[0.0, 0.0], low=0, high=5,
                                labels=[u'0', u' 5 et plus'],
                                scale=u"Veuillez indiquer le nombre d'objets significatifs per\xe7us",
                                disappear=True, respKeys = (), leftKeys = '5', rightKeys = '6', acceptKeys = ['4', '7'],
                                markerStart = '0')
# Initialize components for Routine "Fin_bloc"
Fin_blocClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text=u"Vous venez de terminer le bloc.\n\nVeuillez fermer les yeux et attendre les consignes de l'exp\xe9rimentateur.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Resting_state_instructions2"
Resting_state_instructions2Clock = core.Clock()
resting_instructions_end = visual.TextStim(win=win, name='resting_instructions_end',
    text=u"Nous allons maintenant vous demander\nde rester immobile pendant 3 minutes\nde la m\xeame fa\xe7on que lorsqu'au d\xe9but de\nl'exp\xe9rience, en fixant la croix au centre de\nl'\xe9cran et en ne faisant aucune t\xe2che particuli\xe8re.",
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "Resting_state"
Resting_stateClock = core.Clock()
fix_resting_state = visual.ImageStim(
    win=win, name='fix_resting_state',
    image='fixation_cross', mask=None,
    ori=0, pos=(0, 0), size=[0.4, 0.71111111],
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "Sham"
ShamClock = core.Clock()
rating_sham = visual.RatingScale(win=win, name='rating_sham', marker=u'triangle', size=1.0, pos=[0.0, -0.4],
                                low=0, high=10,labels=[u'Aucune différence', u' Grande différence'], showValue=True,
                                scale=u'\xc0 quel point avez-vous per\xe7u une diff\xe9rence entre les 2 derniers blocs et les blocs pr\xe9c\xe9dents ?',
                                disappear=True, respKeys = (), leftKeys = '5', rightKeys = '6', acceptKeys = ['4', '7'],
                                        markerStart = '5')
# Initialize components for Routine "Finito"
FinitoClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text=u"Merci d'avoir particit\xe9 \xe0 cette exp\xe9rience sur la par\xe9idolie.\nVous pouvez faire signe \xe0 l'exp\xe9rimentateur.",
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
end_instructions = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [Instruction, end_instructions]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Instruction* updates
    if t >= 0.0 and Instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        Instruction.tStart = t
        Instruction.frameNStart = frameN  # exact frame index
        Instruction.setAutoDraw(True)

    # *end_instructions* updates
    if t >= 0.0 and end_instructions.status == NOT_STARTED:
        # keep track of start time/frame for later
        end_instructions.tStart = t
        end_instructions.frameNStart = frameN  # exact frame index
        end_instructions.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(end_instructions.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if end_instructions.status == STARTED:
        theseKeys = event.getKeys(keyList=['4'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            end_instructions.keys = theseKeys[-1]  # just the last key pressed
            end_instructions.rt = end_instructions.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if end_instructions.keys in ['', [], None]:  # No response was made
    end_instructions.keys=None
thisExp.addData('end_instructions.keys',end_instructions.keys)
if end_instructions.keys != None:  # we had a response
    thisExp.addData('end_instructions.rt', end_instructions.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions2"-------
t = 0
Instructions2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions2Components = [fatigueinstructions2, key_resp_4]
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions2"-------
while continueRoutine:
    # get current time
    t = Instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *fatigueinstructions2* updates
    if t >= 0.0 and fatigueinstructions2.status == NOT_STARTED:
        # keep track of start time/frame for later
        fatigueinstructions2.tStart = t
        fatigueinstructions2.frameNStart = frameN  # exact frame index
        fatigueinstructions2.setAutoDraw(True)

    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['4'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions2"-------
for thisComponent in Instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys=None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "Instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Resting_state_instructions"-------
t = 0
Resting_state_instructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = event.BuilderKeyResponse()
# keep track of which components have finished
Resting_state_instructionsComponents = [Resting, key_resp_9]
for thisComponent in Resting_state_instructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Resting_state_instructions"-------
while continueRoutine:
    # get current time
    t = Resting_state_instructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *Resting* updates
    if t >= 0.0 and Resting.status == NOT_STARTED:
        # keep track of start time/frame for later
        Resting.tStart = t
        Resting.frameNStart = frameN  # exact frame index
        Resting.setAutoDraw(True)

    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_9.keys = theseKeys[-1]  # just the last key pressed
            key_resp_9.rt = key_resp_9.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Resting_state_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Resting_state_instructions"-------
for thisComponent in Resting_state_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys=None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.nextEntry()
# the Routine "Resting_state_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Resting_state"-------
t = 0
Resting_stateClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()
# keep track of which components have finished
Resting_stateComponents = [fix_resting_state, key_resp_10]
for thisComponent in Resting_stateComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Resting_state"-------
while continueRoutine:
    # get current time
    t = Resting_stateClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *fix_resting_state* updates
    if t >= 0.0 and fix_resting_state.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_resting_state.tStart = t
        fix_resting_state.frameNStart = frameN  # exact frame index
        fix_resting_state.setAutoDraw(True)
        win.callOnFlip(send_data, port, MEG_SETTINGS['RS_start'])
    frameRemains = 0.0 + 180- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fix_resting_state.status == STARTED and t >= frameRemains:
        fix_resting_state.setAutoDraw(False)
        win.callOnFlip(send_data, port, MEG_SETTINGS['RS_stop'])

    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_10.keys = theseKeys[-1]  # just the last key pressed
            key_resp_10.rt = key_resp_10.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Resting_stateComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Resting_state"-------
for thisComponent in Resting_stateComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys=None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.nextEntry()
# the Routine "Resting_state" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_pratique"-------
t = 0
Start_pratiqueClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_pratiqueComponents = [text_3, key_resp_5]
for thisComponent in Start_pratiqueComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_pratique"-------
while continueRoutine:
    # get current time
    t = Start_pratiqueClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t
        text_3.frameNStart = frameN  # exact frame index
        text_3.setAutoDraw(True)

    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['7'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_pratiqueComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_pratique"-------
for thisComponent in Start_pratiqueComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys=None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.nextEntry()
# the Routine "Start_pratique" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_practice = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_pratique.xlsx'),
    seed=None, name='trials_practice')
thisExp.addLoop(trials_practice)  # add the loop to the experiment
thisTrials_practice = trials_practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
if thisTrials_practice != None:
    for paramName in thisTrials_practice:
        exec('{} = thisTrials_practice[paramName]'.format(paramName))

for thisTrials_practice in trials_practice:
    currentLoop = trials_practice
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_practice.rgb)
    if thisTrials_practice != None:
        for paramName in thisTrials_practice:
            exec('{} = thisTrials_practice[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_practice (TrialHandler)
    trials_practice.addData('n_objets.response', n_objets.getRating())
    trials_practice.addData('n_objets.rt', n_objets.getRT())
    trials_practice.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_practice.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_practice.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_practice'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)

    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_b1"-------
t = 0
Start_b1Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b1Components = [text, key_resp_2]
for thisComponent in Start_b1Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b1"-------
while continueRoutine:
    # get current time
    t = Start_b1Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)

    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['4'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b1"-------
for thisComponent in Start_b1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys=None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Start_b1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_1 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_01.xlsx'),
    seed=None, name='trials_1')
thisExp.addLoop(trials_1)  # add the loop to the experiment
thisTrial_1 = trials_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
if thisTrial_1 != None:
    for paramName in thisTrial_1:
        exec('{} = thisTrial_1[paramName]'.format(paramName))

start_bloc = True
for thisTrial_1 in trials_1:
    currentLoop = trials_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_1.rgb)
    if thisTrial_1 != None:
        for paramName in thisTrial_1:
            exec('{} = thisTrial_1[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    if start_bloc == True:
        win.callOnFlip(send_data, port, MEG_SETTINGS['bloc_start'])
        start_bloc = False
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_1 (TrialHandler)
    trials_1.addData('n_objets.response', n_objets.getRating())
    trials_1.addData('n_objets.rt', n_objets.getRT())
    trials_1.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_1.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_1.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_1'


# ------Prepare to start Routine "Start_b2"-------
t = 0
Start_b2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b2Components = [text_2, key_resp_3]
for thisComponent in Start_b2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b2"-------
while continueRoutine:
    # get current time
    t = Start_b2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t
        text_2.frameNStart = frameN  # exact frame index
        text_2.setAutoDraw(True)

    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = event.getKeys(keyList=['4'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_3.keys = theseKeys[-1]  # just the last key pressed
            key_resp_3.rt = key_resp_3.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b2"-------
for thisComponent in Start_b2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys=None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.nextEntry()
# the Routine "Start_b2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_02.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('n_objets.response', n_objets.getRating())
    trials_2.addData('n_objets.rt', n_objets.getRT())
    trials_2.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_2.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_2.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)

    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_b3"-------
t = 0
Start_b3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_12 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b3Components = [text_8, key_resp_12]
for thisComponent in Start_b3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b3"-------
while continueRoutine:
    # get current time
    t = Start_b3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t
        text_8.frameNStart = frameN  # exact frame index
        text_8.setAutoDraw(True)

    # *key_resp_12* updates
    if t >= 0.0 and key_resp_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_12.tStart = t
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_12.status == STARTED:
        theseKeys = event.getKeys(keyList=['7'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_12.keys = theseKeys[-1]  # just the last key pressed
            key_resp_12.rt = key_resp_12.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b3"-------
for thisComponent in Start_b3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys=None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.nextEntry()
# the Routine "Start_b3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_03.xlsx'),
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

start_bloc = True
for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    if start_bloc == True:
        win.callOnFlip(send_data, port, MEG_SETTINGS['bloc_start'])
        start_bloc = False
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_3 (TrialHandler)
    trials_3.addData('n_objets.response', n_objets.getRating())
    trials_3.addData('n_objets.rt', n_objets.getRT())
    trials_3.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_3.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_3.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_3'


# ------Prepare to start Routine "Start_b4"-------
t = 0
Start_b4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_14 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b4Components = [text_9, key_resp_14]
for thisComponent in Start_b4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b4"-------
while continueRoutine:
    # get current time
    t = Start_b4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_9* updates
    if t >= 0.0 and text_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_9.tStart = t
        text_9.frameNStart = frameN  # exact frame index
        text_9.setAutoDraw(True)

    # *key_resp_14* updates
    if t >= 0.0 and key_resp_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_14.tStart = t
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_14.status == STARTED:
        theseKeys = event.getKeys(keyList=['7'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_14.keys = theseKeys[-1]  # just the last key pressed
            key_resp_14.rt = key_resp_14.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b4"-------
for thisComponent in Start_b4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys=None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.nextEntry()
# the Routine "Start_b4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_4 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_04.xlsx'),
    seed=None, name='trials_4')
thisExp.addLoop(trials_4)  # add the loop to the experiment
thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
if thisTrial_4 != None:
    for paramName in thisTrial_4:
        exec('{} = thisTrial_4[paramName]'.format(paramName))

for thisTrial_4 in trials_4:
    currentLoop = trials_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
    if thisTrial_4 != None:
        for paramName in thisTrial_4:
            exec('{} = thisTrial_4[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_4 (TrialHandler)
    trials_4.addData('n_objets.response', n_objets.getRating())
    trials_4.addData('n_objets.rt', n_objets.getRT())
    trials_4.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_4.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_4.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_4'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)

    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_b5"-------
t = 0
Start_b5Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_15 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b5Components = [text_10, key_resp_15]
for thisComponent in Start_b5Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b5"-------
while continueRoutine:
    # get current time
    t = Start_b5Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_10* updates
    if t >= 0.0 and text_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_10.tStart = t
        text_10.frameNStart = frameN  # exact frame index
        text_10.setAutoDraw(True)

    # *key_resp_15* updates
    if t >= 0.0 and key_resp_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_15.tStart = t
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_15.status == STARTED:
        theseKeys = event.getKeys(keyList=['4'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_15.keys = theseKeys[-1]  # just the last key pressed
            key_resp_15.rt = key_resp_15.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b5"-------
for thisComponent in Start_b5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys=None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.nextEntry()
# the Routine "Start_b5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_5 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_05.xlsx'),
    seed=None, name='trials_5')
thisExp.addLoop(trials_5)  # add the loop to the experiment
thisTrial_5 = trials_5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
if thisTrial_5 != None:
    for paramName in thisTrial_5:
        exec('{} = thisTrial_5[paramName]'.format(paramName))

start_bloc = True
for thisTrial_5 in trials_5:
    currentLoop = trials_5
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_5.rgb)
    if thisTrial_5 != None:
        for paramName in thisTrial_5:
            exec('{} = thisTrial_5[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    if start_bloc == True:
        win.callOnFlip(send_data, port, MEG_SETTINGS['bloc_start'])
        start_bloc = False
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_5 (TrialHandler)
    trials_5.addData('n_objets.response', n_objets.getRating())
    trials_5.addData('n_objets.rt', n_objets.getRT())
    trials_5.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_5.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_5.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_5'


# ------Prepare to start Routine "Start_b6"-------
t = 0
Start_b6Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_16 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b6Components = [text_11, key_resp_16]
for thisComponent in Start_b6Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b6"-------
while continueRoutine:
    # get current time
    t = Start_b6Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_11* updates
    if t >= 0.0 and text_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_11.tStart = t
        text_11.frameNStart = frameN  # exact frame index
        text_11.setAutoDraw(True)

    # *key_resp_16* updates
    if t >= 0.0 and key_resp_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_16.tStart = t
        key_resp_16.frameNStart = frameN  # exact frame index
        key_resp_16.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_16.status == STARTED:
        theseKeys = event.getKeys(keyList=['4'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_16.keys = theseKeys[-1]  # just the last key pressed
            key_resp_16.rt = key_resp_16.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b6Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b6"-------
for thisComponent in Start_b6Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_16.keys in ['', [], None]:  # No response was made
    key_resp_16.keys=None
thisExp.addData('key_resp_16.keys',key_resp_16.keys)
if key_resp_16.keys != None:  # we had a response
    thisExp.addData('key_resp_16.rt', key_resp_16.rt)
thisExp.nextEntry()
# the Routine "Start_b6" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_6 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_06.xlsx'),
    seed=None, name='trials_6')
thisExp.addLoop(trials_6)  # add the loop to the experiment
thisTrial_6 = trials_6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
if thisTrial_6 != None:
    for paramName in thisTrial_6:
        exec('{} = thisTrial_6[paramName]'.format(paramName))

for thisTrial_6 in trials_6:
    currentLoop = trials_6
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_6.rgb)
    if thisTrial_6 != None:
        for paramName in thisTrial_6:
            exec('{} = thisTrial_6[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_6 (TrialHandler)
    trials_6.addData('n_objets.response', n_objets.getRating())
    trials_6.addData('n_objets.rt', n_objets.getRT())
    trials_6.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_6.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_6.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_6'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)

    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_b7"-------
t = 0
Start_b7Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_17 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b7Components = [text_12, key_resp_17]
for thisComponent in Start_b7Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b7"-------
while continueRoutine:
    # get current time
    t = Start_b7Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_12* updates
    if t >= 0.0 and text_12.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_12.tStart = t
        text_12.frameNStart = frameN  # exact frame index
        text_12.setAutoDraw(True)

    # *key_resp_17* updates
    if t >= 0.0 and key_resp_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_17.tStart = t
        key_resp_17.frameNStart = frameN  # exact frame index
        key_resp_17.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_17.status == STARTED:
        theseKeys = event.getKeys(keyList=['7'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_17.keys = theseKeys[-1]  # just the last key pressed
            key_resp_17.rt = key_resp_17.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b7Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b7"-------
for thisComponent in Start_b7Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_17.keys in ['', [], None]:  # No response was made
    key_resp_17.keys=None
thisExp.addData('key_resp_17.keys',key_resp_17.keys)
if key_resp_17.keys != None:  # we had a response
    thisExp.addData('key_resp_17.rt', key_resp_17.rt)
thisExp.nextEntry()
# the Routine "Start_b7" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_7 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_07.xlsx'),
    seed=None, name='trials_7')
thisExp.addLoop(trials_7)  # add the loop to the experiment
thisTrial_7 = trials_7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
if thisTrial_7 != None:
    for paramName in thisTrial_7:
        exec('{} = thisTrial_7[paramName]'.format(paramName))

start_bloc = True
for thisTrial_7 in trials_7:
    currentLoop = trials_7
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_7.rgb)
    if thisTrial_7 != None:
        for paramName in thisTrial_7:
            exec('{} = thisTrial_7[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    if start_bloc == True:
        win.callOnFlip(send_data, port, MEG_SETTINGS['bloc_start'])
        start_bloc = False
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_7 (TrialHandler)
    trials_7.addData('n_objets.response', n_objets.getRating())
    trials_7.addData('n_objets.rt', n_objets.getRT())
    trials_7.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_7.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_7.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_7'


# ------Prepare to start Routine "Start_b8"-------
t = 0
Start_b8Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_18 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b8Components = [text_13, key_resp_18]
for thisComponent in Start_b8Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b8"-------
while continueRoutine:
    # get current time
    t = Start_b8Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_13* updates
    if t >= 0.0 and text_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_13.tStart = t
        text_13.frameNStart = frameN  # exact frame index
        text_13.setAutoDraw(True)

    # *key_resp_18* updates
    if t >= 0.0 and key_resp_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_18.tStart = t
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_18.status == STARTED:
        theseKeys = event.getKeys(keyList=['7'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_18.keys = theseKeys[-1]  # just the last key pressed
            key_resp_18.rt = key_resp_18.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b8Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b8"-------
for thisComponent in Start_b8Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_18.keys in ['', [], None]:  # No response was made
    key_resp_18.keys=None
thisExp.addData('key_resp_18.keys',key_resp_18.keys)
if key_resp_18.keys != None:  # we had a response
    thisExp.addData('key_resp_18.rt', key_resp_18.rt)
thisExp.nextEntry()
# the Routine "Start_b8" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_8 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_08.xlsx'),
    seed=None, name='trials_8')
thisExp.addLoop(trials_8)  # add the loop to the experiment
thisTrial_8 = trials_8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
if thisTrial_8 != None:
    for paramName in thisTrial_8:
        exec('{} = thisTrial_8[paramName]'.format(paramName))

for thisTrial_8 in trials_8:
    currentLoop = trials_8
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_8.rgb)
    if thisTrial_8 != None:
        for paramName in thisTrial_8:
            exec('{} = thisTrial_8[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_8 (TrialHandler)
    trials_8.addData('n_objets.response', n_objets.getRating())
    trials_8.addData('n_objets.rt', n_objets.getRT())
    trials_8.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_8.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_8.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_8'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)

    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_b9"-------
t = 0
Start_b9Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_19 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b9Components = [text_14, key_resp_19]
for thisComponent in Start_b9Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b9"-------
while continueRoutine:
    # get current time
    t = Start_b9Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_14* updates
    if t >= 0.0 and text_14.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_14.tStart = t
        text_14.frameNStart = frameN  # exact frame index
        text_14.setAutoDraw(True)

    # *key_resp_19* updates
    if t >= 0.0 and key_resp_19.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_19.tStart = t
        key_resp_19.frameNStart = frameN  # exact frame index
        key_resp_19.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_19.status == STARTED:
        theseKeys = event.getKeys(keyList=['4'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_19.keys = theseKeys[-1]  # just the last key pressed
            key_resp_19.rt = key_resp_19.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b9Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b9"-------
for thisComponent in Start_b9Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_19.keys in ['', [], None]:  # No response was made
    key_resp_19.keys=None
thisExp.addData('key_resp_19.keys',key_resp_19.keys)
if key_resp_19.keys != None:  # we had a response
    thisExp.addData('key_resp_19.rt', key_resp_19.rt)
thisExp.nextEntry()
# the Routine "Start_b9" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_9 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_09.xlsx'),
    seed=None, name='trials_9')
thisExp.addLoop(trials_9)  # add the loop to the experiment
thisTrial_9 = trials_9.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
if thisTrial_9 != None:
    for paramName in thisTrial_9:
        exec('{} = thisTrial_9[paramName]'.format(paramName))

start_bloc = True
for thisTrial_9 in trials_9:
    currentLoop = trials_9
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_9.rgb)
    if thisTrial_9 != None:
        for paramName in thisTrial_9:
            exec('{} = thisTrial_9[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    if start_bloc == True:
        win.callOnFlip(send_data, port, MEG_SETTINGS['bloc_start'])
        start_bloc = False
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_9 (TrialHandler)
    trials_9.addData('n_objets.response', n_objets.getRating())
    trials_9.addData('n_objets.rt', n_objets.getRT())
    trials_9.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_9.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_9.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_9'


# ------Prepare to start Routine "Start_b10"-------
t = 0
Start_b10Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_20 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b10Components = [text_15, key_resp_20]
for thisComponent in Start_b10Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b10"-------
while continueRoutine:
    # get current time
    t = Start_b10Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_15* updates
    if t >= 0.0 and text_15.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_15.tStart = t
        text_15.frameNStart = frameN  # exact frame index
        text_15.setAutoDraw(True)

    # *key_resp_20* updates
    if t >= 0.0 and key_resp_20.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_20.tStart = t
        key_resp_20.frameNStart = frameN  # exact frame index
        key_resp_20.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_20.status == STARTED:
        theseKeys = event.getKeys(keyList=['4'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_20.keys = theseKeys[-1]  # just the last key pressed
            key_resp_20.rt = key_resp_20.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b10Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b10"-------
for thisComponent in Start_b10Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_20.keys in ['', [], None]:  # No response was made
    key_resp_20.keys=None
thisExp.addData('key_resp_20.keys',key_resp_20.keys)
if key_resp_20.keys != None:  # we had a response
    thisExp.addData('key_resp_20.rt', key_resp_20.rt)
thisExp.nextEntry()
# the Routine "Start_b10" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_10 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_10.xlsx'),
    seed=None, name='trials_10')
thisExp.addLoop(trials_10)  # add the loop to the experiment
thisTrial_10 = trials_10.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
if thisTrial_10 != None:
    for paramName in thisTrial_10:
        exec('{} = thisTrial_10[paramName]'.format(paramName))

for thisTrial_10 in trials_10:
    currentLoop = trials_10
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_10.rgb)
    if thisTrial_10 != None:
        for paramName in thisTrial_10:
            exec('{} = thisTrial_10[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_10 (TrialHandler)
    trials_10.addData('n_objets.response', n_objets.getRating())
    trials_10.addData('n_objets.rt', n_objets.getRT())
    trials_10.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_10.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_10.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_10'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)

    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_b11"-------
t = 0
Start_b11Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_21 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b11Components = [text_16, key_resp_21]
for thisComponent in Start_b11Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b11"-------
while continueRoutine:
    # get current time
    t = Start_b11Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_16* updates
    if t >= 0.0 and text_16.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_16.tStart = t
        text_16.frameNStart = frameN  # exact frame index
        text_16.setAutoDraw(True)

    # *key_resp_21* updates
    if t >= 0.0 and key_resp_21.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_21.tStart = t
        key_resp_21.frameNStart = frameN  # exact frame index
        key_resp_21.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_21.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_21.status == STARTED:
        theseKeys = event.getKeys(keyList=['7'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_21.keys = theseKeys[-1]  # just the last key pressed
            key_resp_21.rt = key_resp_21.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b11Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b11"-------
for thisComponent in Start_b11Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_21.keys in ['', [], None]:  # No response was made
    key_resp_21.keys=None
thisExp.addData('key_resp_21.keys',key_resp_21.keys)
if key_resp_21.keys != None:  # we had a response
    thisExp.addData('key_resp_21.rt', key_resp_21.rt)
thisExp.nextEntry()
# the Routine "Start_b11" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_11 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_11.xlsx'),
    seed=None, name='trials_11')
thisExp.addLoop(trials_11)  # add the loop to the experiment
thisTrial_11 = trials_11.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
if thisTrial_11 != None:
    for paramName in thisTrial_11:
        exec('{} = thisTrial_11[paramName]'.format(paramName))

start_bloc = True
for thisTrial_11 in trials_11:
    currentLoop = trials_11
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_11.rgb)
    if thisTrial_11 != None:
        for paramName in thisTrial_11:
            exec('{} = thisTrial_11[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    if start_bloc == True:
        win.callOnFlip(send_data, port, MEG_SETTINGS['bloc_start'])
        start_bloc = False
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_11 (TrialHandler)
    trials_11.addData('n_objets.response', n_objets.getRating())
    trials_11.addData('n_objets.rt', n_objets.getRT())
    trials_11.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_11.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_11.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_11'


# ------Prepare to start Routine "Start_b12"-------
t = 0
Start_b12Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_22 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_b12Components = [text_17, key_resp_22]
for thisComponent in Start_b12Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_b12"-------
while continueRoutine:
    # get current time
    t = Start_b12Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_17* updates
    if t >= 0.0 and text_17.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_17.tStart = t
        text_17.frameNStart = frameN  # exact frame index
        text_17.setAutoDraw(True)

    # *key_resp_22* updates
    if t >= 0.0 and key_resp_22.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_22.tStart = t
        key_resp_22.frameNStart = frameN  # exact frame index
        key_resp_22.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_22.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_22.status == STARTED:
        theseKeys = event.getKeys(keyList=['7'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_22.keys = theseKeys[-1]  # just the last key pressed
            key_resp_22.rt = key_resp_22.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_b12Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_b12"-------
for thisComponent in Start_b12Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_22.keys in ['', [], None]:  # No response was made
    key_resp_22.keys=None
thisExp.addData('key_resp_22.keys',key_resp_22.keys)
if key_resp_22.keys != None:  # we had a response
    thisExp.addData('key_resp_22.rt', key_resp_22.rt)
thisExp.nextEntry()
# the Routine "Start_b12" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_12 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_12.xlsx'),
    seed=None, name='trials_12')
thisExp.addLoop(trials_12)  # add the loop to the experiment
thisTrial_12 = trials_12.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
if thisTrial_12 != None:
    for paramName in thisTrial_12:
        exec('{} = thisTrial_12[paramName]'.format(paramName))

for thisTrial_12 in trials_12:
    currentLoop = trials_12
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_12.rgb)
    if thisTrial_12 != None:
        for paramName in thisTrial_12:
            exec('{} = thisTrial_12[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_12 (TrialHandler)
    trials_12.addData('n_objets.response', n_objets.getRating())
    trials_12.addData('n_objets.rt', n_objets.getRT())
    trials_12.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_12.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_12.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_12'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)

    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Redondance"-------
t = 0
RedondanceClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
Redondance_question.reset()
# keep track of which components have finished
RedondanceComponents = [Redondance_question]
for thisComponent in RedondanceComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Redondance"-------
while continueRoutine:
    # get current time
    t = RedondanceClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *Redondance_question* updates
    if t >= 0.0 and Redondance_question.status == NOT_STARTED:
        # keep track of start time/frame for later
        Redondance_question.tStart = t
        Redondance_question.frameNStart = frameN  # exact frame index
        Redondance_question.setAutoDraw(True)
    continueRoutine &= Redondance_question.noResponse  # a response ends the trial

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in RedondanceComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Redondance"-------
for thisComponent in RedondanceComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('Redondance_question.response', Redondance_question.getRating())
thisExp.nextEntry()
# the Routine "Redondance" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions_sham"-------
t = 0
Instructions_shamClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_11 = event.BuilderKeyResponse()
# keep track of which components have finished
Instructions_shamComponents = [instructions_sham, key_resp_11]
for thisComponent in Instructions_shamComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions_sham"-------
while continueRoutine:
    # get current time
    t = Instructions_shamClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *instructions_sham* updates
    if t >= 0.0 and instructions_sham.status == NOT_STARTED:
        # keep track of start time/frame for later
        instructions_sham.tStart = t
        instructions_sham.frameNStart = frameN  # exact frame index
        instructions_sham.setAutoDraw(True)

    # *key_resp_11* updates
    if t >= 0.0 and key_resp_11.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_11.tStart = t
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_11.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_11.keys = theseKeys[-1]  # just the last key pressed
            key_resp_11.rt = key_resp_11.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Instructions_shamComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions_sham"-------
for thisComponent in Instructions_shamComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys=None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.nextEntry()
# the Routine "Instructions_sham" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_sham_1 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_13.xlsx'),
    seed=None, name='trials_sham_1')
thisExp.addLoop(trials_sham_1)  # add the loop to the experiment
thisTrials_sham_1 = trials_sham_1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_sham_1.rgb)
if thisTrials_sham_1 != None:
    for paramName in thisTrials_sham_1:
        exec('{} = thisTrials_sham_1[paramName]'.format(paramName))

start_bloc = True
for thisTrials_sham_1 in trials_sham_1:
    currentLoop = trials_sham_1
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_sham_1.rgb)
    if thisTrials_sham_1 != None:
        for paramName in thisTrials_sham_1:
            exec('{} = thisTrials_sham_1[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    if start_bloc == True:
        win.callOnFlip(send_data, port, MEG_SETTINGS['bloc_start_sham'])
        start_bloc = False
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_sham_1 (TrialHandler)
    trials_sham_1.addData('n_objets.response', n_objets.getRating())
    trials_sham_1.addData('n_objets.rt', n_objets.getRT())
    trials_sham_1.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_sham_1.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_sham_1.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_sham_1'


# ------Prepare to start Routine "Start_sham2"-------
t = 0
Start_sham2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_23 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_sham2Components = [text_18, key_resp_23]
for thisComponent in Start_sham2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_sham2"-------
while continueRoutine:
    # get current time
    t = Start_sham2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_18* updates
    if t >= 0.0 and text_18.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_18.tStart = t
        text_18.frameNStart = frameN  # exact frame index
        text_18.setAutoDraw(True)

    # *key_resp_23* updates
    if t >= 0.0 and key_resp_23.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_23.tStart = t
        key_resp_23.frameNStart = frameN  # exact frame index
        key_resp_23.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_23.status == STARTED:
        theseKeys = event.getKeys(keyList=['4'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_23.keys = theseKeys[-1]  # just the last key pressed
            key_resp_23.rt = key_resp_23.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_sham2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_sham2"-------
for thisComponent in Start_sham2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_23.keys in ['', [], None]:  # No response was made
    key_resp_23.keys=None
thisExp.addData('key_resp_23.keys',key_resp_23.keys)
if key_resp_23.keys != None:  # we had a response
    thisExp.addData('key_resp_23.rt', key_resp_23.rt)
thisExp.nextEntry()
# the Routine "Start_sham2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_sham_2 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_14.xlsx'),
    seed=None, name='trials_sham_2')
thisExp.addLoop(trials_sham_2)  # add the loop to the experiment
thisTrials_sham_2 = trials_sham_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_sham_2.rgb)
if thisTrials_sham_2 != None:
    for paramName in thisTrials_sham_2:
        exec('{} = thisTrials_sham_2[paramName]'.format(paramName))

for thisTrials_sham_2 in trials_sham_2:
    currentLoop = trials_sham_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_sham_2.rgb)
    if thisTrials_sham_2 != None:
        for paramName in thisTrials_sham_2:
            exec('{} = thisTrials_sham_2[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_sham_2 (TrialHandler)
    trials_sham_2.addData('n_objets.response', n_objets.getRating())
    trials_sham_2.addData('n_objets.rt', n_objets.getRT())
    trials_sham_2.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_sham_2.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_sham_2.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_sham_2'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)

    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Start_sham3"-------
t = 0
Start_sham3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_24 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_sham3Components = [text_19, key_resp_24]
for thisComponent in Start_sham3Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_sham3"-------
while continueRoutine:
    # get current time
    t = Start_sham3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_19* updates
    if t >= 0.0 and text_19.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_19.tStart = t
        text_19.frameNStart = frameN  # exact frame index
        text_19.setAutoDraw(True)

    # *key_resp_24* updates
    if t >= 0.0 and key_resp_24.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_24.tStart = t
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_24.status == STARTED:
        theseKeys = event.getKeys(keyList=['7'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_24.keys = theseKeys[-1]  # just the last key pressed
            key_resp_24.rt = key_resp_24.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_sham3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_sham3"-------
for thisComponent in Start_sham3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys=None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
thisExp.nextEntry()
# the Routine "Start_sham3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_sham_3 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_15.xlsx'),
    seed=None, name='trials_sham_3')
thisExp.addLoop(trials_sham_3)  # add the loop to the experiment
thisTrials_sham_3 = trials_sham_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_sham_3.rgb)
if thisTrials_sham_3 != None:
    for paramName in thisTrials_sham_3:
        exec('{} = thisTrials_sham_3[paramName]'.format(paramName))

start_bloc = True
for thisTrials_sham_3 in trials_sham_3:
    currentLoop = trials_sham_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_sham_3.rgb)
    if thisTrials_sham_3 != None:
        for paramName in thisTrials_sham_3:
            exec('{} = thisTrials_sham_3[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    if start_bloc == True:
        win.callOnFlip(send_data, port, MEG_SETTINGS['bloc_start_sham'])
        start_bloc = False
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_sham_3 (TrialHandler)
    trials_sham_3.addData('n_objets.response', n_objets.getRating())
    trials_sham_3.addData('n_objets.rt', n_objets.getRT())
    trials_sham_3.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_sham_3.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_sham_3.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_sham_3'


# ------Prepare to start Routine "Start_sham4"-------
t = 0
Start_sham4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_25 = event.BuilderKeyResponse()
# keep track of which components have finished
Start_sham4Components = [text_20, key_resp_25]
for thisComponent in Start_sham4Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Start_sham4"-------
while continueRoutine:
    # get current time
    t = Start_sham4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_20* updates
    if t >= 0.0 and text_20.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_20.tStart = t
        text_20.frameNStart = frameN  # exact frame index
        text_20.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_20.status == STARTED and t >= frameRemains:
        text_20.setAutoDraw(False)

    # *key_resp_25* updates
    if t >= 0.0 and key_resp_25.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_25.tStart = t
        key_resp_25.frameNStart = frameN  # exact frame index
        key_resp_25.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_25.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_25.status == STARTED:
        theseKeys = event.getKeys(keyList=['7'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_25.keys = theseKeys[-1]  # just the last key pressed
            key_resp_25.rt = key_resp_25.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Start_sham4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Start_sham4"-------
for thisComponent in Start_sham4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_25.keys in ['', [], None]:  # No response was made
    key_resp_25.keys=None
thisExp.addData('key_resp_25.keys',key_resp_25.keys)
if key_resp_25.keys != None:  # we had a response
    thisExp.addData('key_resp_25.rt', key_resp_25.rt)
thisExp.nextEntry()
# the Routine "Start_sham4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_sham_4 = data.TrialHandler(nReps=1, method='random',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Images_16.xlsx'),
    seed=None, name='trials_sham_4')
thisExp.addLoop(trials_sham_4)  # add the loop to the experiment
thisTrials_sham_4 = trials_sham_4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrials_sham_4.rgb)
if thisTrials_sham_4 != None:
    for paramName in thisTrials_sham_4:
        exec('{} = thisTrials_sham_4[paramName]'.format(paramName))

for thisTrials_sham_4 in trials_sham_4:
    currentLoop = trials_sham_4
    # abbreviate parameter names if possible (e.g. rgb = thisTrials_sham_4.rgb)
    if thisTrials_sham_4 != None:
        for paramName in thisTrials_sham_4:
            exec('{} = thisTrials_sham_4[paramName]'.format(paramName))

    # ------Prepare to start Routine "trial1"-------
    t = 0
    trial1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(14.500000)
    # update component parameters for each repeat
    image.setImage(ImageFile)
    n_objets.reset()
    reaction_time = event.BuilderKeyResponse()
    # keep track of which components have finished
    trial1Components = [empty_gray, fixation_cross, image, n_objets, reaction_time]
    for thisComponent in trial1Components:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "trial1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trial1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *empty_gray* updates
        if t >= 0.0 and empty_gray.status == NOT_STARTED:
            # keep track of start time/frame for later
            empty_gray.tStart = t
            empty_gray.frameNStart = frameN  # exact frame index
            empty_gray.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if empty_gray.status == STARTED and t >= frameRemains:
            empty_gray.setAutoDraw(False)

        # *fixation_cross* updates
        if t >= 1 and fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation_cross.tStart = t
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['cross'])
        frameRemains = 1 + 1.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation_cross.status == STARTED and t >= frameRemains:
            fixation_cross.setAutoDraw(False)

        # *image* updates
        if t >= 2.5 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t
            image.frameNStart = frameN  # exact frame index
            image.setAutoDraw(True)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_start'])
        frameRemains = 2.5 + 8.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            image.setAutoDraw(False)
            win.callOnFlip(send_data, port, MEG_SETTINGS['im_stop'])
        # *n_objets* updates
        if t >= 10.5 and n_objets.status == NOT_STARTED:
            # keep track of start time/frame for later
            n_objets.tStart = t
            n_objets.frameNStart = frameN  # exact frame index
            n_objets.setAutoDraw(True)
        continueRoutine &= n_objets.noResponse  # a response ends the trial

        # *reaction_time* updates
        if t >= 2.5 and reaction_time.status == NOT_STARTED:
            # keep track of start time/frame for later
            reaction_time.tStart = t
            reaction_time.frameNStart = frameN  # exact frame index
            reaction_time.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(reaction_time.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 2.5 + 8.1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if reaction_time.status == STARTED and t >= frameRemains:
            reaction_time.status = STOPPED
        if reaction_time.status == STARTED:
            theseKeys = event.getKeys(keyList=['4', '7'])
            if theseKeys == ['4'] or theseKeys == ['7']:
                win.callOnFlip(send_data, port, MEG_SETTINGS['resp'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if reaction_time.keys == []:  # then this was the first keypress
                    reaction_time.keys = theseKeys[0]  # just the first key pressed
                    reaction_time.rt = reaction_time.clock.getTime()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store data for trials_sham_4 (TrialHandler)
    trials_sham_4.addData('n_objets.response', n_objets.getRating())
    trials_sham_4.addData('n_objets.rt', n_objets.getRT())
    trials_sham_4.addData('n_objets.history', n_objets.getHistory())
    # check responses
    if reaction_time.keys in ['', [], None]:  # No response was made
        reaction_time.keys=None
    trials_sham_4.addData('reaction_time.keys',reaction_time.keys)
    if reaction_time.keys != None:  # we had a response
        trials_sham_4.addData('reaction_time.rt', reaction_time.rt)
    thisExp.nextEntry()

# completed 1 repeats of 'trials_sham_4'


# ------Prepare to start Routine "Fin_bloc"-------
t = 0
Fin_blocClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_8 = event.BuilderKeyResponse()
# keep track of which components have finished
Fin_blocComponents = [text_7, key_resp_8]
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Fin_bloc"-------
while continueRoutine:
    # get current time
    t = Fin_blocClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_7* updates
    if t >= 0.0 and text_7.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_7.tStart = t
        text_7.frameNStart = frameN  # exact frame index
        text_7.setAutoDraw(True)

    # *key_resp_8* updates
    if t >= 0.0 and key_resp_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_8.tStart = t
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_8.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_8.keys = theseKeys[-1]  # just the last key pressed
            key_resp_8.rt = key_resp_8.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Fin_blocComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Fin_bloc"-------
for thisComponent in Fin_blocComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys=None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.nextEntry()
# the Routine "Fin_bloc" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Resting_state_instructions2"-------
t = 0
Resting_state_instructions2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_13 = event.BuilderKeyResponse()
# keep track of which components have finished
Resting_state_instructions2Components = [resting_instructions_end, key_resp_13]
for thisComponent in Resting_state_instructions2Components:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Resting_state_instructions2"-------
while continueRoutine:
    # get current time
    t = Resting_state_instructions2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *resting_instructions_end* updates
    if t >= 0.0 and resting_instructions_end.status == NOT_STARTED:
        # keep track of start time/frame for later
        resting_instructions_end.tStart = t
        resting_instructions_end.frameNStart = frameN  # exact frame index
        resting_instructions_end.setAutoDraw(True)

    # *key_resp_13* updates
    if t >= 0.0 and key_resp_13.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_13.tStart = t
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_13.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_13.keys = theseKeys[-1]  # just the last key pressed
            key_resp_13.rt = key_resp_13.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Resting_state_instructions2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Resting_state_instructions2"-------
for thisComponent in Resting_state_instructions2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys=None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.nextEntry()
# the Routine "Resting_state_instructions2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Resting_state"-------
t = 0
Resting_stateClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_10 = event.BuilderKeyResponse()
# keep track of which components have finished
Resting_stateComponents = [fix_resting_state, key_resp_10]
for thisComponent in Resting_stateComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Resting_state"-------
while continueRoutine:
    # get current time
    t = Resting_stateClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *fix_resting_state* updates
    if t >= 0.0 and fix_resting_state.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_resting_state.tStart = t
        fix_resting_state.frameNStart = frameN  # exact frame index
        fix_resting_state.setAutoDraw(True)
        win.callOnFlip(send_data, port, MEG_SETTINGS['RS_start'])
    frameRemains = 0.0 + 180- win.monitorFramePeriod * 0.75  # most of one frame period left
    if fix_resting_state.status == STARTED and t >= frameRemains:
        fix_resting_state.setAutoDraw(False)
        win.callOnFlip(send_data, port, MEG_SETTINGS['RS_stop'])

    # *key_resp_10* updates
    if t >= 0.0 and key_resp_10.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_10.tStart = t
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_10.status == STARTED:
        theseKeys = event.getKeys(keyList=['q'])

        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_10.keys = theseKeys[-1]  # just the last key pressed
            key_resp_10.rt = key_resp_10.clock.getTime()
            # a response ends the routine
            continueRoutine = False

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Resting_stateComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Resting_state"-------
for thisComponent in Resting_stateComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys=None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.nextEntry()
# the Routine "Resting_state" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Sham"-------
t = 0
ShamClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
rating_sham.reset()
# keep track of which components have finished
ShamComponents = [rating_sham]
for thisComponent in ShamComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Sham"-------
while continueRoutine:
    # get current time
    t = ShamClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    # *rating_sham* updates
    if t >= 0.0 and rating_sham.status == NOT_STARTED:
        # keep track of start time/frame for later
        rating_sham.tStart = t
        rating_sham.frameNStart = frameN  # exact frame index
        rating_sham.setAutoDraw(True)
    continueRoutine &= rating_sham.noResponse  # a response ends the trial

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ShamComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Sham"-------
for thisComponent in ShamComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# store data for thisExp (ExperimentHandler)
thisExp.addData('rating_sham.response', rating_sham.getRating())
thisExp.addData('rating_sham.rt', rating_sham.getRT())
thisExp.nextEntry()
# the Routine "Sham" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Finito"-------
t = 0
FinitoClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
FinitoComponents = [text_5]
for thisComponent in FinitoComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Finito"-------
while continueRoutine:
    # get current time
    t = FinitoClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in FinitoComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Finito"-------
for thisComponent in FinitoComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Finito" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
