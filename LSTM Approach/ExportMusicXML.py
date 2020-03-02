from music21 import articulations, note, musicxml, stream
n1 = note.Note('D#4')
n1.articulations.append(articulations.Fingering(4))
sc = stream.Score()
sc.append(n1)
GEX = musicxml.m21ToXml.GeneralObjectExporter()
m = GEX.fromScore(sc)
with open('test.xml', 'wb') as xml:
    xml.write(GEX.parse(m))