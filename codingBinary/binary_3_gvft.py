from os import listdir
from os.path import isfile, join
from pydub import AudioSegment
import re

mypath = './dataset-3-g-v-f-t/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print("onlyfiles: ", len(onlyfiles))

data = []
nierozpoznany_instr = 0
for f in onlyfiles:
    trimmed_name = re.sub(".mp3", "", re.sub("_\d+.mp3", "", re.sub("_\d+_", "+", f)))
    if trimmed_name == 'guitar':
        data.append([1,0,0,0])
    elif trimmed_name == 'flute':
        data.append([0,1,0,])
    elif trimmed_name == 'trumpet':
        data.append([0,0,1,0])
    elif trimmed_name == 'viola':
        data.append([0,0,0,1])
    if trimmed_name == 'flute+guitar+trumpet':
        data.append([1,1,1,0])
    elif trimmed_name == 'flute+viola+trumpet':
        data.append([1,0,1,1])
    elif trimmed_name == 'guitar+viola+trumpet':
        data.append([0,1,0,1])
    else:
        data.append([0,0,0,0])
        print("Nierozpoznany instr: ", trimmed_name)

print("Elementy zakodowane!")
