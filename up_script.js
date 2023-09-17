document.addEventListener("DOMContentLoaded", function () {
  // Get all the table rows
  const rows = document.querySelectorAll("tbody tr");

  // Iterate through the rows
  rows.forEach(function (row) {
    // Get the value of the "SLA Breached" column in the current row
    const slaBreachedValue = row.querySelector("td:last-child").textContent.trim();

    // Check if "SLA Breached" is set to "No"
    if (slaBreachedValue === "No") {
      // Add a CSS class to flash the row green
      flashGreen(row);
    }
  });

  // Function to add and remove the CSS class for flashing
  function flashGreen(element) {
    element.classList.add("flash-green");
    setTimeout(function () {
      element.classList.remove("flash-green");
    }, 1000); // Flash for 1 second (adjust as needed)
  }
});
