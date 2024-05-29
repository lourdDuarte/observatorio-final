function draw_line_chart(interanual,intermensual,mes, text, id)

{
  
  var options = {
    series: [
    {
      name: "Interanual",
      data: interanual
    },
    {
      name: "Intermensual",
      data: intermensual
    }
  ],
    chart: {
    height: 350,
    type: 'line',
    dropShadow: {
      enabled: true,
      color: '#000',
      top: 18,
      left: 7,
      blur: 10,
      opacity: 0.2
    },
    toolbar: {
      show: false
    }
  },
  colors: ['#77B6EA', '#545454'],
  dataLabels: {
    enabled: true,
  },
  stroke: {
    curve: 'smooth'
  },
  title: {
    text: text,
    align: 'left'
  },
  grid: {
    borderColor: '#e7e7e7',
    row: {
      colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
      opacity: 0.5
    },
  },
  markers: {
    size: 1
  },
  xaxis: {
    categories: mes,
    title: {
      text: 'Meses'
    }
  },
  yaxis: {
    title: {
      text: ' '
    },
    min: -30,
    max: 350
  },
  legend: {
    position: 'top',
    horizontalAlign: 'right',
    floating: true,
    offsetY: -25,
    offsetX: -5
  }
  };

  var chart = new ApexCharts(document.querySelector("#"+id), options);
  chart.render();
}


function draw_basic_line_chart(data,mes, id){
  
  var options = {
    series: [{
      name: "Desktops",
      data: [10, 41, 35, 51, 49, 62, 69, 91, 148]
  }],
    chart: {
    height: 350,
    type: 'line',
    zoom: {
      enabled: false
    }
  },
  dataLabels: {
    enabled: false
  },
  stroke: {
    curve: 'straight'
  },
  title: {
    text: 'Product Trends by Month',
    align: 'left'
  },
  grid: {
    row: {
      colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
      opacity: 0.5
    },
  },
  xaxis: {
    categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep'],
  }
  };

  var chart = new ApexCharts(document.querySelector("#"+id), options);
  chart.render();
}


function draw_column_chart(data, meses, id){
 
  var options = {
    series: [{
    
    data: [23, 31, 40, 101, 40, 36, 32, 23, 14, 48, 45, 42]
  }],
    chart: {
    height: 350,
    type: 'bar',
  },
 
  
  
  xaxis: {
    categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"],
    position: 'bottom',
   
    
   
  },
 
  title: {
    text: 'Monthly Inflation in Argentina, 2002',
   
    offsetY: 5,
    align: 'center',
    
   
  }
  };

  var chart = new ApexCharts(document.querySelector("#"+id), options);
  chart.render();
}