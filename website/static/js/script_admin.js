// links to sections
const applicationLink = document.getElementById('applicationLink');
const appointmentLink = document.getElementById('appointmentLink');
const userDataLink = document.getElementById('userDataLink');

// the sections
const applicationForm = document.getElementById('applicationForm');
const appointmentForm = document.getElementById('appointmentForm');
const userDataForm = document.getElementById('userDataForm');

// switching sections 
function showForm(formToShow) {

    [applicationForm, appointmentForm, userDataForm].forEach(form => {
        
        form.classList.remove('active');
    
    });

    formToShow.classList.add('active');
}

// showing the right thing for each link
applicationLink.addEventListener('click', (e) => {
    e.preventDefault();
    showForm(applicationForm);
    applicationLink.classList.add('active');
    appointmentLink.classList.remove('active');
    userDataLink.classList.remove('active');
});

appointmentLink.addEventListener('click', (e) => {
    e.preventDefault();
    showForm(appointmentForm);
    appointmentLink.classList.add('active');
    applicationLink.classList.remove('active');
    userDataLink.classList.remove('active');
});

userDataLink.addEventListener('click', (e) => {
    e.preventDefault();
    showForm(userDataForm);
    userDataLink.classList.add('active');
    applicationLink.classList.remove('active');
    appointmentLink.classList.remove('active');
});

// change available residences...
// TO DO -----------------------------------------------------------------

// changing dates available to schedule appointments...
// get the min and max's

const min_d = "{{ max_d }}";
const max_d = "{{ max_d }}";
const min_t = "{{ min_t }}";
const max_t = "{{ max_t }}";

console.log("current min_d is ", min_d);
console.log("current max_d is ", max_d);
console.log("current min_t is ", min_t);
console.log("current max_t is ", max_t);

// define something to return
const messageElement = document.getElementById("cur_bounds")

function cur_bounds() {

    if (min_d == "{{ min_d }}" || max_t == "{{ max_t }}" ) {
        messageElement.textContent = "The signup window is not fully set up yet >:( . Please configure the dates and times.";

    } else {
        messageElement.textContent = `The current signup window is from ${min_d} to ${max_d}, with appointment times from ${min_t} to ${max_t}.`;
    }

    return messageElement
}

cur_bounds()

// TO DO

// printing all user data (i'll try)...
// TO DO
