var w = 40;
var grid = [];
var mouses = 10;
var mouseAmount = [];
var owlAmount = [];
var Mouse;
var current;
var timesMouses = 151;
var mousesP;


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
  amount = new Amount;
  mousesP = createP();

  setInterval(Owls, 5000)
  setInterval(Next, 5000)
  setInterval(function() {
    for (var i = 0; i < mouseAmount.length; i--) {
        if (mouseAmount[i].dead === true) {
          timesMouses -= 1;
          mouseAmount.splice(i,1)
          // mouseAmount[i].active = false;
          console.log('the mouse has been eaten')
          console.log(mouseAmount.length)
        } else {
          console.log('what doesnt kill me makes me stronger')
        }
    }
  }, 5000)

}

function draw() {
  background(1000);
  for ( var i = 0; i < grid.length; i++) {
    grid[i].show();
  }

  mousesP.html(mouseAmount.length)
  amount.run();


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
  this.owlActive = false;
  this.doubleactive = false;
  this.dead = false;


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

    if(this.dead == true) {
      fill(251)
      rect(x, y, w, w)
    }

    if(this.doubleactive == true) {
      fill(51)
      rect(x, y, w, w)
    }
    if(this.owlActive == true) {
      fill('red')
      rect(x, y, w, w)
    }


  }
}

function Amount() {
  this.run = function() {

    if (mouseAmount.length < timesMouses -1) {
      for (var i = 0; i < 1; i++) {
        var r = floor(random(grid.length))
        var mouse = grid[r];
        mouseAmount.push(mouse)
      }
      mouse.active = true;
    }
    if (owlAmount.length < 2) {
      for (var i = 0; i < 1; i++) {
        var r = floor(random(grid.length))
        var owl = grid[r];
        owlAmount.push(owl)
        console.log(owlAmount.length)
      }
      owl.owlActive = true;
    }
    var sortedMouses = mouseAmount.slice().sort();

    for (var i = 0; i < mouseAmount.length - 1; i++) {
      if (sortedMouses[i + 1].i == sortedMouses[i].i && sortedMouses[i + 1].j == sortedMouses[i].j) {
        sortedMouses[i].doubleactive = true;
        mouseAmount[i].doubleactive = true;
      }
    }

  }
}

function Owls(i,j) {
  this.i = i;
  this.j = j;
  for (var i = 0; i < 3; i++) {

      var choice = floor(random(4));

      var top = grid[index(owlAmount[i].i, owlAmount[i].j -1)];
      var right = grid[index(owlAmount[i].i+1, owlAmount[i].j)];
      var bottom = grid[index(owlAmount[i].i, owlAmount[i].j+1)];
      var left = grid[index(owlAmount[i].i-1, owlAmount[i].j)];


      if (top && choice == 0) {
          top.owlActive = true;
          owlAmount[i].owlActive = false;
          owlAmount[i] = top;



      }

      if (right && choice == 1) {
            right.owlActive = true;
            owlAmount[i].owlActive = false;
            owlAmount[i] = right;

      }

      if (bottom && choice == 2) {
          bottom.owlActive = true;
          owlAmount[i].owlActive = false;
          owlAmount[i] = bottom;


      }

      if (left && choice == 3) {
          left.owlActive = true;
          owlAmount[i].owlActive = false;
          owlAmount[i] = left;
          // mouseAmount[i].i = mouseAmount[i].i -1
      }


    }
}

function Next(i,j) {
  this.array = [];
  this.i = i;
  this.j = j;


  for (var i = 0; i < timesMouses; i++) {

      var choice = floor(random(4));
      mouseAmount[i].steps += 1;

      // if (mouseAmount[i].steps == 1) {
      //   timesMouses -= 1;
      //   mouseAmount[i].active = false;
      //   mouseAmount.splice(i,1);
      //   console.log(mouseAmount[i].steps)
      // }


      var top = grid[index(mouseAmount[i].i, mouseAmount[i].j -1)];
      var right = grid[index(mouseAmount[i].i+1, mouseAmount[i].j)];
      var bottom = grid[index(mouseAmount[i].i, mouseAmount[i].j+1)];
      var left = grid[index(mouseAmount[i].i-1, mouseAmount[i].j)];



      if (top && choice === 0) {
          top.active = true;
          mouseAmount[i].active = false;
          mouseAmount[i] = top;
        if (top.owlActive == true) {
          mouseAmount[i].dead = true;

        }

      }

      if (right && choice == 1) {
            right.active = true;
            mouseAmount[i].active = false;
            mouseAmount[i] = right;
            if (right.owlActive == true) {
              mouseAmount[i].dead = true;
            }
      }

      if (bottom && choice == 2) {
          bottom.active = true;
          mouseAmount[i].active = false;
          mouseAmount[i] = bottom;
          if (bottom.owlActive == true) {
            mouseAmount[i].dead = true;
          }

      }

      if (left && choice == 3) {
          left.active = true;
          mouseAmount[i].active = false;
          mouseAmount[i] = left;
          if (left.owlActive == true) {
            mouseAmount[i].dead = true;
          }

      }

      if (mouseAmount[i].doubleactive == true) {

        if (top && choice === 0) {
            top.active = true;
            mouseAmount[i].doubleactive = false;
            mouseAmount[i] = top;
            // mouseAmount[i].j = mouseAmount[i].j -1

        }

        if (right && choice == 1) {
              right.active = true;
              mouseAmount[i].doubleactive = false;
              mouseAmount[i] = right;
        }

        if (bottom && choice == 2) {
            bottom.active = true;
            mouseAmount[i].doubleactive = false;
            mouseAmount[i] = bottom;

        }

        if (left && choice == 3) {
            left.active = true;
            mouseAmount[i].doubleactive = false;
            mouseAmount[i] = left;
            // mouseAmount[i].i = mouseAmount[i].i -1

        }
      }


      //Proplem der skal løses imorgen: Hvis de er ude i kanten og for eksempel left ikke findes og choice = 3 så står de stille...




    }



}






    // for (var i = 0; i < mouseAmount.length; i++) {
    //   var otherthing = mouseAmount[i].i + mouseAmount[i].j;
    //   var otheri = mouseAmount[1].i + mouseAmount[1].j;
    //   if (otherthing == otheri && this.active == true) {
    //     var square = rect(x, y, w, w)
    //     square.fill(255, 0, 255, 100)
    //
    //   } else
    // }

//Grunden er at når de alle sammen skifter fra active:true til active:false sår stoper update function med at update.
