const header = document.querySelector('header');
const clickRedButton = document.querySelector('#red_header');

clickRedButton.addEventListener('click', () => {
  header.style.color = '#FF0000';
}
);