// Function to flash rows with SLA Breached as "Yes"
function flashSLARows() {
    const rows = document.querySelectorAll('tbody tr');

    rows.forEach((row) => {
        const slaBreachedCell = row.querySelector('td:nth-child(3)'); // 3 is the index of the SLA Breached column

        if (slaBreachedCell.textContent.trim() === 'Yes') {
            row.style.backgroundColor = 'red';
            setTimeout(() => {
                row.style.backgroundColor = ''; // Reset to the default background color
            }, 1000); // Flash for 1 second (adjust as needed)
        }
    });
}

// Call the flashSLARows function when the document is ready
document.addEventListener('DOMContentLoaded', function () {
    flashSLARows();
});
