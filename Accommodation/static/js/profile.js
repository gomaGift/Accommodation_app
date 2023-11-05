// script.js (for profile functionality)
document.addEventListener('DOMContentLoaded', function() {
    const profileForm = document.getElementById('profile-form');
    const usernameInput = document.getElementById('username');
    const emailInput = document.getElementById('email');
    const fullnameInput = document.getElementById('fullname');
  
    // Simulated user data (replace with your actual user data)
    const userData = {
      username: 'johndoe',
      email: 'john@example.com',
      fullname: 'John Doe',
    };
  
    // Populate form with user data
    usernameInput.value = userData.username;
    emailInput.value = userData.email;
    fullnameInput.value = userData.fullname;
  
    profileForm.addEventListener('submit', function(event) {
      event.preventDefault();
  
      // Simulated update user data (replace with your actual update logic)
      const updatedUserData = {
        username: usernameInput.value,
        email: emailInput.value,
        fullname: fullnameInput.value,
      };
  
      // Display updated user data
      alert('User data updated: ' + JSON.stringify(updatedUserData));
    });
  });
  