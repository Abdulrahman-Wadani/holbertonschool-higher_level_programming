const uh = document.querySelector('#update_header');
const header = document.querySelector('header');

uh.addEventListener('click', function () {
  header.textContent = 'New Header!!!';
});
