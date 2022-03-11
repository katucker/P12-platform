// Code for interacting with visualizations in the web pages.
        
function displayVerticalBarChart(data, title, xaxis, yaxis) {

    const svg = d3.select('svg');
    const svgContainer = d3.select('#container');
    
    const margin = 80;
    const width = 1000 - 2 * margin;
    const height = 600 - 2 * margin;
    const extension = 10;
    
    // Set height and width attributes for easy reference in other functions.
    svg.attr("height", height)
    svg.attr("width", width)

    const chart = svg.append('g')
      .attr('transform', `translate(${margin}, ${margin})`)
      .attr("class", "chart");

    const xScale = d3.scaleBand()
      .range([0, width])
      .domain(data.map((s) => s.metric))
      .padding(0.4)
    
    const yScale = d3.scaleLinear()
      .range([height, 0])
      .domain([0, 100]);

    // vertical grid lines
    // const makeXLines = () => d3.axisBottom()
    //   .scale(xScale)

    const makeYLines = () => d3.axisLeft()
      .scale(yScale)

    chart.append('g')
      .attr('transform', `translate(0, ${height})`)
      .call(d3.axisBottom(xScale));

    chart.append('g')
      .call(d3.axisLeft(yScale));

    // vertical grid lines
    // chart.append('g')
    //   .attr('class', 'grid')
    //   .attr('transform', `translate(0, ${height})`)
    //   .call(makeXLines()
    //     .tickSize(-height, 0, 0)
    //     .tickFormat('')
    //   )

    chart.append('g')
      .attr('class', 'grid')
      .call(makeYLines()
        .tickSize(-width, 0, 0)
        .tickFormat('')
      )

    const barGroups = chart.selectAll()
      .data(data)
      .enter()
      .append('g')

    barGroups
      .append('rect')
      .attr('class', 'bar')
      .attr('x', (g) => xScale(g.metric))
      .attr('y', (g) => yScale(g.value))
      .attr('height', (g) => height - yScale(g.value))
      .attr('width', xScale.bandwidth())
//       .on('mouseenter', function (actual, i) {
//         d3.selectAll('.value')
//           .attr('opacity', 0)
// 
//         d3.select(this)
//           .transition()
//           .duration(300)
//           .attr('opacity', 0.6)
//           .attr('x', (a) => xScale(a.metric) - 5)
//           .attr('width', xScale.bandwidth() + 10)
// 
//         const y = yScale(actual.value)
// 
//         line = chart.append('line')
//           .attr('id', 'limit')
//           .attr('x1', 0)
//           .attr('y1', y)
//           .attr('x2', width)
//           .attr('y2', y)
// 
//         barGroups.append('text')
//           .attr('class', 'divergence')
//           .attr('x', (a) => xScale(a.metric) + xScale.bandwidth() / 2)
//           .attr('y', (a) => yScale(a.value) + 30)
//           .attr('fill', 'white')
//           .attr('text-anchor', 'middle')
//           .text((a, idx) => {
//             const divergence = (a.value - actual.value).toFixed(1)
//             
//             let text = ''
//             if (divergence > 0) text += '+'
//             text += `${divergence}%`
// 
//             return idx !== i ? text : '';
//           })
// 
//       })
//       .on('mouseleave', function () {
//         d3.selectAll('.value')
//           .attr('opacity', 1)
// 
//         d3.select(this)
//           .transition()
//           .duration(300)
//           .attr('opacity', 1)
//           .attr('x', (a) => xScale(a.metric))
//           .attr('width', xScale.bandwidth())
// 
//         chart.selectAll('#limit').remove()
//         chart.selectAll('.divergence').remove()
//       })

    barGroups 
      .append('text')
      .attr('class', 'value')
      .attr('x', (a) => xScale(a.metric) + xScale.bandwidth() / 2)
      .attr('y', (a) => yScale(a.value) + 30)
      .attr('text-anchor', 'middle')
      .text((a) => `${a.value}%`)
    
    svg
      .append('text')
      .attr('class', 'label')
      .attr('x', -(height / 2) - margin)
      .attr('y', margin / 2.4)
      .attr('transform', 'rotate(-90)')
      .attr('text-anchor', 'middle')
      .text(yaxis)

    svg.append('text')
      .attr('class', 'label')
      .attr('x', width / 2 + margin)
      .attr('y', height + margin * 1.7)
      .attr('text-anchor', 'middle')
      .text(xaxis)

    svg.append('text')
      .attr('class', 'title')
      .attr('x', width / 2 + margin)
      .attr('y', 40)
      .attr('text-anchor', 'middle')
      .text(title)
      
// Add all the reference lines, but make them not visible.
	barGroups
		.append('line')
    	.attr("class", "nationalrefline")
    	.attr("x1", (g) => xScale(g.metric) - extension)
    	.attr("y1", (g) => yScale(g.national))
   		.attr("x2", (g) => xScale(g.metric) + xScale.bandwidth() + extension)
    	.attr("y2", (g) => yScale(g.national))
    	.style("opacity", 0)
    	.attr("stroke-width", 3)

	barGroups
		.append('line')
    	.attr("class", "peerrefline")
    	.attr("x1", (g) => xScale(g.metric) - extension)
    	.attr("y1", (g) => yScale(g.peer))
   		.attr("x2", (g) => xScale(g.metric) + xScale.bandwidth() + extension)
    	.attr("y2", (g) => yScale(g.peer))
    	.style("opacity", 0)
    	.attr("stroke-width", 3)
  
	barGroups
		.append('line')
    	.attr("class", "regionalrefline")
    	.attr("x1", (g) => xScale(g.metric) - extension)
    	.attr("y1", (g) => yScale(g.regional))
   		.attr("x2", (g) => xScale(g.metric) + xScale.bandwidth() + extension)
    	.attr("y2", (g) => yScale(g.regional))
    	.style("opacity", 0)
    	.attr("stroke-width", 3)
}

function toggleBarValues(cb, prog) {
	height = 600-160;
	yScale = d3.scaleLinear()
      .range([height, 0])
      .domain([0, 100]);
	barGroup = d3.selectAll('.bar');
	curdata = barGroup.data();
	if (cb.checked) {
		if (prog === "headstart") {
			curdata.forEach( (g) => g.value += g.headstart)
		} else {
      		curdata.forEach( (g) => g.value += g.lunch)
		}
	} else {
		if (prog === "headstart") {
			curdata.forEach( (g) => g.value -= g.headstart)
		} else {
      		curdata.forEach( (g) => g.value -= g.lunch)
		}
	}
	barGroup
		.data(curdata)
		.transition()
        .duration(300)
      	.attr('y', (g) => yScale(g.value))
        .attr('height', (g) => height - yScale(g.value))
}

function toggleReferenceLines(cb, ref) {
    if (ref === "national") {
    	lines = d3.selectAll(".nationalrefline");
    } else if (ref === "peer") {
    	lines = d3.selectAll(".peerrefline");
    } else {
    	lines = d3.selectAll(".regionalrefline");
    }
	if (cb.checked) {
    	lines.style("opacity", 1);
	} else {
    	lines.style("opacity", 0)
	}
}

