document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const inputId = document.getElementById('input-id');
    const usersList = document.getElementById('users');
    const errorMessage = document.getElementById('error-message');
    const userListTitle = document.getElementById('user-list-title');

    form.addEventListener('submit', function(event) {
        event.preventDefault();

        const value = inputId.value.trim();
        if (value) {
            inputId.classList.remove('error');
            errorMessage.style.display = 'none';

            const listItem = document.createElement('li');
            listItem.textContent = value;

            usersList.appendChild(listItem);

            if (usersList.children.length === 1) {
                userListTitle.style.display = 'block';
            }

            inputId.value = '';
        } else {
            inputId.classList.add('error');
            errorMessage.style.display = 'block';
        }
    });
});
