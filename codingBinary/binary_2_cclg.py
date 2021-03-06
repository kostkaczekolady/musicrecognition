from os import listdir
from os.path import isfile, join
from pydub import AudioSegment
import re

mypath = './dataset-2-c-cl-g/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print("onlyfiles: ", len(onlyfiles))


data = []
for f in onlyfiles:
    trimmed_name = re.sub("_\d+.mp3", "", re.sub("_\d+_", "+", f))
    if trimmed_name == 'clarinet':
        data.append([1,0,0])
    elif trimmed_name == 'cello':
        data.append([0, 1, 0])
    elif trimmed_name == 'guitar':
        data.append([0, 0, 1])
    elif trimmed_name == 'cello+clarinet':
        data.append([1,1,0])
    elif trimmed_name == 'cello+guitar':
        data.append([1,0,1])
    elif trimmed_name == 'clarinet+guitar':
        data.append([0,1,1])
    else:
        data.append([0,0,0])
        print("Nierozpoznany instr: ", trimmed_name)

print("Elementy zakodowane!")