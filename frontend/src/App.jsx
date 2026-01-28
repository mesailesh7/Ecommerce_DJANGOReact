import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import ProductList from "../pages/ProductList.jsx";
import ProductDetails from "../pages/ProductDetails.jsx";
import React from 'react'


const App = () => {
    return (
        <>
            <Router>
                <Routes>
                    <Route path="/" element={<ProductList/>}/>
                    <Route path="/product/:id" element={<ProductDetails/>}/>
                </Routes>
            </Router>
        </>
    )
}
export default App
