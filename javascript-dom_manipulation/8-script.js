fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    const translation = data.hello;
    const helloElement = document.getElementById('hello');
    helloElement.textContent = translation;
  })
  .catch(error => {
    console.error('Fetch error:', error.message);
  });
