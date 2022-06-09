import React, { useRef, useState } from 'react'
import NQueensVisualizer from './NQueensVisualizer';

function App() {
  const numSquaresRef = useRef()
  const [numSquares, setNumSquares] = useState(8);

  function handleRenderBoard(e) {
    const numSquaresCurValue = numSquaresRef.current.value
    if (Number(numSquaresCurValue)) {
      setNumSquares(numSquaresCurValue)
    } else {
      alert("Please enter a valid number")
    }
    numSquaresRef.current.value = null
  }

  function handleIntegerValue(e) {
    if (!Number(e.target.value)) {
      alert("Only numbers are valid")
    }
  }

  return (
    <>
        <h1> N-Queens Visualizer</h1>
        <label> Enter number of queens: </label>
        <input ref={numSquaresRef} type="text" onChange={handleIntegerValue} />
        <button onClick={handleRenderBoard}> Render Board </button>
        <NQueensVisualizer numSquares={numSquares}/>
    </>
  );
}

export default App;
