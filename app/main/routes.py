from flask import render_template, redirect, flash, url_for, request, current_app, \
    g, jsonify
from app import db
from flask_login import logout_user, current_user, login_user, login_required
from app.models import User, Game_info
from werkzeug.urls import url_parse

from app.main import bp
from app.main.forms import InputForm, EditClanForm
from flask_babel import get_locale, _
from app.translate import translate

#base location
@bp.route('/', methods=['GET', 'POST'])

#general/welcome page
@bp.route('/index', methods=['GET', 'POST'])
def index():
    page = request.args.get('page', 1, type=int)

    #paginate with paginate() from SQLAlchemy
    first_user = User.query.get(1)
    games = first_user.all_games().paginate(page, current_app.config['GAMES_PER_PAGE'], False)
    #set next page url IF there are more games
    next_url = url_for('main.index', page = games.next_num) \
        if games.has_next else None
    prev_url = url_for('main.index', page = games.prev_num) \
        if games.has_prev else None

    return render_template('index.html', title=_('Home'), games = games.items,
        next_url = next_url, prev_url = prev_url)

#Data input
@bp.route('/record_new_data', methods=['GET', 'POST'])
@login_required
def record_new_data():
    form = InputForm()
    if form.validate_on_submit():
        #submit all data from form to db
        game = Game_info(class_name = form.class_name.data, eff = int(form.eff.data),
            fireteam = form.fireteam.data, primary = form.primary.data,
            secondary = form.secondary.data, heavy = form.heavy.data,
            map = form.map.data, user = current_user)
        db.session.add(game)
        db.session.commit()
        flash('Data submition successful')
        #once data is submitted the user will be redirected to the home page
        #the home page will not only have been updated to show statistics based
        #on the new data, but also will deter the user from trying to input
        #many games at once and risk incorrect data
        return redirect(url_for('main.index'))
    return render_template('record_new_data.html', title=_('Record New Data'), form=form)

<<<<<<< HEAD
@bp.route('/suggestions', methods=['GET', 'POST'])
@login_required
#this page is intended to, on a per map basis, display to the user their
#current best performing theoretical loadout. this means that primary, secondary,
#heavy, and class will all be considered seperatly in an effort to suggest
#new loadouts
def suggestions():
    all_games = Game_info.query.all()


    mid_games = 0
    #Midtown primaries
    mid_p_hc = 0
    mid_p_ar = 0
    mid_p_pr = 0
    mid_p_sc = 0
    mid_p_bo = 0
    mid_p_sa = 0
    mid_p_sg = 0
    mid_p_sr = 0
    mid_p_gl = 0
    mid_primary = {'hc' : mid_p_hc, 'ar' : mid_p_ar, 'pr' : mid_p_pr,
        'sc' : mid_p_sc, 'bo' : mid_p_bo, 'sa' : mid_p_sa, 'sg' : mid_p_sg,
        'sr' : mid_p_sr, 'gl' : mid_p_gl}
    #Midtown secondaries
    mid_s_hc = 0
    mid_s_ar = 0
    mid_s_pr = 0
    mid_s_sc = 0
    mid_s_bo = 0
    mid_s_sa = 0
    mid_s_sg = 0
    mid_s_sr = 0
    mid_s_gl = 0
    mid_secondary = {'hc' : mid_s_hc, 'ar' : mid_s_ar, 'pr' : mid_s_pr,
        'sc' : mid_s_sc, 'bo' : mid_s_bo, 'sa' : mid_s_sa, 'sg' : mid_s_sg,
        'sr' : mid_s_sr, 'gl' : mid_s_gl, 'fr' : mid_s_fr}
    #Midtown heavies
    mid_heavy = {'lf' : mid_h_lr, 'rl' : mid_h_rl, 'gl' : mid_h_gl,
        'mg' : mid_h_mg}
    mid_class = {}
    mid_ft = False
    for map in all_games:
        #Midtown data suggestions
        if map.map == "mid":
            mid_games+=1
            mid_primary[map.primary]+=1
            mid_secondary[map.secondary]+=1
            mid_heavy[map.heavy]+=1
            mid_class[map.class] = map.class
            mid_ft = map.fireteam

    return render_template('suggestions.html', title=_('Suggestions'),
    mid_games = mid_games, mid_p_hc = mid_primary['hc'])
=======
#displays current best load out
@bp.route('/suggestions', methods=['GET', 'POST'])
@login_required
def suggestions():


    return render_template('suggestions.html', title = _('loadout suggestions'))
>>>>>>> 8e500895ca39618569724bb849c168e7ab6c4f89

#user specific/profile page
@bp.route('/user/<username>')
@login_required
def user(username):
    #test data
    user = User.query.filter_by(username = username).first_or_404()
    games = current_user.games.all()
    return render_template('user.html', user=user, games = games)

#edit clan name on profile/user page
#
#this is done as a seperate form instead of as just another Column in the user
#table soley so that i can learn TextAreaField forms
@bp.route('/edit_clan', methods=['GET', 'POST'])
@login_required
def edit_clan():
    form = EditClanForm()
    if form.validate_on_submit():
        #add clan name to users profile page in db
        current_user.clan_name = form.clan_name.data
        db.session.commit()
        flash('Your changes have been saved')
        return redirect(url_for('user', username=current_user.username))
    #allows for pre-population of form with existing data
    elif request.method == 'GET':
        form.clan_name.data = current_user.clan_name
    return render_template('edit_clan.html', title = _('Edit Clan Name'), form = form)

@bp.route('/translate', methods=['POST'])
@login_required
def translate_text():
    return jsonify({'text': translate(request.form['text'],
                                      request.form['source_language'],
                                      request.form['dest_language'])})
