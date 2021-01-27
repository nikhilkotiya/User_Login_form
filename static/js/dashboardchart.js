
var order_status={{ order_status }}



window.onload=function(){

debugger;
// order status donut chart
new Chart(document.getElementById("orderstatusdonut"), {
    type: 'doughnut',
    data: {
      labels: order_status.labels,
      datasets: [{
        label: "Order Status",
        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f"],
        data: order_status.data,
      }]
    },
    options: {
      title: {
        display: true,
        position: "bottom",
	    labels: {
	        fontSize: 5
	      }
      }
    }
});

//sell charts
new Chart(document.getElementById("selllinechart"), {
  type: 'line',
  data: {
    labels: [1500,1600,1700,1750,1800,1850,1900,1950,1999,2050],
    datasets: [{ 
        data: [86,114,106,106,107,111,133,221,783,2478],
        label: "India",
        borderColor: "#3e95cd",
        fill: false
      },
    ]
  },
  options: {
    title: {
      display: true,
    }
  }
});



}