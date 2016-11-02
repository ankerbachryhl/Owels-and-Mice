//Proev imorgen at lave en ny grid for hver ny mus. Istedet for en masse mus paa en grid.

var population;
var cols, rows;
var w = 40;
var grid = [];
var mouseAmount = 10;
var secGrid = [];
var moveTo;

var current;
var currentNum;

function setup() {
  createCanvas(800, 800);
  cols = floor(width/w)
  rows = floor(height/w)
  frameRate(5);

  for (var j = 0; j < rows; j++) {
    for ( var i = 0; i < cols; i++) {
      var cells = new Cells(i,j);
      var mouses = new Mouse(i,j);
      grid.push(cells);
      secGrid.push(mouses)
    }
    this.currents = [];
    for (var i = 0; i < mouseAmount; i++) {
      currentNum = floor(random(secGrid.length));
      current = secGrid[i];
      this.currents.push(current);
    }
    for (var i = 0; i < mouseAmount; i++) {
      this.currents[i].visited = true;
    }
  }
  population = new Population();



}

function draw() {
  background(51);
  for ( var i = 0; i < secGrid.length; i++) {
    secGrid[i].show();
  }
  for ( var i = 0; i < grid.length; i++) {
    grid[i].show();
  };

  population.run();
  population.update();
  for (var i = 0; i < mouseAmount; i++) {

    var nextCell = current.move();
    if (nextCell) {
      nextCell.visited = true;
      current.visited = false;
      current = nextCell;
    }
  }


}

function index(i, j) {
  if (i < 0 || j < 0 ||  i > cols-1 || j > rows-1 ) {
    return -1;
  }
  return i + j * cols;
}





function Population() {

  this.currents = [];

  this.run = function() {
    for (var i = 0; i < mouseAmount; i++) {
      currentNum = floor(random(secGrid.length));
      current = secGrid[currentNum];
      this.currents.push(current);
    }

  }

  this.update = function() {
    for (var i = 0; i < mouseAmount; i++) {
      this.currents[i].visited = true;
    }
  }

}

// function DNA() {
//   this.update = function() {

//   }
// }



function Mouse(i, j) {
  this.i = i;
  this.j = j;
  this.visited = false;

  this.move = function() {
    var neighbors = [];
    var r = random(1);


    if ( r < 0.25) {
      moveTo = grid[index(i, j -1)];
    } else if (r < 0.5) {
      moveTo = grid[index(i+1, j)];
    } else if (r < 0.75) {
      moveTo = grid[index(i, j+1)];
    } else {
      moveTo = grid[index(i-1, j)];
    }

    return moveTo;

    // var top = grid[index(i, j -1)];
    // var right = grid[index(i+1, j)];
    // var bottom = grid[index(i, j+1)];
    // var left = grid[index(i-1, j)];
    // //Add more neighbors like: i-1, j+1 = venstre hjoerne
    //
    // if (top && !top.visited) {
    //   neighbors.push(top)
    // }
    //
    // if (right && !right.visited) {
    //   neighbors.push(right)
    // }
    //
    // if (bottom && !bottom.visited) {
    //   neighbors.push(bottom)
    // }
    //
    // if (left && !left.visited) {
    //   neighbors.push(left)
    // }
    //
    // if(neighbors.length > 0) {
    //   var r = floor(random(0, neighbors.length));
    //   return neighbors[r];
    // } else {
    //   return undefined;
    // }

  }
  this.show = function() {
    var x = this.i*w;
    var y = this.j*w;
    stroke(255);
    noFill();
    rect(x,y,w,w);
  }
}


function Cells(i, j) {
  this.i = i;
  this.j = j;
  this.visited = false;

  this.move = function() {
    var neighbors = [];



    var top = grid[index(i, j -1)];
    var right = grid[index(i+1, j)];
    var bottom = grid[index(i, j+1)];
    var left = grid[index(i-1, j)];
    //Add more neighbors like: i-1, j+1 = venstre hjoerne

    if (top) {
      neighbors.push(top)
    }

    if (right) {
      neighbors.push(right)
    }

    if (bottom) {
      neighbors.push(bottom)
    }

    if (left) {
      neighbors.push(left)
    }

    if(neighbors.length > 0) {
      var r = floor(random(0, neighbors.length));
      return neighbors[r];
    } else {
      return undefined;
    }

  }


  this.show = function() {
    var x = this.i*w;
    var y = this.j*w;
    if (this.visited) {
      fill(255, 0, 255, 100)
      rect(x, y, w, w)
    }
  }
}
