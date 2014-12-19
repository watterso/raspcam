from flask import Flask, request, session, g, redirect, url_for, \
		     abort, render_template, flash

MEDIA_DIR = '../media'

app = Flask(__name__)
app.config.from_object(__name__)
app.debug=True

@app.route('/')
def show_videos():
  return render_template('show_videos.html', videos=[])

if __name__ == '__main__':
    app.run()
