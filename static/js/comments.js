const buttonEdit = document.getElementsByClassName("btn-edit");
const textBody = document.getElementById("id_body");
const formComment = document.getElementById("commentForm");
const buttonSubmit = document.getElementById("submitButton")

const modalDelete = new bootstrap.Modal(document.getElementById("deleteModal"));
const buttonDelete = document.getElementsByClassName("btn-delete");
const confirmDelete = document.getElementById("deleteConfirm");

/** Edit button */

for (let button of buttonEdit) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        textBody.value = commentContent;
        buttonSubmit.innerText = "Update";
        formComment.setAttribute("action", `edit_comment/${commentId}`);
    });
}

/** Delete button */
for (let button of buttonDelete) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        confirmDelete.hred = `delete_comment/${commentId}`;
        modalDelete.show();
    })
}