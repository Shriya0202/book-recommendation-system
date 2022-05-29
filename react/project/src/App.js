
import './App.css';
import Header from "./Components/Header";
import BookRecs from "./Components/BookRecs";
import Footer from "./Components/Footer";
import SearchBar from "./Components/SearchBar";


function App() {
  return (
  <div className='App'>
    <Header/>
    <SearchBar placeholder="Enter a Book Name"/>
    <BookRecs/>
    <Footer/>
  </div>
  );

}

export default App;
