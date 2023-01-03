
// event listener for submit button
const submitButton = document.querySelector('#submitButton');

function savedEditedPost() {
    document.querySelector('#blogtext').style.display = 'none';
};

// event listener for delete button
for (const button of document.querySelectorAll('.delete')) {
    button.addEventListener('click', (evt) => {
        evt.preventDefault()
        const post_id = evt.target.id
        fetch(`/delete-post/${post_id}`, {
          // this is the end point i want to connect
          // this builds up the HTTP request
            method: 'POST',
            body: '',
            // if my request has a lot of parameters/data, this shows it
            headers: {
              'Content-Type': 'application/json',
            },
            // metadata is info about the request itself. content-type describes the format in my body
            // can include language
          })
            // .then((response) => response.json())
            // .then((responseJson) => {
            //   alert(responseJson.status);
        const post = document.querySelector(`#post-${button.id}`)
        post.style.display= 'none';
        });
    }
