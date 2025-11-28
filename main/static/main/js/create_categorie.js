const nameError = document.getElementById("error_name");
const descError = document.getElementById("error_description");

// VALIDACION DE NOMBRE

const validateName = (value) => {
  if (!value) return (nameError.textContent = "No puede estar vacio");
  else if (value.trim() == "")
    return (nameError.textContent = "No puede estar vacio");
  else if (value.length < 4)
    return (nameError.textContent = "Minimo 4 caracteres");
  nameError.textContent = "";
};

document.getElementById("name").addEventListener("keyup", (e) => {
  validateName(e.target.value);
});

// VALIDACION DE DESCRIPCION

const validateDesciption = (value) => {
  if (!value) return (descError.textContent = "No puede estar vacia");
  else if (value.trim() == "")
    return (descError.textContent = "No puede estar vacia");
  else if (value.length < 4)
    return (descError.textContent = "Minimo 4 caracteres");
  descError.textContent = "";
};

document.getElementById("description").addEventListener("keyup", (e) => {
  validateDesciption(e.target.value);
});

// VALIDAR ANTES DE ENVIAR EL FORMULARIO
document.getElementById("categorie_form").addEventListener("submit", (e) => {
  const name = document.getElementById("name").value;
  const desc = document.getElementById("description").value;

  const validName = validateName(name);
  const validDesc = validateDesciption(desc);

  if (validName || validDesc) return e.preventDefault();
});
