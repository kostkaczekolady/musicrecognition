from pydub import AudioSegment
from os import listdir
from os.path import isfile, join

path = '../dataset-2-c-cl-g/'
solo = '../trumpet.mp3'
# solo = 'viola_08.mp3'

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

audio_segments = []
for f in onlyfiles:
    audio_segments.append(f)

solo_segment = AudioSegment.from_file(solo)

file_path = "./dataset-3-c-cl-g-t/"
for file_name in audio_segments:
    audio_segment = AudioSegment.from_file(path + file_name)
    new_name = file_name[:-4] + '_' + solo[:-4]
    audiosegment_overlay = audio_segment.overlay(solo_segment)
    audiosegment_overlay.export(file_path + new_name + '.mp3', format='mp3')
    # print("wyeksportowane pliki do bazy:", new_name)

print("Mix wykonany")
