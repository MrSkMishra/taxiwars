// console.log("Hello Sk")



// fetch('https://api.sampleapis.com/beers/ale')
//   .then(function(response) {
//     return response.json();
//   })
//   .then(function(data) {
//     var tbody = document.querySelector('#taxi-table tbody');
//     data.forEach(function(taxi) {
//       var row = document.createElement('tr');
//       row.innerHTML = `
//         <td>${taxi.name}</td>
//         <td>${taxi.price}</td>
//         <td>${taxi.rating.average}</td>
//         <td>${taxi.rating.reviews}</td>
//         <td><img src="${taxi.image}" alt="kya hai"></td>
//       `;
//       tbody.appendChild(row);
//     });
//   })
//   .catch(function(error) {
//     console.log('Fetch Error:', error);
//   });



// const form = document.getElementById('login-form');
//   const loginButton = document.getElementById('login-button');

//   // Add event listener for form submission
//   form.addEventListener('submit', function (event) {
//     // Prevent the default form submission behavior
//     event.preventDefault();

//     // Perform custom form validation
//     if (validateForm()) {
//       // If the form is valid, submit the form
//       form.submit();
//     }
//   });

//   // Function to validate the form
//   function validateForm() {
//     // Get the username and password input fields
//     const usernameInput = document.getElementById('username');
//     const passwordInput = document.getElementById('password');

//     // Perform validation checks
//     if (usernameInput.value.trim() === '') {
//       alert('Please enter your username.');
//       return false;
//     }

//     if (passwordInput.value.trim() === '') {
//       alert('Please enter your password.');
//       return false;
//     }

//     // Return true if the form is valid
//     return true;
//   }




//   const signupform = document.getElementById('signup-form');
//   const signupButton = document.getElementById('signup-button');

//   // Add event listener for form submission
//   form.addEventListener('submit', function (event) {
//     // Prevent the default form submission behavior
//     event.preventDefault();

//     // Perform custom form validation
//     if (validateForm()) {
//       // If the form is valid, submit the form
//       form.submit();
//     }
//   });

//   // Function to validate the form
//   function validateForm() {
//     // Get the username and password input fields
//     const firstnameInput = document.getElementById('first_name');
//     const lastnameInput = document.getElementById('last_name');
//     const usernameInput = document.getElementById('username');
//     const passwordInput = document.getElementById('password');

//     // Perform validation checks
//     if (usernameInput.value.trim() === '') {
//       alert('Please enter your username.');
//       return false;
//     }

//     if (passwordInput.value.trim() === '') {
//       alert('Please enter your password.');
//       return false;
//     }

//     // Return true if the form is valid
//     return true;
//   }