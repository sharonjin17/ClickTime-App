from flask import Flask, render_template
import requests

shells = []
baseLayers = []
mixins = []
seasonings = []
condiments = []

shell_arr = requests.get("https://tacos-ocecwkpxeq.now.sh/shells").json()
baseLayer_arr = requests.get("https://tacos-ocecwkpxeq.now.sh/baseLayers").json()
mixin_arr = requests.get("https://tacos-ocecwkpxeq.now.sh/mixIns").json()
condiment_arr = requests.get("https://tacos-ocecwkpxeq.now.sh/condiments").json()
seasoning_arr = requests.get("https://tacos-ocecwkpxeq.now.sh/seasonings").json()

for shell_dict in shell_arr:
    shells.append(shell_dict.get("name"))

for baseLayer_dict in baseLayer_arr:
    baseLayers.append(baseLayer_dict.get("name"))
            
for mixin_dict in mixin_arr:
    mixins.append(mixin_dict.get("name"))

for seasoning_dict in seasoning_arr:
    seasonings.append(seasoning_dict.get("name"))
            
for condiment_dict in condiment_arr:
    condiments.append(condiment_dict.get("name"))
            
app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', shells = shells, baseLayers = baseLayers, mixins = mixins, condiments = condiments, seasonings = seasonings, tacos = [])

if __name__ == '__main__':
    app.run()
