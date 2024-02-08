import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./components/pages/LandingPage";
import Login from "./components/pages/Login";
import Registration from "./components/pages/Registration";
import NotFound from "./components/pages/NotFound";
import "./App.css";

const Router = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" exact element={<LandingPage />} />
        <Route path="/login" exact element={<Login />} />
        <Route path="/register" exact element={<Registration />} />
        <Route path="/*" exact element={<NotFound />} />
      </Routes>
    </BrowserRouter>
  );
};

export default Router;