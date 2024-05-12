function changeColor() {
  the_heading = document.getElementById("hello");
  the_heading.style.color = "red";
  console.log("I just changed the color to: " + the_heading.style.color)  
}

function reveal(clicked_image) {
  image_clicked = document.getElementById(clicked_image)
  result_text = document.getElementById("adv_results")
  random_num = Math.floor(Math.random() * 3) + 1;

    if (random_num === 3) {
        image_clicked.src = "static/images/money_door.png";
        result_text.innerText = "Congratulations! You chose the correct door."
        result_text.style.color = "black";
        } 
    else {
        image_clicked.src = "static/images/snake_door.png";
        result_text.innerText = "You chose the wrong door!"
        result_text.style.color = "black"
        }
  
}
