var key;

function tutorials_clicked() {
    window.location.href = "tutorials";
}
function scratchtube_clicked() {
    window.location.href = "scratchtube";
}
function games_clicked() {
    window.location.href = "games";
}
function eval_key() {
    key = document.getElementById("key_text_box").value
    if (key == "6ty9lkpy") {
        window.location.href = "pro";
    }
    else {
        alert("Incorrect Key")
    }
}

function scratch_link_enter() {
    alert("Add Games Using add_game.py for now...")
}