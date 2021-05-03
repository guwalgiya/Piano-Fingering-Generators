from music21 import articulations, note, musicxml, stream
def generateScoreGivenLists(note_list, finger_list, score_name):
    sc = stream.Score()
    for n, f in zip(note_list, finger_list):
        n_m21 = note.Note(n)
        n_m21.articulations.append(articulations.Fingering(f))
    GEX = musicxml.m21ToXml.GeneralObjectExporter()
    m = GEX.fromScore(sc)
    with open(score_name+'.xml', 'wb') as xml:
        xml.write(GEX.parse(m))