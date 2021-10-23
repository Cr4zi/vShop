if (document.getElementById("MemberCount")) {
    fetch("assets/membercount.json").then(res => res.json()).then(data => {
        document.getElementById("MemberCount").innerHTML = `${data.res} Members`
    })
}

document.addEventListener("click", (e) => {
    if (document.getElementById("DiscordCard") && document.getElementById("DiscordCard").style.display != "none" && e.srcElement?.alt != "DiscordIcon") {
        document.getElementById("DiscordCard").style.display = "none";
    } else if (document.getElementById("MoreCard") && document.getElementById("MoreCard").style.display != "none" && e.target.innerHTML != "More") {
        document.getElementById("MoreCard").style.display = "none";
        document.getElementById("MoreBorder").style.display = "none";
    }
})

document.querySelector("[alt=DiscordIcon]")?.addEventListener("click", (e) => {
    if (document.getElementById("DiscordCard").style.display == "none") {
        document.getElementById("DiscordCard").style.display = "block";
        document.getElementById("DiscordCard").style.animation = "CardAnimation 0.3s ease";
    } else {
        document.getElementById("DiscordCard").style.display = "none";
    }
})

document.getElementById("MoreButton")?.addEventListener("click", (e) => {
    if (document.getElementById("MoreCard").style.display == "none") {
        document.getElementById("MoreCard").style.display = "block";
        document.getElementById("MoreBorder").style.display = "block";
        document.getElementById("MoreCard").style.left = 875+"px";
        
        document.getElementById("MoreCard").animate([{
            left: "820px"
        },{
            left: "875px"
        }], 30)
        document.getElementById("MoreBorder").animate([{
            opacity: "0%"
        },{
            opacity: "100%"
        }], 30)
    } else {
        document.getElementById("MoreCard").style.display = "none";
        document.getElementById("MoreBorder").style.display = "none";
    }
})