// d3.csv("static/resources/breed_labels.csv").then(function(breedData){
//     console.log(breedData);
//     console.log("test");
//     // Object.entries(breedData).forEach(([key, value]) => {
//     //   console.log(`${key}: ${value}`);
//   });
 console.log('Test');


  // Load data from hours-of-tv-watched.csv
d3.csv("static/resources/breed_labels.csv").then(function(breedData) {
  console.log(breedData);
  breedData.forEach(function(data) {
    console.log(data.BreedName)
  });

    // var breedName = Object.values(sampledata.breed);
    // // var wfreq = sampledata.metadata[key].wfreq;
    // // console.log(wfreq)
    // var dropdownMenu = d3.select("#breed");




//   // Use the list of sample names to populate the select options
//   d3.selectAll("#breed").on("change", optionChanged);
//   var dropdownMenu = d3.select("#breed");
//   // Assign the value of the dropdown menu option to a variable
//   var ID = dropdownMenu.property("value");
//   var key = Object.keys(result).find(key => result[key] === ID);
//   var samples = Object.values(sampledata.samples);
//   var otu_id = sampledata.samples[key].otu_ids.slice(0,10).map(x=> `OTU ${x}`);
//   var sample_values = sampledata.samples[key].sample_values.slice(0,10).reverse();
//   var otu_labels = sampledata.samples[key].otu_labels.slice(0,10);

//   // Use the first sample from the list to build the initial plots
//   var firstSample = labels[0];
//   buildCharts(labels);
//   buildMetadata(labels);
//     });
// }

// function optionChanged(newSample) {
//   // Fetch new data each time a new sample is selected 
//   // The function call is in the HTML file as <select id="selDataset" onchange="optionChanged(this.value)"></select>
//   buildCharts(newSample);
//   buildMetadata(newSample);
// }

// // Initialize the dashboard
// init();