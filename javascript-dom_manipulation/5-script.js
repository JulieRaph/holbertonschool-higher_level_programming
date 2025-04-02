const oldHeader = document.querySelector('header');
const updateHeader = document.querySelector('#update_header');

updateHeader.addEventListener('click', () => {
    const newHeader = document.createElement('header');
    newHeader.textContent = 'New Header!!!';
    oldHeader.replaceWith(newHeader);
})