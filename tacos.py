from flask import Flask, render_template

shells, baseLayers, mixins, condiments, seasonings = []

shell_arr = requests.get("https://tacos-ocecwkpxeq.now.sh/shells").json()
baseLayer_arr = requests.get("https://tacos-ocecwkpxeq.now.sh/baseLayers").json()
mixin_arr = requests.get("https://tacos-ocecwkpxeq.now.sh/mixIns").json()
condiment_arr = requests.get("https://tacos-ocecwkpxeq.now.sh/baseLayers").json()
seasoning_arr = requests.get("https://tacos-ocecwkpxeq.now.sh/baseLayers").json()

for shell_dict in shell_arr:
    for s in shell_dict:
        if s == "name":
            shells.append(s)

for baseLayer_dict in baseLayer_arr:
    for b in baseLayer_dict:
        if b == "name":
            baseLayers.append(b)
            
for mixin_dict in mixin_arr:
    for m in mixin_dict:
        if m == "name":
            mixins.append(m)

for seasoning_dict in seasoning_arr:
    for sn in seasoning_dict:
        if sn == "name":
            seasonings.append(sn)
            
for condiment_dict in condiment_arr:
    for c in condiment_dict:
        if c == "name":
            condiments.append(c)

print(condiments)
print(mixins)
print(baseLayers)
            
app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/test')
def test(query):
    return '<h1>You are on the test page.</h1>'

if __name__ == '__main__':
    app.run()
