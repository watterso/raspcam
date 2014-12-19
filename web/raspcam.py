import os
from time import strftime, strptime

from flask import Flask, request, session, g, redirect, url_for, \
		     abort, render_template, flash

MEDIA_DIR = 'static/frames'
FILE_TIME = '%Y%m%d_%H%M%S.jpg'
DISP_TIME = '%B %d, %Y at %H:%M:%S'

app = Flask(__name__)
app.config.from_object(__name__)
app.debug=True

@app.route('/')
def show_frames():

  paths = [{'file':url_for('static', filename='frames/'+x), 'title':strftime(DISP_TIME, strptime(x,FILE_TIME))} for x in os.listdir(MEDIA_DIR)]
  list.sort(paths, key=lambda pic: pic['file'], reverse=True)
  most_recent = paths.pop(0) if len(paths) > 0 else None
  return render_template('show_frames.html', most_recent=most_recent, frames=paths)

if __name__ == '__main__':
    app.run()
