from flask import Flask
from flask import render_template, request, url_for, redirect, jsonify
from random import choice

app = Flask(__name__)


class Bulb:
    def __init__(self):
        self.light_on = self.get_state()

    @staticmethod
    def get_state():
        # system("gpioctl get 19")
        return choice([True, False])

    def toggle_state(self):
        if self.light_on:
            # system("gpioctl dirout-low 19")
            self.light_on = False
        else:
            # system("gpioctl dirout-high 19")
            self.light_on = True

bulb = Bulb()

@app.route('/')
def home():
    return render_template('page.html')


@app.route('/toggle', methods=["GET"])
def toggle():
    bulb.toggle_state()
    return jsonify({"state": bulb.light_on
                    })


@app.route('/check', methods=["GET"])
def check():
    return jsonify({"state": bulb.light_on
                    })

app.run(host='0.0.0.0')
