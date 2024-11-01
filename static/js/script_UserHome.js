// script.js

// Set the username
const usernameElement = document.getElementById("username");
const username = "Christian"; // Replace this with a dynamic username variable if needed
usernameElement.textContent = username;

// Example function to load table data dynamically
const tableBody = document.querySelector("tbody");
const applicants = [
    { name: "Alice Smith", status: "Reviewed", interview: "Scheduled - 2:00 PM", application: "---", assessment: "---" },
    { name: "Bob Johnson", status: "Pending", interview: "Not Scheduled", application: "---", assessment: "---" },
    // Add more applicants as needed
];

applicants.forEach(applicant => {
    const row = document.createElement("tr");
    row.innerHTML = `<td>${applicant.name}</td><td>${applicant.status}</td><td>${applicant.interview}</td><td>${applicant.application}</td><td>${applicant.assessment}</td>`;
    tableBody.appendChild(row);
});
