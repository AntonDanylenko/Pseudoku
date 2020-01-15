var AllVals = new Set([1,2,3,4,5,6,7,8,9]);
var Cliques = [new Set([0,1,2,3,4,5,6,7,8]),
              new Set([9,10,11,12,13,14,15,16,17]),
              new Set([18,19,20,21,22,23,24,25,26]),
              new Set([27,28,29,30,31,32,33,34,35]),
              new Set([36,37,38,39,40,41,42,43,44]),
              new Set([45,46,47,48,49,50,51,52,53]),
              new Set([54,55,56,57,58,59,60,61,62]),
              new Set([63,64,65,66,67,68,69,70,71]),
              new Set([72,73,74,75,76,77,78,79,80]),
              new Set([0,9,18,27,36,45,54,63,72]),
              new Set([1,10,19,28,37,46,55,64,73]),
              new Set([2,11,20,29,38,47,56,65,74]),
              new Set([3,12,21,30,39,48,57,66,75]),
              new Set([4,13,22,31,40,49,58,67,76]),
              new Set([5,14,23,32,41,50,59,68,77]),
              new Set([6,15,24,33,42,51,60,69,78]),
              new Set([7,16,25,34,43,52,61,70,79]),
              new Set([8,17,26,35,44,53,62,71,80]),
              new Set([0,1,2,9,10,11,18,19,20]),
              new Set([3,4,5,12,13,14,21,22,23]),
              new Set([6,7,8,15,16,17,24,25,26]),
              new Set([27,28,29,36,37,38,45,46,47]),
              new Set([30,31,32,39,40,41,48,49,50]),
              new Set([33,34,35,42,43,44,51,52,53]),
              new Set([54,55,56,63,64,65,72,73,74]),
              new Set([57,58,59,66,67,68,75,76,77]),
              new Set([60,61,62,69,70,71,78,79,80])
              ];
var squares = [[0,1,2,9,10,11,18,19,20],
              [3,4,5,12,13,14,21,22,23],
              [6,7,8,15,16,17,24,25,26],
              [27,28,29,36,37,38,45,46,47],
              [30,31,32,39,40,41,48,49,50],
              [33,34,35,42,43,44,51,52,53],
              [54,55,56,63,64,65,72,73,74],
              [57,58,59,66,67,68,75,76,77],
              [60,61,62,69,70,71,78,79,80]
              ];
var rows = [[0,1,2,3,4,5,6,7,8],
            [9,10,11,12,13,14,15,16,17],
            [18,19,20,21,22,23,24,25,26],
            [27,28,29,30,31,32,33,34,35],
            [36,37,38,39,40,41,42,43,44],
            [45,46,47,48,49,50,51,52,53],
            [54,55,56,57,58,59,60,61,62],
            [63,64,65,66,67,68,69,70,71],
            [72,73,74,75,76,77,78,79,80],
            ];
var cols = [[0,9,18,27,36,45,54,63,72],
            [1,10,19,28,37,46,55,64,73],
            [2,11,20,29,38,47,56,65,74],
            [3,12,21,30,39,48,57,66,75],
            [4,13,22,31,40,49,58,67,76],
            [5,14,23,32,41,50,59,68,77],
            [6,15,24,33,42,51,60,69,78],
            [7,16,25,34,43,52,61,70,79],
            [8,17,26,35,44,53,62,71,80],
            ];
var clique_list = [squares, rows, cols];
var neighbors = {};


class MyStack {
  constructor(cells = [], list = []){
    this.cells = cells;
    this.stack = list; // stack of boards
  }

  string(){
    return this.stack;
  }

  push(args){
    this.cells.push(args[0]);
    this.stack.push(args[1]);
  }

  pop(){
    return [this.cells.pop(), this.stack.pop()];
  }
}


function makeNeighbors(){
  for (var cell=0; cell<81; cell++){
    var temp = [];
    for (var clique=0; clique<Cliques.length; clique++){
      // console.log(Cliques[clique]);
      if (Cliques[clique].has(cell)){
        Cliques[clique].forEach(function (val){
            // console.log(val);
            if (!temp.includes(val)){
              temp.push(val);
            }
          });
      }
    }
    neighbors[cell] = temp;
  }
  // console.log(neighbors);
}

function printBoard(board){
  var result = "";
  for (var x=0; x<9; x++){
    for (var y=0; y<9; y++){
      result = result + board[x*9+y] + ",";
    }
    result+="\n";
  }
  console.log(result);
}

function compBoards(board0, board1){
  for (var x=0; x<81; x++){
    if (board0[x]!=board1[x] && board0[x]!='_' && board1[x]!='_'){
      console.log(x);
      return false;
    }
  }
  return true;
}



function findClique(cell, search_type){
  if (cell==-1){
    return clique_list[search_type][0];
  }
  for (var clique=0; clique<clique_list[search_type].length; clique++){
    if (clique_list[search_type][clique].includes(cell)){
      return clique_list[search_type][clique];
    }
  }
  return null;
}

function nextClique(clique, search_type){
  var index = clique_list[search_type].indexOf(clique);
  if (index!=8){
    return clique_list[search_type][index+1];
  }
  return null;
}



function nextOpenCell(board, prev_cell){
  for (var x=prev_cell+1; x<board.length; x++){
    if (board[x]=='_'){
      return x;
    }
  }
  return null;
}

function nextOpenCellinClique(board, prev_cell, clique){
  var start = 0;
  if (clique.includes(prev_cell)){
    start = clique.indexOf(prev_cell)+1;
  }
  for (var x=start; x<clique.length; x++){
    if (board[clique[x]]=='_'){
      return clique[x];
    }
  }
  return null;
}



function canPlace(board, cell, num){
  for (var x=0; x<neighbors[cell].length; x++){
    if (board[neighbors[cell][x]]==num){
      return false;
    }
  }
  return true;
}

function soleCandidate(board, cell){
  var candidate = 0;
  for (var num=1; num<10; num++){
    if (canPlace(board,cell,num)){
      if (candidate==0){
        candidate=num;
      }
      else {
        return 0;
      }
    }
  }
  return candidate;
}

function nextSoleCandidate(board, prev_cell){
  for (var x=prev_cell+1; x<board.length; x++){
    if (board[x]=='_'){
      var num = soleCandidate(board,x);
      if (num!=0){
        return [x,num];
      }
    }
  }
  return [81,0];
}



function nextValidGuess(board, cell, num){
  var temp = [0,false];
  for (var guess=num; guess<10; guess++){
    if (canPlace(board,cell,guess)){
      if (temp[0]==0){
        temp = [guess,true];
      }
      else {
        return [temp[0],false];
      }
    }
  }
  return temp;
}


function writeCell(board, cell, num, stack){
  board[cell] = num;
  stack.push([cell,num]);
}



// NEW_CELL = 0
// FIND_NEXT_CELL = 1
// BACKTRACK = 2
// TEST_CLIQUE = 3
// NEXT_CLIQUE = 4
// NEXT_SEARCH_TYPE = 5
// NEXT_NUM = 6
// REPEAT = 7
// NAIVE_TIME = 8
// START_STRAT = 9
// FIND_NEXT_FORCED = 10

function execute(board, solved=[]){
  makeNeighbors();
  var mystack = new MyStack();
  var state = 0;

  while (state!=5){
    switch (state){

      case 0:
        // console.log("CASE 0");
        var sole_candidate = nextSoleCandidate(board,-1);
        while (sole_candidate[0]!=81){
          // console.log(sole_candidate);
          board[sole_candidate[0]] = sole_candidate[1];
          sole_candidate = nextSoleCandidate(board,sole_candidate[0]);
        }
        printBoard(board);
        console.log(compBoards(board,solved));
        state = 1;
        break;

      case 1:
        // console.log("CASE 1");
        var cells_changed = 0;
        for (var cur_num=1; cur_num<10; cur_num++){
          for (var search_type=0; search_type<3; search_type++){
            var clique = findClique(0,search_type);
            while (clique!=null){
              // console.log(clique);
              var sole_candidate = [-1, false];
              var cell = nextOpenCellinClique(board,-1,clique);
              while (cell!=null){
                if (canPlace(board,cell,cur_num)){
                  if (sole_candidate[0]==-1){
                    sole_candidate = [cell, true];
                  }
                  else {
                    sole_candidate = [cell, false];
                  }
                }
                cell = nextOpenCellinClique(board,cell,clique);
              }
              if (sole_candidate[1]){
                board[sole_candidate[0]] = cur_num;
                cells_changed+=1;
              }
              clique = nextClique(clique,search_type);
            }
          }
        }
        printBoard(board);
        console.log(compBoards(board,solved));
        if (cells_changed!=0){
          state = 0;
        }
        else {
          state = 2;
        }
        break;

      case 2:
        // console.log("CASE 2");



        // printBoard(board);
        // console.log(compBoards(board,solved));
        state = 3;
        break;

      case 3:
        // console.log("CASE 3");
        // printBoard(board);
        // console.log(compBoards(board,solved));
        state = 4;
        break;

      case 4:
        // console.log("CASE 4");
        // printBoard(board);
        // console.log(compBoards(board,solved));
        state = 5;
        break;
    }
  }

  return board;
}




var test_board_easy = ['_', '_', '_', '_', '_', '_', '_', '_', '_',
                      '_', '7', '9', '_', '5', '_', '1', '8', '_',
                      '8', '_', '_', '_', '_', '_', '_', '_', '7',
                      '_', '_', '7', '3', '_', '6', '8', '_', '_',
                      '4', '5', '_', '7', '_', '8', '_', '9', '6',
                      '_', '_', '3', '5', '_', '2', '7', '_', '_',
                      '7', '_', '_', '_', '_', '_', '_', '_', '5',
                      '_', '1', '6', '_', '3', '_', '4', '2', '_',
                      '_', '_', '_', '_', '_', '_', '_', '_', '_'];

var solved_test_board_easy = ["3","4","5","8","7","1","2","6","9",
                              "2","7","9","6","5","3","1","8","4",
                              "8","6","1","4","2","9","5","3","7",
                              "1","9","7","3","4","6","8","5","2",
                              "4","5","2","7","1","8","3","9","6",
                              "6","8","3","5","9","2","7","4","1",
                              "7","3","8","2","6","4","9","1","5",
                              "5","1","6","9","3","7","4","2","8",
                              "9","2","4","1","8","5","6","7","3"];

var test_board_hard = ["_","_","_","_","_","3","_","1","7",
                      "_","1","5","_","_","9","_","_","8",
                      "_","6","_","_","_","_","_","_","_",
                      "1","_","_","_","_","7","_","_","_",
                      "_","_","9","_","_","_","2","_","_",
                      "_","_","_","5","_","_","_","_","4",
                      "_","_","_","_","_","_","_","2","_",
                      "5","_","_","6","_","_","3","4","_",
                      "3","4","_","2","_","_","_","_","_"];

var solved_test_board_hard = ["2","9","4","8","6","3","5","1","7",
                              "7","1","5","4","2","9","6","3","8",
                              "8","6","3","7","5","1","4","9","2",
                              "1","5","2","9","4","7","8","6","3",
                              "4","7","9","3","8","6","2","5","1",
                              "6","3","8","5","1","2","9","7","4",
                              "9","8","6","1","3","4","7","2","5",
                              "5","2","1","6","7","8","3","4","9",
                              "3","4","7","2","9","5","1","8","6"];


function test(){
  // console.log(Cliques);

  // test_stack = new MyStack();
  // console.log(test_stack.string());
  // test_stack.push([80,3]);
  // test_stack.push([1,9]);
  // console.log(test_stack.string());

  // console.log(test_board);

  // makeNeighbors();
  // console.log(neighbors);

  // console.log(findClique(9,1));
  // console.log(nextClique(findClique(80,0),0));

  // console.log(nextOpenCell(test_board,0));
  // console.log(nextOpenCellinClique(test_board,9,findClique(9,1)));

  // console.log(canPlace(test_board,9,3));
  // console.log(soleCandidate(test_board, 40));
  // console.log(nextSoleCandidate(test_board,-1));

  // console.log(nextValidGuess(test_board,40,1));

  // console.log(test_board);
  // printBoard(test_board);

  printBoard(test_board_hard);
  printBoard(execute(test_board_hard,solved_test_board_hard));
}

test();
