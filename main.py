from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from match_game import MatchGame
from data_cleanser import DataCleanser
from snipe import SnipeUpcoming
import math

app = Flask(__name__)

match_game = MatchGame()
data_cleanser = DataCleanser()
snipe_upcoming = SnipeUpcoming()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    console = request.form["console"]
    game = request.form["game"]
    game = data_cleanser.remove_punctuation(game)
    matched_titles = match_game.match_game(console, game)
    if len(matched_titles) > 0:
        if len(matched_titles) == 1:
            rows = match_game.select_from_db(console,matched_titles[0])
            rows.reverse()
            if len(rows) >= 15:
                mean_average = round(sum([row[5] for row in rows[:15]])/15,2)
                sorted_prices = sorted([row[5] for row in rows[:15]])
                median_average = round(sorted_prices[6], 2)
            elif len(rows) > 0:
                mean_average = round(sum([row[5] for row in rows]) / len(rows),2)
                sorted_prices = sorted([row[5] for row in rows])
                median_average = round(sorted_prices[math.floor(len(rows) / 2)])
            else:
                return render_template("error.html")
            return render_template("results.html", game=game, console=console, rows=rows, len_rows=len(rows), mean_average=mean_average, median_average=median_average)
        else:
            return render_template("multiple.html", matches=matched_titles, console=console)
    else:
        return render_template("error.html")

@app.route("/select", methods=["GET", "POST"])
def select():
    game = request.form["game"]
    console = request.form["console"]
    rows = match_game.select_from_db(console, game)
    rows.reverse()
    if len(rows) > 0:
        if len(rows) >= 15:
            mean_average = round(sum([row[5] for row in rows[:15]]) / 15, 2)
            sorted_prices = sorted([row[5] for row in rows[:15]])
            median_average = sorted_prices[6]
        else:
            mean_average = round(sum([row[5] for row in rows]) / len(rows), 2)
            sorted_prices = sorted([row[5] for row in rows])
            median_average = sorted_prices[math.floor(len(rows) / 2)]
        return render_template("results.html", game=game, console=console, rows=rows, len_rows=len(rows), mean_average=mean_average, median_average=median_average)
    else:
        return render_template("error.html")

@app.route("/stats")
def stats():
    last_14_days = {
        "gamecube":match_game.load_last_14_days("gamecube"),
        "ps2":match_game.load_last_14_days("ps2"),
        "ps3":match_game.load_last_14_days("ps3"),
        "ps4":match_game.load_last_14_days("ps4"),
        "xbox_360":match_game.load_last_14_days("xbox_360"),
        "xbox_one":match_game.load_last_14_days("xbox_one")
    }
    #print(last_14_days)
    most_common = {
        "gamecube": match_game.most_commonly_sold(last_14_days["gamecube"]),
        "ps2": match_game.most_commonly_sold(last_14_days["ps2"]),
        "ps3": match_game.most_commonly_sold(last_14_days["ps3"]),
        "ps4": match_game.most_commonly_sold(last_14_days["ps4"]),
        "xbox_360": match_game.most_commonly_sold(last_14_days["xbox_360"]),
        "xbox_one": match_game.most_commonly_sold(last_14_days["xbox_one"])
    }
    highest_value = {
        "gamecube": match_game.highest_value(last_14_days["gamecube"]),
        "ps2": match_game.highest_value(last_14_days["ps2"]),
        "ps3": match_game.highest_value(last_14_days["ps3"]),
        "ps4": match_game.highest_value(last_14_days["ps4"]),
        "xbox_360": match_game.highest_value(last_14_days["xbox_360"]),
        "xbox_one": match_game.highest_value(last_14_days["xbox_one"])
    }
    print(highest_value['gamecube'])
    print(highest_value['ps2'])
    consoles = ["gamecube", "ps2", "ps3", "ps4", "xbox_360", "xbox_one"]
    return render_template("stats.html", most_common=most_common, consoles=consoles, highest_value=highest_value)

@app.route('/search_top/<console>/<game>', methods=['GET'])
def search_top(console, game):
    rows = match_game.select_from_db(console, game)
    rows.reverse()
    if len(rows) >= 15:
        mean_average = round(sum([row[5] for row in rows[:15]]) / 15, 2)
        sorted_prices = sorted([row[5] for row in rows[:15]])
        median_average = sorted_prices[6]
    else:
        mean_average = round(sum([row[5] for row in rows]) / len(rows), 2)
        sorted_prices = sorted([row[5] for row in rows])
        median_average = sorted_prices[math.floor(len(rows) / 2) - 1]
    return render_template("results.html", game=game, console=console, rows=rows,
                           len_rows=len(rows), mean_average=mean_average, median_average=median_average)

@app.route('/params')
def enter_params():
    return render_template('params.html')

@app.route('/snipe', methods=['GET', 'POST'])
def snipe_upcoming_auctions():
    time = request.form['time']
    # if 'other' box ticked, take value from text input
    if time == "":
        time = request.form['time-other']
    # catch instances where user clicks 'other' but does not enter a value
    try:
        time = int(time)
    except ValueError:
        return render_template('params.html')
    # differential will be used to multiply current price e.g. 10% means price x 1.1
    differential = request.form['differential']
    # if 'other' box ticked, take value from text input
    if differential == "":
        differential = request.form['diff-other']
    # catch instances where user clicks 'other' but does not enter a value
    try:
        differential = float(differential) / 100
    except ValueError:
        return render_template('params.html')
    # capture 'more options'
    min_results = int(request.form['number-results'])
    average_compare = request.form['average-compare']
    # retrieve list of auctions ending soon
    game_list = snipe_upcoming.find_upcoming(time)
    # add the average sale price to each item, require results > min_results
    game_list = [snipe_upcoming.find_average(game) for game in game_list]
    game_list = [game for game in game_list if game['num_results'] >= min_results]
    # find games where the mean or median sale price is below current bid
    game_list = [game for game in game_list if snipe_upcoming.current_below_average(game, differential, average_compare)]
    return render_template("snipe.html", games=game_list, num_results=len(game_list))

if __name__ == "__main__":
    app.run(debug=True)