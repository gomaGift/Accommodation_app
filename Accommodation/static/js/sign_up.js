// Form submission handling
const registrationForm = document.getElementById('registrationForm');
const message = document.getElementById('message');

registrationForm.addEventListener('submit', async (event) => {
  event.preventDefault();

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;
  const confirmPassword = document.getElementById('confirmPassword').value;

  if (password !== confirmPassword) {
    message.textContent = 'Password and Confirm Password must match.';
    return;
  }

  // You can make an AJAX request (e.g., using fetch) to your server to register the user.
  // Replace the URL with the actual registration endpoint on your server.
  const response = await fetch('/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      username,
      password,
    }),
  });

  if (response.ok) {
    // Registration was successful, handle the response accordingly
    const data = await response.json();
    message.textContent = 'Registration successful. User ID: ' + data.userId;
  } else {
    // Registration failed, handle the error
    const errorData = await response.json();
    message.textContent = 'Registration failed: ' + errorData.message;
  }
});