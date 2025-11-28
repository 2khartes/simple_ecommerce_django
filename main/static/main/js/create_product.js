const imgError = document.getElementById("error_img");
const nameError = document.getElementById("error_name");
const priceError = document.getElementById("error_price");
const stockError = document.getElementById("error_stock");
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

// VALIDACION DE PRECIO

const validatePrice = (value) => {
  if (!value) return (priceError.textContent = "No puede estar vacio");
  else if (value.trim() == "")
    return (priceError.textContent = "No puede estar vacio");
  else if (isNaN(Number(value)))
    return (priceError.textContent = "Debe ser un numero");
  else if (Number(value) <= 0)
    return (priceError.textContent = "Debe ser mayor a 0");
  priceError.textContent = "";
};

document.getElementById("price").addEventListener("keyup", (e) => {
  validatePrice(e.target.value);
});

// VALIDACION DE STOCK

const validateStock = (value) => {
  if (!value) return (stockError.textContent = "No puede estar vacio");
  else if (value.trim() == "")
    return (stockError.textContent = "No puede estar vacio");
  else if (isNaN(Number(value)))
    return (stockError.textContent = "Debe ser un numero");
  else if (Number(value) <= 0)
    return (stockError.textContent = "Debe ser mayor a 0");
  stockError.textContent = "";
};

document.getElementById("stock").addEventListener("keyup", (e) => {
  validateStock(e.target.value);
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

// VALIDACION DE IMAGEN

const validateImg = (file) => {
  if (!file) return (imgError.textContent = "No puede quedar vacia");
  const container = document.getElementById("container-img");
  container.innerHTML = "";
  const img = document.createElement("img");
  img.src = URL.createObjectURL(file);
  container.appendChild(img);
  imgError.textContent = "";
};

document.getElementById("img").addEventListener("change", (e) => {
  validateImg(e.target.files[0]);
});

// VALIDAR ANTES DE ENVIAR EL FORMULARIO
document.getElementById("product_form").addEventListener("submit", (e) => {
  const name = document.getElementById("name").value;
  const price = document.getElementById("price").value;
  const stock = document.getElementById("stock").value;
  const desc = document.getElementById("description").value;
  const img = document.getElementById("img").files[0];

  const validName = validateName(name);
  const validPrice = validatePrice(price);
  const validStock = validateStock(stock);
  const validDesc = validateDesciption(desc);

  if (!e.target.action.includes("update")) {
    const validImg = validateImg(img);
    if (validName || validPrice || validStock || validDesc || validImg)
      return e.preventDefault();

    return;
  }

  if (validName || validPrice || validStock || validDesc)
    return e.preventDefault();
});
