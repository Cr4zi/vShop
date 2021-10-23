const express = require("express");
const path = require("path");
const app = express();
const Discord = require("discord.js")
const client = new Discord.Client({
    intents: Object.values(Discord.Intents.FLAGS)
});
client.login("ODk4NTY0MTAzNzIxODY5MzEy.YWmDCA.TN8BJ5mrg5fvrY8zj-1F0wo5tLs")

app.use("/assets/", express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "pages", "coming_soon.html"))
})

app.get("/home", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "pages", "home.html"))
})

app.get("/@me", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "pages", "home_logged_in.html"))
})

app.get("/login", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "pages", "login.html"))
});

app.get("/signup", (req, res) => {
    res.sendFile(path.join(__dirname, "public", "pages", "signup.html"))
});

app.get("/assets/membercount.json", (req, res) => {
    res.send({
        status: 200,
        res: client.guilds.cache.get("892790509691621406").memberCount.toLocaleString()
    })
})

app.listen(3000, async () => {
    console.log("The Server Is Runing On Port 3000, http://localhost:3000/")
});