// from data.js
var tableData = data;

// Get a reference to the table and table body
var tbody = d3.select("tbody");

function buildTable(table) {
    table.forEach((sightings) => {
        var row = tbody.append("tr");
        Object.entries(sightings).forEach(([key, value]) => {
            var cell = tbody.append("td");
            cell.text(value);
        });
    });
}

buildTable(tableData);

// Select the Filter Table button
var submit = d3.select("#filter-btn");
submit.on("click", function() {
    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Get the value property of the input element
    var inputValueDate = d3.select("#datetime").property("value");
    var inputValueCity = d3.select("#city").property("value");
    var inputValueState = d3.select("#state").property("value");
    var inputValueCountry = d3.select("#country").property("value");
    var inputValueShape = d3.select("#shape").property("value");

    // Filtered data array
    var filteredData = tableData.filter(tableDatum => 
        tableDatum.datetime === inputValueDate || 
        tableDatum.city === inputValueCity ||
        tableDatum.state === inputValueState ||
        tableDatum.country === inputValueCountry ||
        tableDatum.shape === inputValueShape);

    // Clear table and message if it exists
    tbody.html("");
    d3.select("span").html("");


    if(filteredData === undefined || filteredData.length == 0) {
        d3.select("span").text("Sorry, no UFO sightings for the selection filter(s)!").style("font-size", "20px");
    }
    else {
        // Display new table with filtered data
        buildTable(filteredData);
    }

    // Clear filters
    d3.select("#datetime").node().value = "";
    d3.select("#city").node().value = "";
    d3.select("#state").node().value = "";
    d3.select("#country").node().value = "";
    d3.select("#shape").node().value = "";
});

// Select the Reset button
var submit = d3.select("#un-filter-btn");
submit.on("click", function() {
    // Prevent the page from refreshing
    d3.event.preventDefault();

    // Clear table and message if it exists
    tbody.html("");
    d3.select("span").html("");
    
    // Rebuild full table
    buildTable(tableData);
})