const header = document.querySelector('header');
const clickRedButton = document.querySelector('#red_header');

clickRedButton.addEventListener('click', () => {
  header.classList.add ('red');
}
);