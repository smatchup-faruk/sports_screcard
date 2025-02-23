from flask import Flask, render_template
from config import Config
from models import db, Score
from forms import ScoreForm

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ScoreForm()
    if form.validate_on_submit():
        score = Score(team=form.team.data, score=form.score.data)
        db.session.add(score)
        db.session.commit()
    scores = Score.query.all()
    return render_template('index.html', form=form, scores=scores)

if __name__ == '__main__':
    app.run(debug=True)