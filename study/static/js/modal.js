// Get the modal
var modal = document.getElementById("myModal");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
document.getElementById("delete_blog").onclick = function() {
  modal.style.display = "block";
  document.getElementById("yes").setAttribute("data-blog-id", this.getAttribute('data-blog-id'));
}

document.getElementById("no").onclick = function(){
    modal.style.display = "none";
}

document.getElementById("yes").onclick = function(){
    window.location.href = "/blog_delete/" + this.getAttribute('data-blog-id');
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}