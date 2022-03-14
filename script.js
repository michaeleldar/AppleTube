var key;

function tutorials_clicked() {
    window.location.href = "tutorials.html";
}
function scratchtube_clicked() {
    window.location.href = "scratchtube.html";
}
function games_clicked() {
    window.location.href = "games.html";
}
function eval_key() {
    key = document.getElementById("key_text_box").value
    if (key == "6ty9lkpy") {
        window.location.href = "pro.html";
    }
    else {
        alert("Incorrect Key")
    }
}

function scratch_link_enter() {
    alert("Add Games Manually For Now...")
}