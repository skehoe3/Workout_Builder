//https://teamtreehouse.com/community/how-to-reset-a-contact-form-with-javascript
const resForm = document.getElementById("inputForm");

resForm.addEventListener('click', function(){
    document.getElementById("inputForm").reset();
});