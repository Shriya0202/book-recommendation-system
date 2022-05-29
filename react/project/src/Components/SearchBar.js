import React, { useEffect, useState } from "react";
import "./SearchBar.css";
import SearchIcon from '@mui/icons-material/Search';
import CloseIcon from '@mui/icons-material/Close';



function SearchBar() {
  const [name,setName]=useState("");
  const [suggestions,setSuggestions]=useState("");
  const [bookTitles,setBookTitles]=useState("");
  const[filteredData, setFilteredData]=useState([]);
  const[EnteredWord, setEnteredWord]=useState("");
  const[showSearchIcon, setShowSearchIcon]=useState(false);
  const[showOptions, setShowOptions]=useState(true);
  useEffect(()=> {
    fetch("http://localhost:5000/api",{method: 'GET'})
    .then((res) => res.json())
        .then((json) => {
        setBookTitles(json.json_data["Title"][0])
        })},[])
  

  function sendBookName(){
    setFilteredData([]);
    fetch("http://localhost:5000/prediction/"+EnteredWord,{method: 'GET'})
    .then((res) => res.json())
            .then((json) => {
            setSuggestions(json)
            setShowSearchIcon(false);
            })
  } 
  
   
    
  const handleFilter = (event) => {
    const searchWord = event.target.value 
    //setShowSearchIcon(false);
    setEnteredWord(searchWord);
    setShowOptions(true);
    const newFilter = bookTitles && bookTitles.filter((value)=>{
      return value.toLowerCase().includes(searchWord.toLowerCase());
    });
    if(searchWord==""){
      setFilteredData([]);
    }else{
      setFilteredData(newFilter);
    }      
  };  
  
  const clearInput= () => {
    setFilteredData([]);
    setEnteredWord("");
    setShowSearchIcon(true);
  }

  return (
    <div className="search">
        <div className="searchInputs">
            <input type= "text" placeholder="Enter a Book Name" id="search" value={EnteredWord} onChange={handleFilter} />
           <button type = "button" > 
            <div className="searchIcon">
              {filteredData.length === 0 || showSearchIcon?( <SearchIcon onClick={sendBookName}/> ):( <CloseIcon id="clearBtn" onClick={clearInput}/>)}
              
            </div>
            </button>
        </div>
        {(filteredData.length!==0 && showOptions) &&(
        <div className="dataResult" >
         {filteredData.slice(0, 15).map((value,key)=>
          {return (
            <a className="dataItem" onClick = { () => { setShowOptions(false); 
            setShowSearchIcon(true); 
            setEnteredWord(value); }} >
              <p>{value}</p>
            </a>);
          })}
        </div>)}
     <div className="bookRecs"> {suggestions}</div> 
    </div>

  )
}

export default SearchBar
