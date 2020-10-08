function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}
//
function userInput(){
  
}

function ajaxPostRequest(path, data, callback){
    let request = new XMLHttpRequest();
    request.onreadystatechange = function(){
        if (this.readyState===4&&this.status ===200){
            callback(this.response);
        }
    };
    request.open("POST", path);
    request.send(data);
}

function onload() {
  //console.log(3)
  ajaxGetRequest("/pieChart", showPiechart);
  ajaxGetRequest("/table", showTable);
  //ajaxPostRequest("/POSTpieChart", 3 , postPiechart);
  let button = document.getElementById("button")
  button.onclick = filterByyear
  let button1 = document.getElementById("buttonBackwards")
  button1.onclick = filterByboroughforYears
  console.log(3)
}

function filterByyear(){
  ajaxPostRequest("/POSTpieChart", 3 , postPiechart);
}

function filterByboroughforYears(){
  ajaxGetRequest("/pieChart", showPiechart);
}


function showPiechart(response){
  //console.log(response);
  let resp = JSON.parse(response);
  //console.log(3)
  //console.log(resp)
  //console.log(resp[0])
  let insertGraph = document.getElementById("pieChart");
  let trace1 = [{
  values: [resp[0], resp[1], resp[2], resp[3], resp[4]],
  labels: ['Manhattan', 'Bronx', 'Brooklyn', 'Queens', 'Staten Island'], 
  type: 'pie'
}];
  let layout = {
    title: 'New York City Borough Homelessness for Years 2009 - 2012',
    height:1000,
    width:1000
  }
  Plotly.newPlot('pieChart', trace1, layout);
//   myPlot.on('plotly_click', function(data){
//     var pts = '';
//     for(var i=0; i < data.points.length; i++){
//         pts = 'x = '+data.points[i].x +'\ny = '+
//             data.points[i].y.toPrecision(4) + '\n\n';
//     }
//     alert('Closest point clicked:\n\n'+pts);
// });


}

function showTable(response){
  //console.log(3)
  let resp = JSON.parse(response);
  //console.log(resp)
  //console.log(resp[0])
  let trace1 = [
      ['Manhattan', 'Bronx', 'Brooklyn', 'Queens','Staten Island'],
      [resp[0][0], resp[1][0], resp[2][0], resp[3][0], resp[4][0]],
      [resp[0][1], resp[1][1], resp[2][1], resp[3][1], resp[4][1]],
      [resp[0][2], resp[1][2], resp[2][2], resp[3][1], resp[4][2]],
      [resp[0][3], resp[1][3], resp[2][3], resp[3][1], resp[4][3]]]
  let layout = [{
  type: 'table',
  header: {
    values: [["<b>Homeless Population Amounts By Borough</b>"], ["<b>2009</b>"],
				 ["<b>2010</b>"], ["<b>2011</b>"], ["<b>2012</b>"]],
    align: "center",
    line: {width: 1, color: 'black'},
    fill: {color: "grey"},
    font: {family: "Arial", size: 12, color: "white"}
  },
  cells: {
    values: trace1,
    align: "center",
    line: {color: "black", width: 1},
    font: {family: "Arial", size: 11, color: ["black"]}
  }
}]

Plotly.plot('table', layout);

  
}

function postPiechart(response){
  console.log(3)
  let resp = JSON.parse(response);
  let trace1 = [{
  values: [resp[0], resp[1], resp[2], resp[3]],
  labels: ['2009', '2010', '2011', '2012'], 
  type: 'pie'
}];
let layout = {
    title: 'New York City Homelessness for Years 2009 - 2012',
    height:1000,
    width: 1000
  }
  Plotly.newPlot('pieChart', trace1, layout);
}



function showHi(){
  let firstName = document.getElementById("firstNameinput").value
  let lastName = document.getElementById("lastNameinput").value
  document.getElementById("Hi").innerHTML = "Hi " + firstName + " " + lastName
  
}


//make a button that when clicked turns the old graph into a pie chart that filters everything in the data set by year