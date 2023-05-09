from bottle import Bottle, route, run, template, static_file

app = Bottle()

@app.route('/')
def index():
    return template('templates/index.tpl')

@app.route('/squad')
def squad():
    players = ['Big Gabi', 'other Gabi', 'Little Gabi']
    return template('templates/squad.tpl', players=players)

@app.route('/news')
def news():
    headlines = ['Arsenal bottletop bill and his best friend corky the league', 
                 'Shakeup at Arsenal as Arteta deletes Holdinho', 
                 'Arsenal announce new sponsorship deal with Belle Delphine']
    return template('templates/news.tpl', headlines=headlines)

if __name__ == '__main__':
    run(app, host='localhost', port=3000, debug=True)