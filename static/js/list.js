$(function () {
  $("#addJobForm").on("submit", function (e) {
    e.preventDefault();
    $.ajax({
      url: "/add_job",
      method: "POST",
      data: $(this).serialize(),
      success: function (response) {
        if (response.status === "success") {
          alert(response.message);
          location.reload();
        }
      },
      error: function () {
        alert("Failed to add job. Please try again.");
      },
    });
  });

  const jobList = $("#jobList")[0];
  const departmentCheckboxes = $(".department-checkbox");
  const searchBox = $("#searchBox");

  departmentCheckboxes.on("change", filterJobs);
  searchBox.on("input", filterJobs);

  function filterJobs() {
    const searchTerm = searchBox.val().toLowerCase();
    const selectedDepartments = departmentCheckboxes
      .filter(":checked")
      .map(function () {
        return this.value;
      })
      .get();

    $(jobList.rows).each(function () {
      const title = this.cells[0].textContent.toLowerCase();
      const department = this.dataset.department;
      this.style.display =
        title.includes(searchTerm) &&
        (selectedDepartments.length === 0 ||
          selectedDepartments.includes(department))
          ? ""
          : "none";
    });
  }
});
