fetch("assets/membercount.json").then(res => res.json()).then(data => {
    document.getElementById("MemberCount").innerHTML = `${data.res} Members`
});

document.addEventListener("click", (e) => {
    if (document.getElementById("DiscordCard").style.display != "none" && e.srcElement?.alt != "DiscordIcon") {
        document.getElementById("DiscordCard").style.display = "none";
    }
})

document.querySelector("[alt=DiscordIcon]").addEventListener("click", (e) => {
    if (document.getElementById("DiscordCard").style.display == "none") {
        document.getElementById("DiscordCard").style.display = "block";
        document.getElementById("DiscordCard").style.animation = "CardAnimation 0.3s ease";
    } else {
        document.getElementById("DiscordCard").style.display = "none";
    }
})
