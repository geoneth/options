from flask import Flask, render_template, request, send_file
from global_info import config
from logic.pipeline import run

app = Flask(__name__)


@app.route("/")
def main():
    return render_template(
            "home.html",
            load_data=config.core_info,
            viz_types=config.all_viz_types,
                           )

@app.route("/Calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        data = standardize_flat(request.form.to_dict(flat=False))
        if catch_blank(data):
            return render_template(
                    "calculate.html",
                    load_data=config.core_info,
                    viz_types=config.all_viz_types,
                    saved_values=data,
                    output=None
                    )
        else:
            output = run(**data)
            return render_template(
                "calculate.html",
                load_data=config.core_info,
                viz_types=config.all_viz_types,
                saved_values=data,
                output=output
                )
    else:
        return render_template(
                "calculate.html",
                load_data=config.core_info,
                viz_types=config.all_viz_types,
                saved_values=dict(request.args),
                output=None
                )


def standardize_flat(dictionary):
    temp = {}
    for key, value in dictionary.items():
        if len(value) == 1:
            temp[key] = value[0]
        else:
            temp[key] = value
    return temp

def catch_blank(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, list):
            if "" in value:
                return True
        else:
            if value == "":
                return True
    return False

if __name__ == "__main__":
    app.run()

