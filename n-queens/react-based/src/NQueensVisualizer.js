import React, { Component } from 'react'

// 1. Render the board with number of squares
// 2. Create a state variable with set of queens placed
// 3. Allow queens to be placed in each square
// 4. Re-render when each queen is placed
 
export default class NQueensVisualizer extends Component {
  render() {
    return (
      <div>N-Queens Visualizer {this.props.numSquares} </div>
    )
  }
}
