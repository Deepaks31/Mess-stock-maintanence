document.addEventListener("DOMContentLoaded", function() {
    const toggleButton = document.querySelector('.toggle');
    const sidebar = document.querySelector('.sidebar');
    const dashboard = document.querySelector('.dashboard');
  
    toggleButton.addEventListener('click', function() {
      sidebar.classList.toggle('close');
      if (sidebar.classList.contains('close')) {
        dashboard.style.paddingLeft = '88px'; // Adjust this value based on your sidebar width
      } else {
        dashboard.style.paddingLeft = '250px'; // Adjust this value based on your sidebar width
      }
    });
  });
  


