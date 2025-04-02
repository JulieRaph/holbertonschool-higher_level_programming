const header = document.querySelector('header');
const clickRedButton = document.querySelector('#toggle_header');

clickRedButton.addEventListener('click', () => {
  header.classList.toggle ('red');
  header.classList.toggle ('green');
}
);