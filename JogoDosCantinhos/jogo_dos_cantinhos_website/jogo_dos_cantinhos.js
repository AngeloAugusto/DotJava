class Piece {
    constructor(player, x, y) {
        this.player = player;
        this.x = x;
        this.y = y;
        this.color = player == 1 ? "red" : "blue";
    }
}

let board = document.getElementById("Board");

function drawBoard() {
    let ctx = board.getContext("2d");
    ctx.moveTo(30, 30);
    ctx.lineTo(30, 270);
    ctx.moveTo(150, 30);
    ctx.lineTo(150, 270);
    ctx.moveTo(270, 30);
    ctx.lineTo(270, 270);
    ctx.moveTo(30, 30);
    ctx.lineTo(270, 30);
    ctx.moveTo(30, 270);
    ctx.lineTo(270, 270);
    ctx.moveTo(30, 150);
    ctx.lineTo(270, 150);
    ctx.stroke();
}

drawBoard()
