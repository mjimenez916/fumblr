// event listener for edit button
const editPostButton = document.querySelector('#editButton');

function showTextEditor() {
    document.querySelector('#blogtext').style.display = 'block';
};

editPostButton.addEventListener('click', showTextEditor);
