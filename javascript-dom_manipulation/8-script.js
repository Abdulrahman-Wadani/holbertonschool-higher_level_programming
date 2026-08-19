document.addEventListener('DOMContentLoaded', function () {
  const hellodev = document.querySelector('#hello');

  async function hellof () {
    const respons = await fetch('https://hellosalut.stefanbohacek.com/?lang=fr');
    const data = await respons.json();
    hellodev.textContent = data.hello;
  }
  hellof();
});
