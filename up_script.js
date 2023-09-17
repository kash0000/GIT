// script.js

// Function to make rows with 'SLA Breached' column as 'Yes' flash red
function flashSLAStatus() {
    const rows = document.querySelectorAll('tbody tr');
    rows.forEach((row) => {
        const slaBreachedCell = row.querySelector('td:nth-child(3)'); // Assuming 'SLA Breached' is the third column (index 2)
        if (slaBreachedCell.textContent.trim() === 'Yes') {
            // Add the 'flash-red' class to the row
            row.classList.add('flash-red');
        }
    });
}

// Call the function on page load
window.addEventListener('load', flashSLAStatus);
