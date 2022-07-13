
// event listener for submit button
const submitButton = document.querySelector('#submitButton');

function savedEditedPost() {
    document.querySelector('#blogtext').style.display = 'none';
};

//submitButton.addEventListener('click', savedEditedPost);

// event listener for delete button
for (const button of document.querySelectorAll('.delete')) {
    button.addEventListener('click', (evt) => {
        evt.preventDefault()
        const post_id = evt.target.id
        fetch(`/delete-post/${post_id}`, {
          // this is the end point i want to connect to
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
// requests and responses have different requirements


   //        .then((response) => response.text())
//        .then(successFunction)

// evt.target
// evt only has meaning inside a call back function



//fetch(`/delete-post/${post_id}`, {
 //   method: 'POST',
//})
// create an event listener for this submit button
// write a function that hides the summertext editor (type is onclick)
// after it hides then update the post information
// unpack JSON data
// grab the HTML elements for post subject, post text, and post tag then edit the information using the JSON 





// write a function that makes an AJAX request to edit the post and replace it with new text


