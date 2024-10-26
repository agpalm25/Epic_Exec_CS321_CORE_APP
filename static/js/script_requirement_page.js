const checkboxes = document.querySelectorAll('input[type="checkbox"]');
const continueBtn = document.querySelector('.continue-btn');
const message = document.querySelector('.message');

checkboxes.forEach(checkbox => {
    checkbox.addEventListener('change', () => {
        if ([...checkboxes].every(cb => cb.checked)) {
            continueBtn.disabled = false;
            message.textContent = "Congratulations!";
        } else {
            continueBtn.disabled = true;
            message.textContent = "I'm sorry..";
        }
    });
});
