document.getElementById('toggle_header').addEventListener('click', function() {
  // Select the header element
  const header = document.querySelector('header');

  // Toggle between "red" and "green" classes
  if (header.classList.contains('red')) {
      header.classList.remove('red');
      header.classList.add('green');
  } else {
      header.classList.remove('green');
      header.classList.add('red');
  }
});
