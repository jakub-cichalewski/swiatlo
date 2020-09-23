from flask import Flask
from flask import render_template, request, url_for, redirect, jsonify
from os import system, popen

LIGHT_GPIO = 19
ERROR_GPIO = 18

system(f"gpioctl dirout-low {ERROR_GPIO}")

# call on exit
def abort():
    system(f"gpioctl dirout-high {ERROR_GPIO}")
    exit(1)


class Bulb:
    def __init__(self):
        self.light_on = self.get_state()

    def get_state(self):
        with popen(f"gpioctl get {LIGHT_GPIO}") as pipe:
            output = pipe.read()

        if "HIGH" in output:
            self.light_on = True
        elif "LOW" in output:
            self.light_on = False
        else:
            abort()
        return self.light_on

    def on(self):
        system(f"gpioctl dirout-high {LIGHT_GPIO}")
        self.light_on = True

    def off(self):
        system(f"gpioctl dirout-low {LIGHT_GPIO}")
        self.light_on = False

    def toggle_state(self):
        if self.light_on:
            self.off()
        else:
            self.on()


bulb = Bulb()
app = Flask(__name__)

print(bulb.light_on)

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


if __name__ == "__main__":
    try:
        app.run(host='0.0.0.0')
    except:
        abort()
