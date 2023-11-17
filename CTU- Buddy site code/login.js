function signup() {
    const username = document.getElementById("signup-username").value;
    const password = document.getElementById("signup-password").value;
    
    // Store user information 
    localStorage.setItem(username, password);
    
    // Clear the signup form
    document.getElementById("signup-username").value = "";
    document.getElementById("signup-password").value = "";
    
    alert("Sign up successful! You can now login.");
}

function login() {
    const username = document.getElementById("login-username").value;
    const password = document.getElementById("login-password").value;
    
    // Check if the entered password matches the stored password
    const storedPassword = localStorage.getItem(username);
    
    if (password === storedPassword) {
        // Successful login
        document.getElementById("signup-form").style.display = "none";
        document.getElementById("login-form").style.display = "none";
        document.getElementById("profile").style.display = "block";
        document.getElementById("profile-username").textContent = username;
    } else {
        alert("Login failed. Please check your username and password.");
    }
}

function logout() {
    // Clear the user's data from the profile
    document.getElementById("profile").style.display = "none";
    document.getElementById("signup-form").style.display = "block";
    document.getElementById("login-form").style.display = "block";
    
    // Clear the login form
    document.getElementById("login-username").value = "";
    document.getElementById("login-password").value = "";
}
