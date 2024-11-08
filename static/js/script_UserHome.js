// script.js

// Set the username
const usernameElement = document.getElementById("username");
const username = "Admin"; // Replace this with a dynamic username variable if needed
usernameElement.textContent = username;

// Example function to load table data dynamically
const tableBody = document.querySelector("tbody");

applicants.forEach(applicant => {
    const row = document.createElement("tr");
    row.innerHTML = `
    <td>${applicant.name} ${applicant.last_name}</td>
    <td>${applicant.status || "N/A"}</td>
    <td>${applicant.interview || "N/A"}</td>
    <td>${applicant.application || "N/A"}</td>
    <td>${applicant.assessment || "N/A"}</td>
    `;
    tableBody.appendChild(row);
});
