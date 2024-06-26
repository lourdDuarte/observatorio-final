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


function draw_basic_line_chart(data,mes,text, id){
  
  var options = {
    series: [{
      name: "data",
      data: data
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
    text: text,
    align: 'center'
  },
  grid: {
    row: {
      colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
      opacity: 0.5
    },
  },
  xaxis: {
    categories: mes,
  }
  };

  var chart = new ApexCharts(document.querySelector("#"+id), options);
  chart.render();
}


function draw_column_chart(data, meses, text, id){
 
  var options = {
    series: [{
    
    data: data
  }],
    chart: {
    height: 350,
    type: 'bar',
  },
 
  
  
  xaxis: {
    categories: meses,
    position: 'bottom',
   
    
   
  },
 
  title: {
    text: text,
    offsetY: 5,
    align: 'center',
    
   
  }
  };

  var chart = new ApexCharts(document.querySelector("#"+id), options);
  chart.render();
}