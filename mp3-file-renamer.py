import id3reader
import os

def renameMp3( src ):
  id3r = id3reader.Reader(src)
  filename = id3r.getValue('performer') + ' - ' + id3r.getValue('title') + ' - ' + id3r.getValue('album') + '.mp3'
  dest = dir + filename
  print 'Rename ' + src + ' to ' + dest
  os.rename(src, dest)

dir = '/home/tomswiggers/projects/mp3-file-renamer/mp3/'

files = os.listdir(dir)

for src in files:
  renameMp3(dir + src)
