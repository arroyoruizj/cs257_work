function changeColor() {
  the_heading = document.getElementById("hello");
  the_heading.style.color = "red";
  console.log("I just changed the color to: " + the_heading.style.color)  
}

function reveal(clicked_image) {
  image_clicked = document.getElementById(clicked_image)
  random_num = Math.floor(Math.random() * 3) + 1;

    if (random_num === 3) {
        image_clicked.src = "static/images/money_door.png";
        } 
    else {
        image_clicked.src = "static/images/snake_door.png";
        }
  
}
