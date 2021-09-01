const express = require("express");
const path = require("path");
const app = express();

app.use(express.static(path.join(__dirname, "public")));

app.listen(3000, async () => {
    console.log("The Server Is Runing On Port 3000, http://localhost:3000/pages/Home.html")
});

