from enum import Enum
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'tagset.txt')

tagFile = open(filename, 'r')
tags = tagFile.readline()
tags_list = tags.split()

tagSetEnum = Enum('tagSetEnum', tags)
