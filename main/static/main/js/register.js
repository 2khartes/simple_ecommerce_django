const usernameError = document.getElementById("error_username");
const passwordError = document.getElementById("error_password1");
const passwordError2 = document.getElementById("error_password2");

const validatePassword = (value) => {
  if (!value) return (passwordError.textContent = "No puede quedar vacia");
  else if (value.length < 6)
    return (passwordError.textContent = "Minimo 6 caracteres");
  passwordError.textContent = "";
};

document.getElementById("password1").addEventListener("keyup", (e) => {
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

const validateSecondPassword = (value) => {
  const pass = document.getElementById("password1").value;
  if (!value)
    return (passwordError2.textContent =
      "La contraseña de validacion no puede quedar vacia");
  else if (pass != value)
    return (passwordError2.textContent = "Las contraseñas no coinciden");

  passwordError2.textContent = "";
};

document.getElementById("password2").addEventListener("keyup", (e) => {
  validateSecondPassword(e.target.value);
});

document.getElementById("auth_form").addEventListener("submit", (e) => {
  const password = document.getElementById("password1").value;
  const password2 = document.getElementById("password2").value;
  const username = document.getElementById("username").value;

  const passwordValid = validatePassword(password);
  const secondPasswordValid = validateSecondPassword(password2);
  const usernameValid = validateUsername(username);

  if (passwordValid || usernameValid || secondPasswordValid)
    return e.preventDefault();
});
