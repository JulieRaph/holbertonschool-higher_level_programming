const addList = document.querySelector('#add_item');

addList.addEventListener('click', () => {
    const list = document.querySelector('.my_list');
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.append(newItem);
})

