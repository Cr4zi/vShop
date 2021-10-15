const express = require("express");
const path = require("path");
const app = express();

app.use("/assets/", express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "pages", "coming_soon.html"))
})

app.listen(3000, async () => {
    console.log("The Server Is Runing On Port 3000, http://localhost:3000/")
});