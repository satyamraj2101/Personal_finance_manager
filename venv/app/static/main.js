const form = document.getElementById('registerForm');
const name = document.getElementById('name');
const email = document.getElementById('email');
const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirmPassword');

form.addEventListener('submit', (e) => {
  let messages = [];
  
  if(name.value === '' || name.value == null) {
    messages.push('Name is required');
  }

  if(email.value === '' || email.value == null) {
    messages.push('Email is required');
  }

  if(password.value === '' || password.value == null) {
    messages.push('Password is required'); 
  }

  if(password.value !== confirmPassword.value) {
    messages.push('Passwords do not match');
  }

  if(messages.length > 0) {
    e.preventDefault();
    error.innerText = messages.join(', ');
  }

});

