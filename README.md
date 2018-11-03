# theSquatStand
The Squat Stand is a webapp implementing some of the most basic features of the (now-defunct) website thesquatrack.com. It is used to track workout history, with an emphasis on weightlifting and powerlifting training.

It is built using Flask for the back-end, Bootstrap for the front-end, and Bokeh to create the charts.

In addition to keeping workout history, the Squat Stand tracks personal bests on each exercise and generates summary statistics including daily and weekly volume and rep counts.

![Summaries](/images/stats.png)

![Workout History](/images/history.png)

![Workout Entry](/images/entry.png)

## How to run
1. Create and activate a python virtual environment.
```
python3 -m virtualenv venv
source venv/bin/activate
```
2. Install the required packages.
```
pip install -r requirements.txt
```
3. Set the FLASK_APP variable to thesquatstand.py, then start flask.
```
export FLASK_APP=thesquatstand.py
flask run
```
4. Direct your web browser to localhost:5000.

## Future features
* Track additional exercise measurements (e.g. distance, time).
* Display individual exercise history.
* Implement a user system.
* Track and plot additional workout statistics (e.g. intensity).
* Improve the look and feel of the site.
