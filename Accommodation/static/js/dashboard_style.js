// script.js (for dashboard functionality)
document.addEventListener('DOMContentLoaded', function() {
    const options = document.querySelectorAll('.options a');
  
    options.forEach(option => {
      option.addEventListener('click', function(e) {
        e.preventDefault();
        alert(`You clicked: ${option.textContent}`);
      });
    });
  });