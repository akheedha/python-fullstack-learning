import "./App.css";
import image from "./images/hello.jpg";

function App() {
  let greeting = "Hello World";

  return (
    <div>
      <h1 className="greetingStyle">{greeting}</h1>
      <img src={image} alt="Hello" />
    </div>
  );
}

export default App;