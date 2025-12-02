document.getElementById("loginForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const user = document.getElementById("username").value;
    const pass = document.getElementById("password").value;

    // Change these credentials to anything you want:
    if (user === "student" && pass === "password123") {
        window.location.href = "../homepage/index.html";
    } else {
        const msg = document.getElementById("loginMessage");
        msg.innerText = "Invalid login. Try again.";
        msg.style.color = "red";
    }
});
