from flask import Blueprint, render_template

# Create a blueprint for routes
main_blueprint = Blueprint('main', __name__)


@main_blueprint.route("/")
def home():
    return render_template("home.html")


@main_blueprint.route("/requirements")
def requirements():
    return render_template("requirements_page.html")


@main_blueprint.route("/appointment")
def appointment():
    return render_template("appointment.html")


@main_blueprint.route("/ca-info")
def ca_info():
    return render_template("ca_info.html")


# @main_blueprint.route("/application")
# def application():
 #   return render_template("application.html")


@main_blueprint.route("/UserHome")
def user_home():
    return render_template("UserHome.html")


@main_blueprint.route("/assessment")
def assessment():
    return render_template("assessment.html")
