document.addEventListener("DOMContentLoaded", function(){
    console.log("DOM Content Loaded, script running");

    // Get form data
    const form_user = document.getElementById("username");
    const form_pass = document.getElementById("password");
    const form = document.getElementById("login_form");

    form.addEventListener("submit", function(e){
        e.preventDefault();
        let username = form_user.value;
        let password = form_pass.value;

        let data = {
            'user':username,
            'pass':password
        }

        // TODO: Test this
        fetch("http://localhost:8000/api/test_post", {  // Make the api request
            method: 'POST',  // Use the POST method
            headers: {
                'Content-Type': 'application/json'  // State we are sending JSON data
            },
            body: JSON.stringify(data)  // Set the data to send as a string
        })
    });
});