import random, requests, glob, os
from flask import Flask, render_template, request
from threading import Thread
from discord_webhook import DiscordWebhook


def get(url):
  global imgURL
  imgURL = url

def delt():
  files = glob.glob('static/images/*')
  for f in files:
    os.remove(f)

def webSend(msg, filename):
  size = round(os.stat(f'static/images/{filename}').st_size/1000000, 1)
  if size < 8.1:
    url = os.getenv("webhk")
    webhook = DiscordWebhook(url=url, username="DDrive", content=msg)
    with open(f"static/images/{filename}", "rb") as f:
      webhook.add_file(file=f.read(), filename=filename)
    webhook.execute()
    return True, size
  else:
    return False, size


app = Flask('DDrive')

@app.route('/', methods=["GET", "POST"])
def home():
  if request.method == "POST":
    try:
      file = request.files['img']
      file.save(f"static/images/{file.filename}")
      tf, size = webSend(file.filename, file.filename)
      if tf:
        delt()
        return render_template("home.html", r=imgURL, t=file.filename, size=size, c="true")
      else:
        delt()
        return render_template("home.html", c="false")
    except Exception as e:
      return f"Something went wrong while uploading, try again!<br>{e}"
  else:
	  return render_template("home.html", c="false")

    
def run():
  app.run(
		host='0.0.0.0',
		port=2566
	)

def keep_alive():
	t = Thread(target=run)
	t.start()
