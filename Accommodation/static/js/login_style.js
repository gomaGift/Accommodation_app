document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from actually submitting
  
    // Retrieve the values from the form
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
  
    // Perform your login logic here (replace with actual login logic)
    // For demonstration, we'll just log the input values
    console.log('Login clicked with username:', username, 'and password:', password);
  });
 
  
  
  
  