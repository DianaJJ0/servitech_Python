const express = require("express");
const path = require("path");
const app = express();

// Configurar EJS como motor de vistas
app.set("view engine", "ejs");
app.set("views", path.join(__dirname));

// Servir archivos estáticos
app.use("/assets", express.static(path.join(__dirname, "assets")));

// Rutas principales
app.get("/", (req, res) => {
  res.render("index");
});
app.get("/registro", (req, res) => {
  res.render("registro");
});
app.get("/login", (req, res) => {
  res.render("login");
});
// Puedes agregar más rutas según tus vistas EJS

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor frontend escuchando en http://localhost:${PORT}`);
});
