import './App.css';

/*
const rectInfos = [
  [{top:"0px",left:"0px",color:"white"},{top:"0px",left:"50px",color:"black"},
    {top:"0px",left:"100px",color:"white"},{top:"0px",left:"150px",color:"black"},
    {top:"0px",left:"200px",color:"white"},{top:"0px",left:"250px",color:"black"},
    {top:"0px",left:"300px",color:"white"},{top:"0px",left:"350px",color:"black"}],
  [{top:"50px",left:"0px",color:"black"},{top:"50px",left:"50px",color:"white"},
    {top:"50px",left:"100px",color:"black"},{top:"50px",left:"150px",color:"white"},
    {top:"50px",left:"200px",color:"black"},{top:"50px",left:"250px",color:"white"},
    {top:"50px",left:"300px",color:"black"},{top:"50px",left:"350px",color:"white"}],
  [{top:"100px",left:"0px",color:"white"},{top:"100px",left:"50px",color:"black"},
    {top:"100px",left:"100px",color:"white"},{top:"100px",left:"150px",color:"black"},
    {top:"100px",left:"200px",color:"white"},{top:"100px",left:"250px",color:"black"},
    {top:"100px",left:"300px",color:"white"},{top:"100px",left:"350px",color:"black"}],
  [{top:"150px",left:"0px",color:"black"},{top:"150px",left:"50px",color:"white"},
    {top:"150px",left:"100px",color:"black"},{top:"150px",left:"150px",color:"white"},
    {top:"150px",left:"200px",color:"black"},{top:"150px",left:"250px",color:"white"},
    {top:"150px",left:"300px",color:"black"},{top:"150px",left:"350px",color:"white"}],
]

const width = 50

const rects = rectInfos.map((row,i)=>
   row.map((svgElement,j)=>
       <svg key={`i+${i}+${j}+j`} style={{width:"50px", height:"50px",position: "absolute", top:svgElement.top, left:svgElement.left}}>
           <rect style={{fill:svgElement.color, width:"50px", height:"50px"}} />
       </svg>
   )
)

        <div style={{position: "relative", width:"1000px", height:"300px"}}>
          {rects}
        </div>
*/

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <h1> N - Queens (React-based) </h1>
      </header>
    </div>
  );
}

export default App;
