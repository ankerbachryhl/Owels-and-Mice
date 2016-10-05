var w = 40;
var grid = [];
var Mouse;


function setup() {
  createCanvas(800, 800);
  cols = floor(width/w)
  rows = floor(height/w)
  // frameRate(5);

  for (var j = 0; j < rows; j++) {
    for ( var i = 0; i < cols; i++) {
      var cell = new Cells(i,j);
      grid.push(cell);
    }
  }
  Mouse = new Mouse;
}

function draw() {
  background(255);
  for ( var i = 0; i < grid.length; i++) {
    grid[i].show();
  }
  Mouse.run();
}

function index(i, j) {
  if (i < 0 || j < 0 ||  i > cols-1 || j > rows-1 ) {
    return -1;
  }
  return i + j * cols;
}


function Cells(i, j) {
  this.i = i;
  this.j = j;
  this.steps = 0;
  this.active = false;


  this.show = function() {
    var x = this.i*w;
    var y = this.j*w;
    stroke(51);
    noFill();
    rect(x,y,w,w);

    if(this.active == true) {
      fill(155, 0, 255, 100)
      rect(x, y, w, w)
    }
    if(this.maxactive == 150) {
      fill(255,255,255,255)
      rect(x, y, w, w)
    }
  }
}

function Mouse() {
  this.maxactive = 0;
  this.run = function() {

      var r = floor(random(grid.length))
      grid[0].active = true;
      this.maxactive+= 1;
      console.log(this.maxactive)
  }
}
