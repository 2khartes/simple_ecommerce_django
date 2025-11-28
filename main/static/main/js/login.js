const usernameError = document.getElementById("error_username");
const passwordError = document.getElementById("error_password");

const validatePassword = (value) => {
  if (!value) return (passwordError.textContent = "No puede quedar vacia");
  else if (value.length < 6)
    return (passwordError.textContent = "Minimo 6 caracteres");
  passwordError.textContent = "";
};

document.getElementById("password").addEventListener("keyup", (e) => {
  validatePassword(e.target.value);
});

const validateUsername = (value) => {
  if (!value) return (usernameError.textContent = "No Puede quedar vacio");
  else if (value.length < 6)
    return (usernameError.textContent = "Minimo 6 caracteres");
  usernameError.textContent = "";
};

document.getElementById("username").addEventListener("keyup", (e) => {
  validateUsername(e.target.value);
});

document.getElementById("auth_form").addEventListener("submit", (e) => {
  const password = document.getElementById("password").value;
  const username = document.getElementById("username").value;

  const passwordValid = validatePassword(password);
  const usernameValid = validateUsername(username);

  if (passwordValid || usernameValid) return e.preventDefault();
});
