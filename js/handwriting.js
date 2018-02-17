// Adapted from: https://www.w3schools.com/graphics/canvas_drawing.asp
var mousePressed = false;
var lastX, lastY;
var ctx;

// Adapted from: https://stackoverflow.com/questions/2368784/draw-on-html5-canvas-using-a-mouse
function InitThis() {
    ctx = document.getElementById("myCanvas").getContext("2d");

    $("#myCanvas").mousedown(function (e) {
        mousePressed = true;
        Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, false);
    });

    $("#myCanvas").mousemove(function (e) {
        if (mousePressed) {
            Draw(e.pageX - $(this).offset().left, e.pageY - $(this).offset().top, true);
        }
    });

    $("#myCanvas").mouseup(function (e) {
        mousePressed = false;
    });
	    $("#myCanvas").mouseleave(function (e) {
        mousePressed = false;
    });
}
// Adapted from: http://www.html5canvastutorials.com/tutorials/html5-canvas-line-color/
function Draw(x, y, isDown) {
    if (isDown) {
        ctx.beginPath();
        ctx.strokeStyle = "black";
        ctx.lineWidth = $("#selWidth").val();
        ctx.lineJoin = "round";
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(x, y);
        ctx.closePath();
        ctx.stroke();
    }
    lastX = x; lastY = y;
}

// Adapted from: http://www.html5canvastutorials.com/advanced/html5-clear-canvas/
function clearArea() {
    // Use the identity matrix while clearing the canvas
    ctx.setTransform(1, 0, 0, 1, 0, 0);
    ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
}

function saveFile(){
	var img = canvas.toDataURL("images/png");

    $.ajax({
        url: "/upload",
        method: 'POST',
        data: img,
        success: function (res) {
            console.log(res);
            $("#prediction").text( res);

        }, error: function (err) {
            console.log(err);
        }
    });
}