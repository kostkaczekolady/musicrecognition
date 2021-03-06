from os import listdir
from os.path import isfile, join
from pydub import AudioSegment

mypath = '../dataset-1-instrument/'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

audio_segments = []
for f in onlyfiles:
    audio_segments.append((f, AudioSegment.from_file(mypath + f)))

audio_segments_ovelayed = []
for as_idx, (file_name, audio_segment) in enumerate(audio_segments):
    for i in range(as_idx, len(audio_segments)):
        if file_name[:-7] == audio_segments[i][0][:-7]:
            continue
        audio_segments_ovelayed.append((
            file_name[:-4] + '_' + audio_segments[i][0][:-4],
            audio_segment.overlay(audio_segments[i][1])
        ))
# audio_segments_ovelayed jest krotką, pierwsza wartość to nazwa połączonych plików a druga to objekt AudioSegment overlayowany

for (file_name, audio_segment) in audio_segments_ovelayed:
    # print("wyeksportowane pliki do bazy:", file_name)
    file_path = "../dataset-2-c-cl-g/"
    audio_segment.export(file_path + file_name + '.mp3', format='mp3')

print("Mix wykonany")
