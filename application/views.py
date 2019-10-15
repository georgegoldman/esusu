from flask import Blueprint, render_template, request
from application.web_forms import RegistrationForm, LoginForm, AdminForm, GroupForm, AdduserForm, ChangeAdminForm
from flask_login import login_required, current_user
from .models import Group, Member, User
import datetime
from datetime import date
from application import db
from sqlalchemy.sql import text
from sqlalchemy import create_engine

view = Blueprint('view', __name__)

engine = create_engine('postgresql://postgres:password@localhost/esusu', convert_unicode=True)
connection  = engine.connect()

@view.route('/')
@view.route('/home')
def home():
    return render_template('home.html', title='esusu-home')


@view.route('/signup')
def signup():

    form = RegistrationForm()

    return render_template('signup.html', form=form, title='esusu-signup')


@view.route('/login')
def login():
    form = LoginForm()

    return render_template('login.html', form=form, title='esusu-login')

@view.route('/account_home')
@login_required
def account_home():


    return render_template('account_home.html', username=current_user.username)

@view.route('/admin_signup')
@login_required
def admin_signup():

    form = AdminForm()
    return render_template('admin-signup.html', form=form,)

@view.route('/group_creation')
@login_required
def group_creation():

    form = GroupForm()

    return render_template('create-group-page.html', form=form)

@view.route('/group')
@login_required
def group():


    # members = connection.execute(
    #     text(f"select * from public.user left join public.member on public.user.id = public.member.group_id where public.user.id = {current_user.id} ")
    # )

    members = Member.query.all()

    # members = Member.query.all()
    groups = connection.execute(
        text(f"select * from public.group")
    )

    # def desolve_table(y):
    #     for current_user.id  in y:
    #         return True



    # for group in groups:
    return render_template('group.html', members=members, groups=groups)


    # print(len(members))
    # return 'hi'


@view.route('/member')
@login_required
def add_member():

    group_id  = request.args.get('user_id')

    member_details = connection.execute(
        text(f'select * from public.user inner join public.member on public.member.user_id = public.user.id where public.member.group_id = {group_id}')
    )

    return render_template('member-detail.html', member = member_details)


@view.route('/group_details')
@login_required
def group_details():

    group_id = request.args.get('group_id')


    datas = connection.execute(
        text(f" select * from public.user inner join public.member on public.member.user_id = public.user.id full join public.group on public.group.id = public.member.group_id where public.group.id = {group_id}")
    )

    return render_template('group-details.html', datas=datas)



@view.route('/change_admin')
@login_required
def change_admin():

    group_id = request.args.get('group_id')

    form = ChangeAdminForm()

    return render_template('change-admin.html', form=form, group_id=group_id)
