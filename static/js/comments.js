const buttonEdit = document.getElementsByClassName("btn-edit");
const textBody = document.getElementById("id_body");
const formComment = document.getElementById("commentForm");
const buttonSubmit = document.getElementById("submitButton")

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

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
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}