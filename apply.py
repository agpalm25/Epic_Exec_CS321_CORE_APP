from flask import Blueprint, render_template, request, flash, redirect, url_for
from models import db, Applicant

apply = Blueprint('apply', __name__)


@apply.route("/application", methods=['GET', 'POST'])
def submit_application():

    if request.method == 'POST':

        student_id = request.form.get('student_id')

        existing_applicant = Applicant.query.filter_by(
            student_id=student_id).first()
        if existing_applicant:

            # if the applicant already applied...
            print("that's not gonna work")

        email = request.form.get('email')

        last_name = request.form.get('last_name')
        first_name = request.form.get('first_name')
        preferred_name = request.form.get('preferred_name')
        pronouns = request.form.get('pronouns')
        phone_number = request.form.get('phone_number')

        cur_residence = request.form.get('cur_residence')
        cur_room_number = request.form.get('cur_room_number')
        cur_position = request.form.get('cur_position')
        study_abroad = request.form.get('study_abroad')
        prev_leadership = request.form.get('prev_leadership')

        major_1 = request.form.get('major_1')
        major_2 = request.form.get('major_2')
        minor_1 = request.form.get('minor_1')
        minor_2 = request.form.get('minor_2')
        gpa = request.form.get('gpa')

        next_year_standing = request.form.get('next_year_standing')
        anticipated_month_year_grad = request.form.get(
            'anticipated_month_year_grad')
        time_commitments = request.form.get('time_commitments')

        text_response_1 = request.form.get('text_response_1')
        add_info = request.form.get('add_info')

        # insert something here for a resume !

        healthy_housing_interest = request.form.get('healthy_housing_interest')
        substance_housing_interest = request.form.get(
            'substance_housing_interest')
        intercultural_housing_interest = request.form.get(
            'intercultural_housing_interest')
        staff_interest_1 = request.form.get('staff_interest_1')
        staff_interest_2 = request.form.get('staff_interest_2')
        pop_interest = request.form.get('pop_interest')

        new_application = Applicant(student_id=student_id)
        # , email=email, last_name=last_name, first_name=first_name, preferred_name=preferred_name, pronouns=pronouns, phone_number=phone_number, cur_residence=cur_residence, cur_room_number=cur_room_number, cur_position=cur_position, study_abroad=study_abroad, prev_leadership=prev_leadership, major_1=major_1, major_2=major_2, minor_1=minor_1, minor_2=minor_2, gpa=gpa, next_year_standing=next_year_standing,
        #                             anticipated_month_year_grad=anticipated_month_year_grad, time_commitments=time_commitments, text_response_1=text_response_1, add_info=add_info, healthy_housing_interest=healthy_housing_interest, substance_housing_interest=substance_housing_interest, intercultural_housing_interest=intercultural_housing_interest, staff_interest_1=staff_interest_1, staff_interest_2=staff_interest_2, pop_interest=pop_interest, signature=signature)

        db.session.add(new_application)
        db.commit()

        return render_template("home.html")

    return render_template("application.html")
