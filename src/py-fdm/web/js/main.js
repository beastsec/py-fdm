/**
 * Verify if input creds have or not content.
 */
function CredsVerify(){
    const usernme = document.getElementById('username');
    const password = document.getElementById('password');
    const user_error = document.getElementById('error-user');
    const pass_error = document.getElementById('error-password');
    if (!username.value){
        username.className = 'form-control is-invalid';
        user_error.style.display = 'inline';
        user_error.textContent = 'Username is required';
    }else{
        username.className = 'form-control';
        user_error.style.display = 'none'
    }
    if (!password.value){
        password.className = 'form-control is-invalid';
        pass_error.style.display = 'inline';
        pass_error.textContent = 'Password is required';
    }else{
        password.className = 'form-control';
        pass_error.style.display = 'none';
    }
}
const login = document.getElementById('login');
login.addEventListener('click',CredsVerify);


