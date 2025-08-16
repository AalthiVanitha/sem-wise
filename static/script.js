window.addEventListener("DOMContentLoaded", function () {
  fetch("/analyze")
    .then((response) => response.json())
    .then((data) => {
      console.log("API Response:", data);

      let resultDiv = document.getElementById("result");

      if (data.success) {
        resultDiv.innerHTML = `
            <table>
                <tr>
                    <th>Total Students</th>
                    <td>${data.total_students}</td>
                </tr>
                <tr>
                    <th>Passed Students</th>
                    <td>${data.passed_students}</td>
                </tr>
                <tr>
                    <th>Failed Students</th>
                    <td>${data.failed_students}</td>
                </tr>
                <tr>
                    <th>Pass Percentage</th>
                    <td>${data.pass_percentage}%</td>
                </tr>
                <tr>
                    <th>Fail Percentage</th>
                    <td>${data.fail_percentage}%</td>
                </tr>
            </table>
        `;
      } else {
        resultDiv.innerHTML = `<h3 style='color:red;'>Error: ${data.error}</h3>`;
      }
    })
    .catch((error) => {
      console.error("Fetch Error:", error);
      document.getElementById("result").innerHTML =
        "<h3 style='color:red;'>Failed to fetch results.</h3>";
    });
});
