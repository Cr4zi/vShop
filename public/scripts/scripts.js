fetch("https://discord.com/api/guilds/892790509691621406/widget.json").then(res => res.json()).then(data => {
    document.getElementById("MemberCount").innerHTML = `${data.members.length} Members`
})

document.querySelector("[alt=DiscordIcon]").addEventListener("click", (e) => {
    if (document.getElementById("DiscordCard").style.display == "none") {
        document.getElementById("DiscordCard").style.display = "block";
        document.getElementById("DiscordCard").style.animation = "CardAnimation 0.3s ease";
    } else {
        document.getElementById("DiscordCard").style.display = "none";
    }
})