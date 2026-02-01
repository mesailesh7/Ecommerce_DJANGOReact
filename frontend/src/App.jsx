import {BrowserRouter as Router, Route, Routes} from "react-router-dom";
import ProductList from "./pages/ProductList.jsx";
import ProductDetails from "./pages/ProductDetails.jsx";
import React from 'react'
import Navbar from "./components/Navbar.jsx";
import CartPage from "./pages/CartPage.jsx";

const App = () => {
    return (
        <>
            <Router>
                <Navbar/>
                <Routes>
                    <Route path="/" element={<ProductList/>}/>
                    <Route path="/product/:id" element={<ProductDetails/>}/>
                    <Route path="/cart" element={<CartPage/>}/>
                </Routes>
            </Router>
        </>
    )
}
export default App
