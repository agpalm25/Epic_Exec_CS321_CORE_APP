import pytest
from website.models import ApplicantInformation, AssessmentForm
from sqlalchemy.exc import IntegrityError
import uuid


@pytest.fixture
def applicant_data():
    """Fixture for creating an ApplicantInformation record."""
    return {
        "student_id": str(uuid.uuid4())[:6], 
        "last_name": "Doe",
        "first_name": "John",
        "pronouns": "he/him",
        "current_hall": "Test Hall",
        "current_room_number": "101",
        "current_email": "john.doe@example.com",
        "current_phone_number": "555-1234",
        "returning_ca_or_new_ca": "New",
        "major_1": "CS",
        "class_year": "2025",
        "cumulative_gpa": 3.8,
        "leadership_experience": ["Team Lead", "Mentor"]
    }


@pytest.fixture
def assessment_data():
    """Fixture for creating an AssessmentForm record."""
    return {
        "evaluator_name": "Jane Smith",
        "q1_response": "Response to Q1",
        "q1_evaluation": 4,
        "q2_response": "Response to Q2",
        "q2_evaluation": 5,
        "q3_response": "Response to Q3",
        "q3_evaluation": 3,
        "q4_response": "Response to Q4",
        "q4_followup": "Follow-up Q4",
        "q4_evaluation": 4,
        "q5_response": "Response to Q5",
        "q5_followup": "Follow-up Q5",
        "q5_evaluation": 5,
        "q6_response": "Response to Q6",
        "q6_followup": "Follow-up Q6",
        "q6_evaluation": 3,
        "study_abroad_plans": "None",
        "can_attend_training": True,
        "candidate_questions": "What are the growth opportunities?",
        "perceived_strengths": "Strong leadership skills.",
        "perceived_growth_areas": "Needs to improve time management.",
        "general_comments": "Strong candidate for the role.",
        "hiring_recommendation": "Strongly Recommend",
        "recommendation_rationale": "Candidate demonstrates excellent potential."
    }


def test_create_assessment(db, session, applicant_data, assessment_data):
    """Test creating an AssessmentForm record."""
    applicant = ApplicantInformation(**applicant_data)
    session.add(applicant)
    session.commit()

    assessment = AssessmentForm(student_id=applicant.student_id, **assessment_data)
    session.add(assessment)
    session.commit()

    assert assessment.id is not None
    assert assessment.student_id == applicant.student_id
    assert assessment.evaluator_name == assessment_data["evaluator_name"]


def test_update_assessment(db, session, applicant_data, assessment_data):
    """Test updating an AssessmentForm record."""
    applicant = ApplicantInformation(**applicant_data)
    session.add(applicant)
    session.commit()

    assessment = AssessmentForm(student_id=applicant.student_id, **assessment_data)
    session.add(assessment)
    session.commit()

    assessment.q1_response = "Updated response to Q1"
    assessment.q1_evaluation = 5
    session.commit()

    updated_assessment = AssessmentForm.query.filter_by(student_id=applicant.student_id).first()
    assert updated_assessment.q1_response == "Updated response to Q1"
    assert updated_assessment.q1_evaluation == 5


def test_delete_assessment(db, session, applicant_data, assessment_data):
    """Test deleting an AssessmentForm record."""
    applicant = ApplicantInformation(**applicant_data)
    session.add(applicant)
    session.commit()

    assessment = AssessmentForm(student_id=applicant.student_id, **assessment_data)
    session.add(assessment)
    session.commit()

    session.delete(assessment)
    session.commit()

    deleted_assessment = AssessmentForm.query.filter_by(student_id=applicant.student_id).first()
    assert deleted_assessment is None


def test_relationship(session, applicant_data, assessment_data):
    """Test the relationship between AssessmentForm and ApplicantInformation."""
    applicant = ApplicantInformation(**applicant_data)
    session.add(applicant)
    session.commit()

    assessment = AssessmentForm(student_id=applicant.student_id, **assessment_data)
    session.add(assessment)
    session.commit()

    fetched_applicant = ApplicantInformation.query.filter_by(student_id=applicant.student_id).first()
    assert fetched_applicant.assessment_form == assessment


def test_create_duplicate_student_id(db, session, applicant_data):
    """Test that creating a duplicate student_id raises an IntegrityError."""
    applicant1 = ApplicantInformation(**applicant_data)
    session.add(applicant1)
    session.commit()

    with pytest.raises(IntegrityError):
        applicant2 = ApplicantInformation(**applicant_data)
        session.add(applicant2)
        session.commit()
