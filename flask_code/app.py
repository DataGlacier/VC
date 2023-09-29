import dataclasses
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    Data = [
        ("NEW YORK NY", 8405837, 302149),
        ("CHICAGO IL", 1955130, 164468),
        ("LOS ANGELES CA", 1595037, 144132),
        ("MIAMI FL", 1339155, 17675),
        ("SILICON VALLEY", 1177609, 27247),
        ("ORANGE COUNTY", 1030185, 12994),
        ("SAN DIEGO CA", 959307, 69995),
        ("PHOENIX AZ", 943999, 6133),
        ("DALLAS TX", 942908, 22157),
        ("ATLANTA GA", 814885, 24701),
        ("DENVER CO", 754233, 12421),
        ("AUSTIN TX", 698371, 14978),
        ("SEATTLE WA", 671238, 25063),
        ("TUCSON AZ", 631442, 5712),
        ("SAN FRANCISCO CA", 629591, 213609),
        ("SACRAMENTO CA", 545776, 7044),
        ("PITTSBURGH PA", 542085, 3643),
        ("WASHINGTON DC", 418859, 127001),
        ("NASHVILLE TN", 327225, 9270),
        ("BOSTON MA", 248968, 80021),
    ]

    labels = [row[0] for row in Data]
    values1 = [row[1] for row in Data]
    values2 = [row[2] for row in Data]

    return render_template("index.html", labels=labels, values1=values1, values2=values2)

