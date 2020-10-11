d3.csv("db/adoption_data.csv").then(function(data) {
  console.log(data[0]);
});

trace1 = {
    type: 'bar', 
    x:  
    y: 
  };
  data = [trace1];
  layout = {
    title: 'Popular Adoption Breeds ', 
    xaxis: {title: 'Breed'}, 
    yaxis: {title: 'Adoption Rate'}, 
    plot_bgcolor: 'rgb(230, 230,230)'
  };
  Plotly.plot('plotly-div', {
    data: data,
    layout: layout
  });