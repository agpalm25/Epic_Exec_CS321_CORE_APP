from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required
from .models import Time_Bounds
from website import db

admin_blueprint = Blueprint('admin', __name__)

@admin_blueprint.route("/admin_fun")
@login_required
def admin_fun() :
    
    min_d = Time_Bounds.min_d
    max_d = Time_Bounds.max_d
    min_t = Time_Bounds.min_t
    max_t = Time_Bounds.max_t

    return render_template("admin_fun.html", min_d = min_d, max_d = max_d, min_t = min_t, max_t = max_t)

@admin_blueprint.route("/appointment", methods=['GET', 'POST'])
def appointment() :
    return render_template("appointment.html", bounds=check_for_time)


@admin_blueprint.route("/update_date_bounds", methods=['GET', 'POST'])
def update_date_bounds() :
    return

@admin_blueprint.route("/update_time_bounds", methods = ['GET', 'POST'])
def update_time_bounds() :
    return

def get_the_time() :
    return Time_Bounds.get()

def check_for_time() :

    entries = Time_Bounds.query.count()

    if entries < 1:

        min_d = '2024-09-01'
        max_d = '2024-12-30'
        min_t = '09:00'
        max_t = '17:00'

        bounds = Time_Bounds(min_d=min_d, max_d=max_d, min_t=min_t, max_t=max_t)
        db.session.add(bounds)
        db.session.commit()

    else : 
        bounds = Time_Bounds.query.first()

    return bounds
