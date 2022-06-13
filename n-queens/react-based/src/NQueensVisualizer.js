import React, { Component } from 'react'
import Square from './Square'

// 1. Implement Rendering in the Square Class
// 2. Allow queens to be placed in each square
// 3. Re-render when each queen is placed
 
class NQueensVisualizer extends Component {

  constructor(props) {
    super(props)
    this.state = {
      width : 100,
      colors : ["#000000", "#FFFFFF"],
      num_queens_placed: 0
    }
  }

  render() {
    const numSquaresConst = Number(this.props.numSquares)
    return (
      <>
      { Array.apply(0, Array(numSquaresConst * numSquaresConst)).map((_, i) => (
        <Square
          key = {i}
          row={Math.floor(i / numSquaresConst)}
          column={i % numSquaresConst}
          size={this.state.width}
          color = {this.state.colors[i % 2]}
          />))
      }
      </>
    )
  }
}

export default NQueensVisualizer;