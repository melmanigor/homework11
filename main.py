from flask import Flask, render_template

import utils

app = Flask(__name__)


@app.route('/')
def all_candidates():
    items = utils.open_json()
    return render_template('list.html', items=items)


@app.route("/candidate/<int:id>")
def id_candidates(id):
    candidate = utils.get_candidate(id)
    return render_template('single.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def search_candidate(candidate_name):
    candidates,count = utils.get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates=candidates, count=count)


@app.route("/skill/<skill_name>")
def skill_candidates(skill_name):
    candidates, count = utils.get_candidates_by_skill(skill_name)
    return render_template('skill.html', candidates=candidates, skill_name=skill_name, count=count)


app.run(debug=True, port=8000)
