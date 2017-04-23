# -*- coding: utf-8 -*-
"""Public section, including homepage and signup."""
from flask import Blueprint, flash, redirect, render_template, request, url_for, session
from flask_login import login_required, login_user, logout_user

from myflaskapp.extensions import login_manager
from myflaskapp.public.forms import LoginForm, ToDoListForm
from myflaskapp.user.forms import RegisterForm
from myflaskapp.user.models import User
from myflaskapp.utils import flash_errors

blueprint = Blueprint('public', __name__, static_folder='../static')


@login_manager.user_loader
def load_user(user_id):
    """Load user by ID."""
    return User.get_by_id(int(user_id))


@blueprint.route('/', methods=['GET', 'POST'])
def home():
    """Home page."""
    login_form = LoginForm(request.form, prefix='login')
    # Handle logging in
    if request.method == 'POST':
        if login_form.validate_on_submit():
            login_user(login_form.user)
            flash('You are logged in.', 'success')
            redirect_url = request.args.get('next') or url_for('user.members')
            return redirect(redirect_url)
        else:
            flash_errors(login_form)
    return render_template('public/home.html', form=login_form)


@blueprint.route('/logout/')
@login_required
def logout():
    """Logout."""
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('public.home'))


@blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    """Register new user."""
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        User.create(username=form.username.data, email=form.email.data,
                    password=form.password.data, active=True)
        flash('Thank you for registering. You can now log in.', 'success')
        return redirect(url_for('public.home'))
    else:
        flash_errors(form)
    return render_template('public/register.html', form=form)


@blueprint.route('/about/')
def about():
    """About page."""
    form = LoginForm(request.form)
    return render_template('public/about.html', form=form)


@blueprint.route('/to-do/', methods=['GET', 'POST'])
def to_do():
    """To-Do page."""
    #

    todo_form = ToDoListForm(request.form, prefix='todo')

    searchword = request.args.get('key', '')
    print('searchword',searchword)
    if searchword == 'clear':
        try:
            session['list_items'] = []
            return render_template('todo.html', form=todo_form)
        except:
            pass

    if 'list_items' not in session:
        print("We have no list items")
        session['list_items'] = []
    else:
        pass

    if todo_form.validate_on_submit():
        print("On entry have list items", session['list_items'])
        print("Form data", str(todo_form.item.data))
        session['list_items'].append(str(todo_form.item.data))
        session.modified = True
        print("After append have list items", session['list_items'])
        print("*" * 5)
        return redirect(url_for('.to_do'))




    #print("list_items", session['list_items'])
    return render_template('todo.html', form=todo_form,
                           session=session)
